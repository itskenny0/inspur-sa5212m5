#!/usr/bin/env python3
"""Build a static BIOS menu reference from a UEFIExtract dump and IFRExtractor-RS."""

import argparse
import hashlib
import heapq
import json
from pathlib import Path
import re
import struct
import subprocess
import tempfile
import uuid

IMAGE_SHA256 = "927b893e0f5ae8c47702be9251307087f8f3523cc8e6e488437b787eca9d12ee"
VENDOR_FLAGS = {"InspurGenSetupFeature", "InspurSocketSetupFeatures",
                "InspurPchSetupFeatures", "InspurMgmtSetupFeature"}
CONTROLS = {"OneOf", "Numeric", "CheckBox", "String", "Password", "OrderedList",
            "Date", "Time", "Action", "Ref", "ResetButton"}
CONDITIONS = {"SuppressIf", "GrayOutIf", "DisableIf", "NoSubmitIf", "InconsistentIf", "WarningIf"}
EXPRS = {"True", "False", "Zero", "One", "Ones", "Uint8", "Uint16", "Uint32", "Uint64",
         "EqIdVal", "EqIdValList", "EqIdId", "QuestionRef1", "QuestionRef2", "QuestionRef3",
         "And", "Or", "Not", "Equal", "NotEqual", "LessThan", "LessEqual", "GreaterThan",
         "GreaterEqual", "BitwiseAnd", "BitwiseOr", "BitwiseNot", "ShiftLeft", "ShiftRight",
         "Add", "Subtract", "Multiply", "Divide", "Modulo", "Get", "RuleRef", "Undefined",
         "ToBoolean", "ToUint", "ToString", "StringRef1", "StringRef2", "Security", "This"}
RECORD = re.compile(r"^0x([0-9A-F]+):\s*(.*?)\s+\{ ((?:[0-9A-F]{2} )*[0-9A-F]{2}) \}", re.M | re.S)
FIELD = re.compile(r'(?:^|,? )([A-Za-z][A-Za-z0-9]*): (".*?"(?=,? [A-Za-z][A-Za-z0-9]*: |$)|\[[^]]*\]|.*?)(?=,? [A-Za-z][A-Za-z0-9]*: |$)', re.S)


def clean(value):
    return re.sub(r"\s+", " ", value.replace("\u2014", " - ").replace("\u2013", "-")).strip()


def fields(detail):
    result = {}
    for key, value in FIELD.findall(detail):
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        result[key] = clean(value)
    return result


def number(value, default=None):
    try:
        return int(value.split(",")[0], 0)
    except (ValueError, AttributeError):
        return default


def parse_ifr(text):
    roots, stack, count = [], [], 0
    for match in RECORD.finditer(text):
        offset, detail, raw = match.groups()
        data = bytes.fromhex(raw)
        if len(data) != data[1] & 0x7F:
            raise ValueError(f"Bad IFR record length at {offset}")
        kind, _, rest = detail.strip().partition(" ")
        node = {"offset": int(offset, 16), "kind": kind, "fields": fields(rest),
                "detail": clean(detail), "raw": data.hex(), "children": []}
        count += 1
        if kind == "End":
            if not stack:
                raise ValueError(f"Unexpected End at {offset}")
            stack.pop()
            continue
        (stack[-1]["children"] if stack else roots).append(node)
        if data[1] & 0x80:
            stack.append(node)
    if stack:
        raise ValueError("Unclosed IFR scopes")
    return roots, count


def walk(nodes):
    for node in nodes:
        yield node
        yield from walk(node["children"])


def package_list(output):
    kind, result = None, {"forms": [], "strings": []}
    for line in output.splitlines():
        if line.startswith("UEFI HII form packages:"):
            kind = "forms"
        elif line.startswith("UEFI HII string packages:"):
            kind = "strings"
        elif line.startswith("Framework"):
            kind = None
        elif kind and line.startswith("Index:"):
            entry = {k.replace(" ", ""): v for k, v in re.findall(r'(?:^|, )([^:]+): ([^,]+)', line)}
            if "Totalstrings" in entry:
                entry["TotalStrings"] = entry.pop("Totalstrings")
            entry = {k: number(v, v) for k, v in entry.items()}
            result[kind].append(entry)
    return result


def synthetic_strings(max_id):
    # A standard en-US string package with explicit unresolved labels.
    header = bytearray(52)
    struct.pack_into("<II", header, 4, 52, 52)
    struct.pack_into("<H", header, 44, 1)
    header[46:52] = b"en-US\0"
    body = b"".join(b"\x14" + f"[unresolved string 0x{i:X}]".encode("utf-16le") + b"\0\0"
                    for i in range(1, max_id + 1)) + b"\0"
    struct.pack_into("<I", header, 0, ((len(header) + len(body)) | (4 << 24)))
    return bytes(header) + body


