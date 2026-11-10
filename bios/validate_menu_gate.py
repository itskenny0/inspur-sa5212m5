#!/usr/bin/env python3
"""Emulate the known 3.0.29 menu gate without accessing real hardware."""
import argparse
from pathlib import Path
import hashlib
import json
import struct
import uuid
from unicorn import Uc, UC_ARCH_X86, UC_MODE_64, UC_HOOK_INSN, UC_HOOK_CODE
from unicorn.x86_const import (
    UC_X86_INS_IN, UC_X86_INS_OUT, UC_X86_REG_RSP, UC_X86_REG_RDI,
    UC_X86_REG_RCX, UC_X86_REG_RDX, UC_X86_REG_R8, UC_X86_REG_R9,
    UC_X86_REG_RAX, UC_X86_REG_RIP,
)


DRIVER_SHA256 = '9a1b82b4738d6086bb9ae622001bc52529c407a093afef0bf7937fd0c8f779bb'
VARIABLES = {
    'InspurPchSetupFeatures': 'd19a26a3-17f1-48c3-8a1e-11eb0a7f6e4e',
    'InspurSocketSetupFeatures': '07013588-c789-4e12-a7c3-88fafae79f7c',
    'InspurGenSetupFeature': 'ec87d643-eba4-4bb5-a1e5-3f3e36b20da9',
    'InspurMgmtSetupFeature': '01239999-fc0e-4b6e-9e79-d54d5db6cd20',
}


def run(image, value):
    assert image[0x529:0x530] == bytes.fromhex('ba70000000b054')
    assert image[0x561:0x569] == bytes.fromhex('0f95842441020000')
    uc = Uc(UC_ARCH_X86, UC_MODE_64)
    uc.mem_map(0, 0x10000)
    uc.mem_write(0, image)
    uc.mem_map(0x100000, 0x10000)
    uc.mem_map(0x200000, 0x1000)
    uc.mem_map(0x300000, 0x1000)
    uc.mem_write(0x1c18, struct.pack('<Q', 0x200000))
    uc.mem_write(0x200058, struct.pack('<Q', 0x300000))
    uc.mem_write(0x300000, b'\xc3')
    uc.reg_write(UC_X86_REG_RSP, 0x108000)
    uc.reg_write(UC_X86_REG_RDI, 2)
    # GUID initialized by the preceding instructions at 0x43d..0x4a5.
    uc.mem_write(0x108030, uuid.UUID('ec87d643-eba4-4bb5-a1e5-3f3e36b20da9').bytes_le)
    # First byte is outside this block's scope; only the second is validated.
    uc.mem_write(0x108240, b'\xa5\x99')
    selected = []
    calls = []

    def out_port(uc, port, size, data, _):
        assert port == 0x70 and size == 1 and data == 0x54
        selected.append(data)

    def in_port(uc, port, size, _):
        assert port == 0x71 and size == 1 and selected == [0x54]
        return value

    def callback(uc, address, size, _):
        if address != 0x300000:
            return
        p = uc.reg_read(UC_X86_REG_RCX)
        raw = bytearray()
        while True:
            pair = bytes(uc.mem_read(p, 2))
            if pair == b'\0\0':
                break
            raw.extend(pair)
            p += 2
        guid = uuid.UUID(bytes_le=bytes(uc.mem_read(uc.reg_read(UC_X86_REG_RDX), 16)))
        attrs = uc.reg_read(UC_X86_REG_R8)
        length = uc.reg_read(UC_X86_REG_R9)
        buf, = struct.unpack('<Q', uc.mem_read(uc.reg_read(UC_X86_REG_RSP) + 0x28, 8))
        payload = bytes(uc.mem_read(buf, length))
        calls.append({'name': raw.decode('utf-16le'), 'guid': str(guid),
                      'attributes': attrs, 'data': payload.hex()})
        uc.reg_write(UC_X86_REG_RAX, 0)

    uc.hook_add(UC_HOOK_INSN, out_port, None, 1, 0, UC_X86_INS_OUT)
    uc.hook_add(UC_HOOK_INSN, in_port, None, 1, 0, UC_X86_INS_IN)
    uc.hook_add(UC_HOOK_CODE, callback)
    uc.emu_start(0x529, 0x5eb, count=200)
    assert uc.reg_read(UC_X86_REG_RIP) == 0x5eb
    assert len(calls) == 4
    assert {c['name']: c['guid'] for c in calls} == VARIABLES
    assert all(c['attributes'] == 2 and c['data'] == ('a500' if value == 0x35 else 'a501')
               for c in calls)
    return calls


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('driver', type=Path, help='Extracted CBB_Dxe PE32 body, without section header.')
    args = parser.parse_args()
    if not __debug__:
        parser.error('Run without -O so that validation assertions remain enabled.')
    image = args.driver.read_bytes()
    if hashlib.sha256(image).hexdigest() != DRIVER_SHA256:
        parser.error('Driver hash differs from the researched 3.0.29 image.')
    results = {value: run(image, value) for value in range(256)}
    print(json.dumps({'checked_cmos_values': 256,
                      'scope': 'Only the second payload byte is validated; a5 is a first-byte marker.',
                      'restricted_0xff': results[0xff],
                      'unrestricted_0x35': results[0x35]}, indent=2))
