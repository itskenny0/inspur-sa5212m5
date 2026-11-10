#!/usr/bin/env python3
"""Search the generated BIOS catalogue without accessing hardware."""

import argparse
import json
from pathlib import Path


def search(catalog, term="", module="", needs_unlock=False):
    for package in catalog["packages"]:
        if module.casefold() not in (package["source"]["module"] + " " + package["title"]).casefold():
            continue
        for form in package["forms"]:
            for item in form["items"]:
                if item["kind"] in {"Subtitle", "Text"}:
                    continue
                text = " ".join([item["prompt"], item["help"], *form["path"]]).casefold()
                if term.casefold() not in text or (needs_unlock and not item["access"]["vendor_condition"]):
                    continue
                yield {"module": package["source"]["module"], "path": form["path"], "item": item,
                       "page": f"forms/{form['key']}.md"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("term", nargs="?", default="")
    parser.add_argument("--module", default="")
    parser.add_argument("--needs-unlock", action="store_true",
                        help="Only records whose selected path contains a CMOS vendor condition.")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--catalog", type=Path, default=Path(__file__).parent / "menu-map/catalog.json")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    catalog = json.loads(args.catalog.read_text())
    matches = list(search(catalog, args.term, args.module, args.needs_unlock))
    if args.json:
        print(json.dumps(matches[:args.limit], indent=2))
        return
    print(f"{len(matches)} matching records; showing {min(len(matches), args.limit)}. Static firmware data only.")
    for match in matches[:args.limit]:
        item = match["item"]
        print(f"\n{match['module']}: {' > '.join(match['path'])} > {item['prompt'] or '(internal question)'}")
        print(f"  Help: {item['help'] or '(no explanatory firmware help)'}")
        print(f"  Type: {item['kind']}; vendor condition: {item['access']['vendor_condition']}")
        print(f"  Hidden on selected path: stock={item['access']['stock_hidden']}, unlock={item['access']['unlocked_hidden']}")
        if item["options"]:
            print("  Choices: " + "; ".join(f"{o['label']}={o['value']}" for o in item["options"]))
        print(f"  Page: {args.catalog.parent / match['page']}")


if __name__ == "__main__":
    main()