def recover_short_english(data):
    """Adapt a standard 'en' package that IFRExtractor 1.6.1 overlooks."""
    for offset in range(len(data) - 49):
        if data[offset + 3] != 4:
            continue
        length = int.from_bytes(data[offset:offset + 3], "little")
        header_size, string_offset = struct.unpack_from("<II", data, offset + 4)
        if header_size != 49 or string_offset != 49 or not 49 < length <= len(data) - offset:
            continue
        if data[offset + 46:offset + 49] != b"en\0":
            continue
        header = bytearray(data[offset:offset + 46] + b"en-US\0")
        struct.pack_into("<III", header, 0, ((length + 3) | (4 << 24)), 52, 52)
        return bytes(header) + data[offset + 49:offset + length], {
            "original_offset": offset, "original_length": length, "original_language": "en",
            "extractor_language": "en-US", "note": "String block bytes unchanged; only temporary header is normalized."}
    return None, None


def source_metadata(body, root):
    for parent in body.parents:
        info = parent / "info.txt"
        if info.exists():
            text = info.read_text()
            match = re.search(r"File GUID: (.+)", text)
            if match:
                name = re.search(r"^Text: (.+)", text, re.M)
                return {"ffs_guid": match[1], "module": name[1] if name else match[1],
                        "path": str(body.relative_to(root))}
    return {"module": body.parent.name, "ffs_guid": None, "path": str(body.relative_to(root))}


def extract_sources(root, extractor):
    sources, by_hash = [], {}
    with tempfile.TemporaryDirectory(prefix="bios-menu-map-") as tmp:
        tmp = Path(tmp)
        for body in sorted(root.rglob("body.bin")):
            if any(p.is_dir() for p in body.parent.iterdir()) or body.stat().st_size < 256:
                continue
            listed = subprocess.run([extractor, str(body), "list"], capture_output=True, text=True)
            packages = package_list(listed.stdout)
            if not packages["forms"]:
                continue
            data = body.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            meta = source_metadata(body, root)
            if digest in by_hash:
                by_hash[digest]["aliases"].append(meta)
                continue
            recovery = None
            if not packages["strings"]:
                recovered, recovery = recover_short_english(data)
                if recovered:
                    data += recovered
                    adapted = tmp / "adapted.bin"
                    adapted.write_bytes(data)
                    relisted = subprocess.run([extractor, str(adapted), "list"], capture_output=True, text=True)
                    packages = package_list(relisted.stdout)
            source = {**meta, "sha256": digest, "aliases": [], "packages": packages,
                      "strings_resolved": bool(packages["strings"])}
            if recovery:
                source["string_header_recovery"] = recovery
            if not packages["strings"]:
                maximum = max(p["MaxStringId"] for p in packages["forms"])
                data += synthetic_strings(maximum)
                source["synthetic_string_labels"] = True
            temporary = tmp / (digest + ".bin")
            temporary.write_bytes(data)
            extracted = subprocess.run([extractor, str(temporary), "verbose"], capture_output=True, text=True)
            if extracted.returncode:
                raise ValueError(f"IFR extraction failed for {meta['path']}: {extracted.stdout}")
            by_hash[digest] = source
            sources.append(source)
            source["texts"] = []
            for form in packages["forms"]:
                choices = [s for s in packages["strings"]
                           if s.get("Language") == "en-US" and s["TotalStrings"] > form["MaxStringId"]]
                if source["strings_resolved"] and not choices:
                    raise ValueError(f"No complete English strings for {meta['path']}, package {form['Index']}")
                if choices:
                    def gap(s):
                        return min(abs(s["Offset"] + s["Length"] - form["Offset"]),
                                   abs(form["Offset"] + form["Length"] - s["Offset"]))
                    strings = min(choices, key=gap)
                    string_index = strings["Index"]
                else:
                    strings, string_index = None, 0
                outputs = list(tmp.glob(f"{digest}.bin.{form['Index']}.{string_index}.en-US.uefi.ifr.txt"))
                if len(outputs) != 1:
                    raise ValueError(f"Missing IFR output for {meta['path']}")
                source["texts"].append({"form_package": form, "string_package": strings,
                                        "text": outputs[0].read_text()})
            print(f"Extracted {meta['module']}: {len(source['texts'])} form package(s)")
    return sources


def flatten_expression(nodes):
    result = []
    for node in nodes:
        result.append(node)
        result.extend(flatten_expression(node["children"]))
    return result


