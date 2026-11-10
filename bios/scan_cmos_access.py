#!/usr/bin/env python3
"""Look for one direct CMOS access pattern in extracted x86 PE code."""

import argparse
import json
from pathlib import Path

import capstone
import pefile


def scan(root):
    hits, examined = [], 0
    for body in sorted(root.rglob("body.bin")):
        if not body.parent.name.endswith("PE32 image section"):
            continue
        try:
            pe = pefile.PE(data=body.read_bytes(), fast_load=True)
        except pefile.PEFormatError:
            continue
        if pe.FILE_HEADER.Machine not in (0x8664, 0x14C):
            continue
        examined += 1
        mode = capstone.CS_MODE_64 if pe.FILE_HEADER.Machine == 0x8664 else capstone.CS_MODE_32
        decoder = capstone.Cs(capstone.CS_ARCH_X86, mode)
        decoder.skipdata = True
        for section in pe.sections:
            raw = section.get_data()
            if not section.Characteristics & 0x20000000 or b"\xb0\x54" not in raw:
                continue
            instructions = list(decoder.disasm(raw, section.VirtualAddress))
            for index, insn in enumerate(instructions):
                if insn.mnemonic != "mov" or insn.op_str != "al, 0x54":
                    continue
                if not any(i.mnemonic == "out" for i in instructions[index:index + 12]):
                    continue
                window = instructions[max(0, index - 3):index + 15]
                hits.append({"source": str(body.relative_to(root)), "address": insn.address,
                             "instructions": [f"{i.address:X} {i.mnemonic} {i.op_str}" for i in window]})
    return {"pe_images_examined": examined,
            "scope": "Literal mov al,0x54 near out instructions in x86 PE code. Indirect, table-driven, other encodings and TE code not covered.",
            "hits": hits}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dump", type=Path)
    args = parser.parse_args()
    print(json.dumps(scan(args.dump), indent=2))
