"""Check scope, expression, string recovery and navigation handling offline."""

import struct
import unittest

import build_menu_map as menu


def node(kind, fields=None, children=None, raw=""):
    return {"kind": kind, "fields": fields or {}, "children": children or [], "raw": raw, "detail": kind}


class MenuMapTests(unittest.TestCase):
    def test_fields_preserve_help_and_parse_defaults_without_commas(self):
        values = menu.fields('Prompt: "CSM Support", Help: "Choose a value, Min: is explained here.", QuestionFlags: 0x14')
        self.assertEqual(values["Help"], "Choose a value, Min: is explained here.")
        self.assertEqual(values["QuestionFlags"], "0x14")
        self.assertEqual(menu.fields('Option: "Disabled" Value: 0, Default')["Option"], "Disabled")
        self.assertEqual(menu.fields('DefaultId: 0x0 Value: 1'), {"DefaultId": "0x0", "Value": "1"})

    def test_multiline_help_and_nested_scopes(self):
        text = '''0x100: Form FormId: 0x1, Title: "Test" { 01 86 01 00 01 00 }
0x106: SuppressIf { 0A 82 }
0x108: True { 46 02 }
0x10A: Text Prompt: "Example", Help: "First line
second line", Text: "Info" { 03 08 01 00 02 00 03 00 }
0x112: End { 29 02 }
0x114: End { 29 02 }
'''
        roots, count = menu.parse_ifr(text)
        self.assertEqual(count, 6)
        child = roots[0]["children"][0]["children"][1]
        self.assertEqual(child["fields"]["Help"], "First line second line")
        with self.assertRaises(ValueError):
            menu.parse_ifr(text.rsplit("0x114:", 1)[0])

    def test_vendor_or_unknown_condition_stays_unknown_after_unlock(self):
        nodes = [node("EqIdVal", {"QuestionId": "0x1", "Value": "0x1"},
                      [node("EqIdVal", {"QuestionId": "0x2", "Value": "0x1"}), node("Or")])]
        expr = menu.expression(nodes)
        questions = {1: {"storage": {"name": "InspurGenSetupFeature", "offset": 1}}}
        self.assertTrue(menu.evaluate(expr, questions, 1))
        self.assertIsNone(menu.evaluate(expr, questions, 0))

    def test_unknown_and_false_is_false(self):
        expr = {"op": "and", "args": [{"op": "question", "id": 9}, {"op": "constant", "value": 0}]}
        self.assertFalse(menu.evaluate(expr, {}, 0))

    def test_recovered_language_keeps_string_blocks(self):
        blocks = b"\x14" + "Example".encode("utf-16le") + b"\0\0\0"
        header = bytearray(49)
        struct.pack_into("<III", header, 0, (49 + len(blocks)) | (4 << 24), 49, 49)
        header[46:49] = b"en\0"
        adapted, metadata = menu.recover_short_english(bytes(header) + blocks)
        self.assertEqual(adapted[52:], blocks)
        self.assertEqual(adapted[46:52], b"en-US\0")
        self.assertEqual(metadata["original_offset"], 0)

    def test_route_avoids_permanent_suppression_and_inherits_vendor_gate(self):
        a = {"key": "a", "id": 1, "title": "Root", "conditions": [], "items": []}
        b = {"key": "b", "id": 2, "title": "Page", "conditions": [], "items": []}
        base = {"kind": "Ref", "conditions": [], "offset": 0, "fields": {"FormId": "0x2"}}
        a["items"] = [{**base, "prompt": "Blocked", "conditions": ["always"]},
                      {**base, "prompt": "Available after unlock", "conditions": ["vendor"]}]
        control = {"kind": "Numeric", "fields": {}, "conditions": []}
        b["items"] = [control]
        conditions = {
            "always": {"kind": "SuppressIf", "stock_result": 1, "unlocked_result": 1, "vendor_flag": False},
            "vendor": {"kind": "SuppressIf", "stock_result": 1, "unlocked_result": 0, "vendor_flag": True},
        }
        package = {"guid": "guid", "forms": [a, b], "root_ids": [1], "title": "Root", "conditions": conditions}
        menu.routes([package])
        self.assertEqual(b["path"], ["Root", "Available after unlock"])
        self.assertEqual(control["access"]["stock_hidden"], "yes")
        self.assertEqual(control["access"]["unlocked_hidden"], "no")


if __name__ == "__main__":
    unittest.main()