def expression(nodes):
    stack = []
    binary = {"And": "and", "Or": "or", "Equal": "==", "NotEqual": "!=", "LessThan": "<",
              "LessEqual": "<=", "GreaterThan": ">", "GreaterEqual": ">=", "BitwiseAnd": "&",
              "BitwiseOr": "|", "ShiftLeft": "<<", "ShiftRight": ">>", "Add": "+",
              "Subtract": "-", "Multiply": "*", "Divide": "/", "Modulo": "%"}
    for node in flatten_expression(nodes):
        kind, f = node["kind"], node["fields"]
        if kind in {"EqIdVal", "EqIdValList", "EqIdId", "QuestionRef1"}:
            q = {"op": "question", "id": number(f.get("QuestionId"))}
            if kind == "QuestionRef1":
                stack.append(q)
            elif kind == "EqIdVal":
                stack.append({"op": "==", "args": [q, {"op": "constant", "value": number(f.get("Value"))}]})
            elif kind == "EqIdValList":
                vals = [int(x, 0) for x in re.findall(r"0x[0-9A-Fa-f]+|\d+", f.get("Values", ""))]
                stack.append({"op": "in", "args": [q], "values": vals})
            else:
                data = bytes.fromhex(node["raw"])
                a, b = struct.unpack_from("<HH", data, 2)
                stack.append({"op": "==", "args": [{"op": "question", "id": a}, {"op": "question", "id": b}]})
        elif kind.startswith("Uint") or kind in {"True", "False", "Zero", "One", "Ones"}:
            value = {"True": 1, "False": 0, "Zero": 0, "One": 1, "Ones": 0xFFFFFFFFFFFFFFFF}.get(kind)
            stack.append({"op": "constant", "value": number(f.get("Value"), value)})
        elif kind in binary and len(stack) >= 2:
            b, a = stack.pop(), stack.pop()
            stack.append({"op": binary[kind], "args": [a, b]})
        elif kind in {"Not", "BitwiseNot", "ToBoolean", "ToUint"} and stack:
            stack.append({"op": kind, "args": [stack.pop()]})
        else:
            return {"op": "unparsed", "text": " ; ".join(n["detail"] for n in flatten_expression(nodes))}
    return stack[0] if len(stack) == 1 else {"op": "unparsed", "text": " ; ".join(n["detail"] for n in flatten_expression(nodes))}


def qrefs(expr):
    if expr["op"] == "question":
        yield expr["id"]
    for arg in expr.get("args", []):
        yield from qrefs(arg)


def evaluate(expr, questions, vendor):
    op = expr["op"]
    if op == "constant":
        return expr["value"]
    if op == "question":
        q = questions.get(expr["id"], {})
        storage = q.get("storage") or {}
        return vendor if storage.get("name") in VENDOR_FLAGS and storage.get("offset") == 1 else None
    args = [evaluate(a, questions, vendor) for a in expr.get("args", [])]
    if op == "and":
        return False if any(a is not None and not a for a in args) else (None if None in args else all(args))
    if op == "or":
        return True if any(a is not None and bool(a) for a in args) else (None if None in args else any(args))
    if op == "unparsed" or any(a is None for a in args):
        return None
    if op == "in":
        return args[0] in expr["values"]
    if op in {"Not", "BitwiseNot", "ToBoolean", "ToUint"}:
        return {"Not": lambda: not args[0], "BitwiseNot": lambda: ~args[0],
                "ToBoolean": lambda: bool(args[0]), "ToUint": lambda: int(args[0])}[op]()
    if len(args) != 2:
        return None
    a, b = args
    try:
        return {"==": lambda: a == b, "!=": lambda: a != b, "<": lambda: a < b,
                "<=": lambda: a <= b, ">": lambda: a > b, ">=": lambda: a >= b,
                "&": lambda: a & b, "|": lambda: a | b, "<<": lambda: a << b,
                ">>": lambda: a >> b, "+": lambda: a + b, "-": lambda: a - b,
                "*": lambda: a * b, "/": lambda: a // b, "%": lambda: a % b}[op]()
    except (KeyError, ZeroDivisionError, ValueError):
        return None


def describe_expression(expr, questions):
    op = expr["op"]
    if op == "constant":
        return "unknown" if expr["value"] is None else f"0x{expr['value']:X}"
    if op == "question":
        q = questions.get(expr["id"], {})
        storage = q.get("storage") or {}
        if storage.get("name") and storage.get("offset") is not None:
            name = f"{storage['name']}[0x{storage['offset']:X}]"
        else:
            name = q.get("prompt") or f"Q0x{expr['id']:X}"
        if q.get("prompt"):
            name += f" ({q['prompt']})"
        return name
    if op == "unparsed":
        return expr["text"]
    args = [describe_expression(a, questions) for a in expr.get("args", [])]
    if op == "in":
        return f"{args[0]} in {expr['values']}"
    if len(args) == 1:
        return f"{op}({args[0]})"
    return f"({args[0]} {op} {args[1]})"


def build_packages(sources):
    packages = []
    for source in sources:
        for entry in source.pop("texts"):
            roots, count = parse_ifr(entry.pop("text"))
            for fs in (n for n in roots if n["kind"] == "FormSet"):
                package_id = f"{source['sha256'][:12]}-{entry['form_package']['Index']}"
                package = {"id": package_id, "source": source, **entry,
                           "guid": fs["fields"]["Guid"], "title": fs["fields"].get("Title", ""),
                           "help": fs["fields"].get("Help", ""), "opcode_count": count,
                           "forms": [], "conditions": {}, "varstores": {}, "questions": {}}
                for n in walk([fs]):
                    if n["kind"] in {"VarStore", "VarStoreEfi", "VarStoreNameValue"}:
                        f = n["fields"]
                        package["varstores"][number(f.get("VarStoreId"))] = f
                def descend(nodes, form=None, inherited=(), owner=None):
                    for n in nodes:
                        kind, f = n["kind"], n["fields"]
                        if kind in CONDITIONS:
                            leading = []
                            for child in n["children"]:
                                if child["kind"] not in EXPRS:
                                    break
                                leading.append(child)
                            cid = f"{package_id}-c{n['offset']:X}"
                            package["conditions"][cid] = {"id": cid, "kind": kind, "offset": n["offset"],
                                "expression": expression(leading), "raw_expression": [x["detail"] for x in flatten_expression(leading)]}
                            descend(n["children"][len(leading):], form, (*inherited, cid), owner)
                        elif kind == "Form":
                            new_form = {"id": number(f["FormId"]), "key": f"{package_id}-f{number(f['FormId']):X}",
                                        "title": f.get("Title", ""), "offset": n["offset"], "items": [],
                                        "conditions": list(inherited), "dynamic_labels": []}
                            package["forms"].append(new_form)
                            descend(n["children"], new_form, inherited)
                        elif form and kind in CONTROLS | {"Text", "Subtitle"}:
                            item = {"kind": kind, "offset": n["offset"], "fields": f,
                                    "prompt": f.get("Prompt", ""), "help": f.get("Help", ""),
                                    "question_id": number(f.get("QuestionId")),
                                    "conditions": list(inherited), "options": [], "defaults": [],
                                    "form_key": form["key"], "raw": n["raw"]}
                            vs = package["varstores"].get(number(f.get("VarStoreId")))
                            item["storage"] = ({"name": vs.get("Name"), "guid": vs.get("Guid"),
                                                "offset": number(f.get("VarOffset")),
                                                "size": number(vs.get("Size")), "varstore_id": number(f.get("VarStoreId"))}
                                               if vs else None)
                            if item["question_id"] is not None:
                                package["questions"][item["question_id"]] = item
                            form["items"].append(item)
                            descend(n["children"], form, inherited, item)
                        elif owner and kind in {"OneOfOption", "Default", "Value"}:
                            if kind == "OneOfOption":
                                owner["options"].append({"label": f.get("Option", ""), "value": (f.get("Value") or "").split(",")[0],
                                    "default": ", Default" in n["detail"], "manufacturing_default": ", MfgDefault" in n["detail"],
                                    "conditions": list(inherited)})
                            elif kind == "Default":
                                value = f.get("Value") if "Value" in f else f.get("String")
                                owner["defaults"].append({"store": f.get("DefaultId"), "value": value,
                                                          "type": "string" if "String" in f else "value",
                                                          "conditions": list(inherited)})
                            else:
                                owner["value_expression"] = expression(n["children"])
                        else:
                            if form and kind == "Guid" and "Label" in n["detail"]:
                                form["dynamic_labels"].append(n["detail"])
                            descend(n["children"], form, inherited, owner)
                descend(fs["children"])
                for condition in package["conditions"].values():
                    expr = condition["expression"]
                    condition["description"] = describe_expression(expr, package["questions"])
                    condition["stock_result"] = evaluate(expr, package["questions"], 1)
                    condition["unlocked_result"] = evaluate(expr, package["questions"], 0)
                    condition["vendor_flag"] = any((package["questions"].get(q, {}).get("storage") or {}).get("name") in VENDOR_FLAGS
                                                   and (package["questions"].get(q, {}).get("storage") or {}).get("offset") == 1
                                                   for q in qrefs(expr))
                packages.append(package)
    return packages


def menu_roots(packages, amitse):
    for p in packages:
        matches, pos = [], 0
        needle = uuid.UUID(p["guid"]).bytes_le
        while True:
            pos = amitse.find(needle, pos)
            if pos < 0:
                break
            if pos + 18 <= len(amitse):
                fid, = struct.unpack_from("<H", amitse, pos + 16)
                if any(f["id"] == fid for f in p["forms"]):
                    matches.append({"offset": pos, "form_id": fid})
            pos += 1
        p["amitse_entries"] = matches
        p["root_ids"] = sorted({m["form_id"] for m in matches}) or [p["forms"][0]["id"]]
        p["root_basis"] = "AMITSE GUID/form entry candidates" if matches else "First declared form; runtime driver registration not verified"


def routes(packages):
    by_guid = {}
    all_forms = {f["key"]: (p, f) for p in packages for f in p["forms"]}
    for p in packages:
        by_guid.setdefault(p["guid"], []).append(p)
    all_conditions = {k: v for p in packages for k, v in p["conditions"].items()}
    edges = {}
    for p in packages:
        for f in p["forms"]:
            f["incoming"] = []
    for p in packages:
        for f in p["forms"]:
            for item in f["items"]:
                if item["kind"] != "Ref":
                    continue
                target_guid = item["fields"].get("FormSetGuid", p["guid"])
                candidates = by_guid.get(target_guid, []) if target_guid != p["guid"] else [p]
                target_id = number(item["fields"].get("FormId"))
                targets = [tf for tp in candidates for tf in tp["forms"] if tf["id"] == target_id]
                item["targets"] = [tf["key"] for tf in targets]
                for tf in targets:
                    edge = {"from": f["key"], "to": tf["key"], "prompt": item["prompt"],
                            "conditions": item["conditions"], "offset": item["offset"]}
                    edges.setdefault(f["key"], []).append(edge)
                    tf["incoming"].append(edge)
    # Prefer a route without a statically true hide condition after unlock.
    heap, best = [], {}
    for p in packages:
        for f in p["forms"]:
            if f["id"] in p["root_ids"]:
                heapq.heappush(heap, (0, f["key"], (f["title"],), ()))
    while heap:
        cost, key, path, conditions = heapq.heappop(heap)
        if key in best:
            continue
        best[key] = (path, conditions)
        for edge in edges.get(key, []):
            tests = [all_conditions[c]["unlocked_result"] for c in edge["conditions"]
                     if all_conditions[c]["kind"] == "SuppressIf"]
            penalty = 10000 if any(x is not None and bool(x) for x in tests) else (10 if None in tests else 0)
            label = edge["prompt"] or all_forms[edge["to"]][1]["title"]
            heapq.heappush(heap, (cost + 1 + penalty, edge["to"], (*path, label),
                                  tuple(dict.fromkeys((*conditions, *edge["conditions"])))))
    for key, (p, f) in all_forms.items():
        path, inherited = best.get(key, ((p["title"], f["title"]), ()))
        f["path"] = list(path)
        f["route_conditions"] = list(inherited)
        f["route_found"] = key in best
        for item in f["items"]:
            condition_ids = list(dict.fromkeys((*inherited, *item["conditions"])))
            relevant = [all_conditions[c] for c in condition_ids]
            def state(kinds, scenario):
                vals = [c[scenario] for c in relevant if c["kind"] in kinds]
                if any(v is not None and bool(v) for v in vals):
                    return "yes"
                return "conditional" if None in vals else "no"
            item["access"] = {"vendor_condition": any(c["vendor_flag"] for c in relevant),
                "stock_hidden": state({"SuppressIf"}, "stock_result"),
                "unlocked_hidden": state({"SuppressIf"}, "unlocked_result"),
                "stock_disabled": state({"GrayOutIf", "DisableIf"}, "stock_result"),
                "unlocked_disabled": state({"GrayOutIf", "DisableIf"}, "unlocked_result"),
                "condition_ids": condition_ids}
    return all_forms, all_conditions


def md(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("|", "&#124;").replace("`", "'").replace("[", "&#91;").replace("]", "&#93;")


def form_filename(key):
    return f"forms/{key}.md"


def access_label(item):
    a = item["access"]
    if a["unlocked_hidden"] == "yes":
        label = "Hidden even with CMOS unlock on this path"
    elif a["vendor_condition"]:
        label = "CMOS vendor gate; other conditions may apply"
    elif a["unlocked_hidden"] == "conditional":
        label = "Conditional; no CMOS vendor gate on this path"
    else:
        label = "No active IFR hide condition on this path"
    if a["unlocked_disabled"] != "no":
        label += f"; disabled after unlock: {a['unlocked_disabled']}"
    if number(item["fields"].get("QuestionFlags"), 0) & 1:
        label += "; read-only flag"
    return label


def meaningful(item):
    if item["kind"] in CONTROLS:
        return True
    return bool(re.sub(r"[\s\-_=]", "", item["prompt"] + item["fields"].get("Text", "")))


def render(packages, sources, output, image_hash):
    output.mkdir(parents=True, exist_ok=True)
    (output / "forms").mkdir(exist_ok=True)
    all_forms, all_conditions = routes(packages)
    rendered = 0
    for p in packages:
        for f in p["forms"]:
            lines = [f"# {md(f['title']) or '(untitled form)'}", "",
                     f"[Menu index](../README.md) | [Module index](../{p['id']}.md)", "",
                     f"Path: **{md(' > '.join(f['path']))}**", "",
                     f"Source: `{p['source']['module']}`. Formset `{p['guid']}`, form `0x{f['id']:X}`, PE/section offset `0x{f['offset']:X}`.", "",
                     f"Root evidence: {p['root_basis']}.", "",
                     "Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.", ""]
            if not f["route_found"]:
                lines += ["No reference path from a candidate root was found. This may be an internal or runtime-linked form.", ""]
            if not p["source"]["strings_resolved"]:
                lines += ["**String package unavailable. Labels are unresolved string IDs, not descriptions of the controls.**", ""]
            if f["incoming"]:
                lines += ["## Incoming references", ""]
                for edge in f["incoming"]:
                    parent = all_forms[edge["from"]][1]
                    lines += [f"- [{md(parent['title'])}]({Path(form_filename(parent['key'])).name}) via {md(edge['prompt']) or '(blank reference)'}, offset `0x{edge['offset']:X}`."]
                lines += [""]
            lines += ["## Controls and information", ""]
            for item in f["items"]:
                if not meaningful(item):
                    continue
                rendered += 1
                prompt = item["prompt"] or f"(internal {item['kind']}, Q0x{item['question_id']:X})"
                lines += [f"### {md(prompt)}", "", f"Type: `{item['kind']}`. Offset: `0x{item['offset']:X}`.", ""]
                help_text = item["help"]
                if help_text:
                    lines += [f"Firmware help: {md(help_text)}", ""]
                elif item["kind"] == "Text":
                    lines += ["Firmware provides this information field without explanatory help.", ""]
                else:
                    lines += ["No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.", ""]
                if item["fields"].get("Text"):
                    lines += [f"Static display text: {md(item['fields']['Text'])}. Runtime callbacks may replace this text.", ""]
                if item["kind"] == "Ref":
                    if item.get("targets"):
                        lines += ["Opens: " + ", ".join(f"[{md(all_forms[k][1]['title'])}]({Path(form_filename(k)).name})" for k in item["targets"]) + ".", ""]
                    else:
                        lines += ["Target is not resolved in the extracted forms; it may be supplied at runtime.", ""]
                lines += [f"Access: {access_label(item)}.", ""]
                if item["options"]:
                    lines += ["| Choice | Value | Static default flags | Additional conditions |", "| --- | --- | --- | --- |"]
                    for option in item["options"]:
                        flags = ", ".join(x for x, active in (("standard", option["default"]), ("manufacturing", option["manufacturing_default"])) if active)
                        extra_ids = [cid for cid in option["conditions"] if cid not in item["conditions"]]
                        extra = "; ".join(f"{all_conditions[cid]['kind']}: {all_conditions[cid]['description']}" for cid in extra_ids)
                        lines += [f"| {md(option['label'])} | {md(option['value'])} | {flags or 'none'} | {md(extra) or 'none'} |"]
                    lines += [""]
                if item["defaults"]:
                    def default_label(d):
                        value = json.dumps(d["value"], ensure_ascii=False) if d["type"] == "string" else str(d["value"])
                        return f"store {md(d['store'])}: {md(value)}"
                    lines += ["Explicit static defaults: " + "; ".join(default_label(d) for d in item["defaults"]) + ".", ""]
                details = [f"{k}: {v}" for k, v in item["fields"].items()
                           if k in {"Min", "Max", "Step", "Size", "MinSize", "MaxSize", "Default", "MfgDefault"}]
                if details:
                    lines += [md("; ".join(details)) + ".", ""]
                if "value_expression" in item:
                    lines += ["Computed value expression: " + md(describe_expression(item["value_expression"], p["questions"])) + ".", ""]
                if item["question_id"] is not None:
                    flags = number(item["fields"].get("QuestionFlags"), 0)
                    decoded = [name for bit, name in ((1, "read-only"), (4, "callback"), (0x10, "reset required"),
                               (0x20, "REST style"), (0x40, "reconnect required"), (0x80, "options only")) if flags & bit]
                    lines += [f"Question ID: `0x{item['question_id']:X}`. Question flags: `0x{flags:X}` ({', '.join(decoded) or 'none of the decoded flags'}).", ""]
                if item["storage"]:
                    storage = item["storage"]
                    suffix = f" at byte offset `0x{storage['offset']:X}`" if storage["offset"] is not None else " (no fixed byte offset in this record)"
                    lines += [f"Storage: `{storage['name']}`{suffix}, GUID `{storage['guid']}`. This is a variable offset, not a CMOS address.", ""]
                if item["access"]["condition_ids"]:
                    lines += ["Conditions on this path and item:", ""]
                    for cid in item["access"]["condition_ids"]:
                        c = all_conditions[cid]
                        a = "runtime-dependent" if c["stock_result"] is None else str(bool(c["stock_result"])).lower()
                        b = "runtime-dependent" if c["unlocked_result"] is None else str(bool(c["unlocked_result"])).lower()
                        lines += [f"- `{c['kind']}` at `0x{c['offset']:X}`: {md(c['description'])}. Expression result: stock {a}; CMOS unlock {b}."]
                    lines += [""]
            if f["dynamic_labels"]:
                lines += ["## Runtime insertion labels", "", "The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.", ""]
                lines += [f"- {md(label)}" for label in f["dynamic_labels"]] + [""]
            (output / form_filename(f["key"])).write_text("\n".join(lines))
        module_lines = [f"# {md(p['title'])}: {md(p['source']['module'])}", "", "[Menu index](README.md)", "",
                        f"Formset: `{p['guid']}`. Package ID: `{p['id']}`.", "", f"Firmware help: {md(p['help']) or '(none)' }", "",
                        "| Form | Static path | Controls |", "| --- | --- | --- |"]
        for f in p["forms"]:
            controls = sum(i["kind"] in CONTROLS for i in f["items"])
            module_lines += [f"| [{md(f['title']) or '(untitled)'}]({form_filename(f['key'])}) | {md(' > '.join(f['path']))} | {controls} |"]
        (output / f"{p['id']}.md").write_text("\n".join(module_lines) + "\n")
    controls = [i for p in packages for f in p["forms"] for i in f["items"] if i["kind"] in CONTROLS]
    summary = {"sources": len(sources), "form_packages": len(packages), "forms": len(all_forms),
               "controls_including_references_and_internal_questions": len(controls),
               "question_records_excluding_navigation": sum(i["kind"] != "Ref" for i in controls),
               "navigation_references": sum(i["kind"] == "Ref" for i in controls),
               "controls_with_blank_prompts": sum(not i["prompt"] for i in controls),
               "rendered_controls_and_information": rendered,
               "vendor_condition_on_selected_path": sum(i["access"]["vendor_condition"] for i in controls),
               "controls_without_help": sum(not i["help"] for i in controls),
               "conditions": len(all_conditions),
               "unparsed_condition_expressions": sum(c["expression"]["op"] == "unparsed" for c in all_conditions.values())}
    serializable = []
    for p in packages:
        serializable.append({k: v for k, v in p.items() if k not in {"questions"}})
    payload = {"firmware": "Inspur Thor02 3.0.29", "image_sha256": image_hash,
               "summary": summary, "sources": sources, "packages": serializable}
    (output / "catalog.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    # A compact index stays useful in editors and spreadsheet applications.
    import csv
    with (output / "settings.tsv").open("w", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(["module", "path", "setting", "type", "firmware_help", "choices",
                         "vendor_gate", "hidden_stock", "hidden_unlocked", "disabled_unlocked", "storage", "page"])
        for p in packages:
            for form in p["forms"]:
                for item in form["items"]:
                    if item["kind"] not in CONTROLS:
                        continue
                    storage = item["storage"] or {}
                    writer.writerow([p["source"]["module"], " > ".join(form["path"]), item["prompt"], item["kind"],
                        item["help"], "; ".join(f"{o['label']}={o['value']}" for o in item["options"]),
                        item["access"]["vendor_condition"], item["access"]["stock_hidden"], item["access"]["unlocked_hidden"],
                        item["access"]["unlocked_disabled"], str(storage), form_filename(form["key"])])
    lines = ["# BIOS 3.0.29 menu map", "",
             "This is a static catalogue of the setup forms found in the researched Thor02 BIOS. Each form page lists its controls, firmware help, choices, static defaults, storage and visibility conditions. It includes internal questions and option ROM forms as well as the main BIOS menus.", "",
             "[Unlock research](../README.md) | [Guide to the main areas](../menu-guide.md) | [Risks and recovery](../risks.md) | [Compact setting index](settings.tsv) | [Machine-readable catalogue](catalog.json)", "",
             "## Coverage", "", "| Item | Count |", "| --- | --- |"]
    lines += [f"| {key.replace('_', ' ')} | {value} |" for key, value in summary.items()]
    lines += ["", "## Menus and drivers", "", "| Area | Source | Forms |", "| --- | --- | --- |"]
    for p in packages:
        suffix = " (unresolved labels)" if not p["source"]["strings_resolved"] else ""
        lines += [f"| [{md(p['title'])}{suffix}]({p['id']}.md) | `{p['source']['module']}` | {len(p['forms'])} |"]
    lines += ["", "## Reading the map", "",
              "- Firmware help explains the vendor's intended behavior. When help is missing or just repeats a label, the map does not invent a description.",
              "- Static defaults are compiled into the form. They are not a readout of current settings, and callbacks or external default stores may override them.",
              "- CMOS vendor gate means a condition refers to byte 1 of one of the four restriction variables controlled by CMOS 0x54. It does not mean the setting will definitely appear or work after unlock.",
              "- SuppressIf hides an item when its expression is true. GrayOutIf and DisableIf restrict interaction. Other condition types can validate or reject changes.",
              "- Expression results only substitute the vendor flag: 1 for stock and 0 for unlock. Other question values remain unknown. No live hardware state or current configuration is assumed.",
              "- Conditions include the selected reference path. Incoming references let you check alternate routes. The selected path prefers routes without a known active suppression after unlock.",
              "- AMITSE GUID/form pairs are root candidates, not proof that a particular menu table is selected at runtime. Driver roots and option ROM pages depend on registration and installed devices.",
              "- AMITSESetupData access-level policy is not decoded here. IFR conditions and question flags describe only part of the setup engine's access decisions.",
              "- Blank spacer subtitles are omitted from the prose pages. Internal questions, blank references and named information fields remain in the JSON.",
              "- Runtime insertion labels mark places where drivers can add device-specific pages. Those generated controls cannot be recovered completely from static IFR.",
              "- Some bundled driver images contain multiple forms and English string tables. The generator chooses a table with sufficient IDs nearest the form package and records that choice in JSON.",
              "- The Intel DIMM Gen 1 driver's original language tag is 'en'. IFRExtractor overlooks that short header. A temporary copy uses 'en-US' with the same string blocks; JSON records the original location and adaptation. No labels are guessed.",
              "- If no English strings can be recovered, explicit unresolved IDs are used. There are no unresolved string-package components in this build.",
              "- Text line breaks and dash typography are normalized. All offsets are in the extracted source body, unless explicitly described as variable or AMITSE offsets.",
              "- This map has not been checked against a rebooted unlocked server. Consult the risk notes before changing controls.", "",
              "## Searching", "", "Each module index links to its form pages. Search the complete local catalogue with:", "", "```bash",
              "python3 bios/query_menu.py 'CSM Support'",
              "python3 bios/query_menu.py 'voltage' --module Platform",
              "python3 bios/query_menu.py --needs-unlock --limit 50",
              "```", "", "The TSV file can also be opened in a spreadsheet. The JSON contains all conditions, incoming references, source hashes and extraction choices.", "",
              "## Regenerating", "", "Run UEFIExtract A76 against a copy of the original image, then use IFRExtractor-RS 1.6.1:", "", "```bash",
              "/path/to/uefiextract /path/to/original.bin all",
              "python3 bios/build_menu_map.py --image /path/to/original.bin \\",
              "  --dump /path/to/original.bin.dump --ifrextractor /path/to/ifrextractor \\",
              "  --output bios/menu-map", "```", "",
              "The generator uses only Python's standard library and the external extractor. It reads the dump, uses temporary files for extraction and writes documentation. It does not access server hardware.", "",
              "Encoding and condition semantics: [EDK II IFR definitions](https://github.com/tianocore/edk2/blob/master/MdePkg/Include/Uefi/UefiInternalFormRepresentation.h). Firmware extraction: [UEFITool](https://github.com/LongSoft/UEFITool) and [IFRExtractor-RS](https://github.com/LongSoft/IFRExtractor-RS).", ""]
    (output / "README.md").write_text("\n".join(lines))
    print(json.dumps(summary, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True)
    parser.add_argument("--dump", type=Path, required=True)
    parser.add_argument("--ifrextractor", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    digest = hashlib.sha256(args.image.read_bytes()).hexdigest()
    if digest != IMAGE_SHA256:
        parser.error("Image differs from the researched 3.0.29 dump.")
    sources = extract_sources(args.dump.resolve(), str(Path(args.ifrextractor).resolve()))
    packages = build_packages(sources)
    amitse = next(p for p in args.dump.rglob("body.bin") if p.parent.name.endswith("PE32 image section")
                  and any(parent.name.endswith(" AMITSE") for parent in p.parents)).read_bytes()
    menu_roots(packages, amitse)
    render(packages, sources, args.output, digest)


if __name__ == "__main__":
    main()
