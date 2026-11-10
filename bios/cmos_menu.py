#!/usr/bin/env python3
"""Read or change the menu unlock byte on the researched Thor02 BIOS."""

import argparse
import json
import os
from pathlib import Path
import platform
import stat

BOARD = "YZMB-00824-103"
BIOS = "3.0.29"
CMOS_ADDRESS = 0x54
DEVICE_OFFSET = CMOS_ADDRESS - 0x0E
UNLOCK = 0x35


def check_machine():
    if platform.system() != "Linux" or platform.machine() not in ("x86_64", "i386", "i686"):
        raise ValueError("This script requires Linux on x86.")
    for field, expected in (("board_name", BOARD), ("bios_version", BIOS)):
        actual = Path("/sys/class/dmi/id", field).read_text().strip()
        if actual != expected:
            raise ValueError(f"Unsupported {field}: {actual!r}; expected {expected!r}.")


def read_byte(fd):
    data = os.pread(fd, 1, DEVICE_OFFSET)
    if len(data) != 1:
        raise OSError("Could not read the CMOS byte.")
    return data[0]


def write_byte(fd, value):
    if os.pwrite(fd, bytes([value]), DEVICE_OFFSET) != 1:
        raise OSError("Short write to /dev/nvram.")
    if read_byte(fd) != value:
        raise OSError("CMOS readback did not match. Do not reboot before checking it.")


def save_backup(path, value):
    data = {"format": 1, "board": BOARD, "bios": BIOS,
            "cmos_address": CMOS_ADDRESS, "original_value": value}
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())


def load_backup(path):
    data = json.loads(Path(path).read_text())
    expected = {"format": 1, "board": BOARD, "bios": BIOS, "cmos_address": CMOS_ADDRESS}
    if not isinstance(data, dict) or any(data.get(key) != value for key, value in expected.items()):
        raise ValueError("Backup does not match this board, BIOS and CMOS address.")
    value = data.get("original_value")
    if type(value) is not int or not 0 <= value <= 255:
        raise ValueError("Backup contains an invalid original value.")
    return value


def operate(fd, action, backup=None):
    current = read_byte(fd)
    print(f"CMOS 0x{CMOS_ADDRESS:02X}: 0x{current:02X}")
    if action == "status":
        print("Unlock selected." if current == UNLOCK else "Unlock not selected.")
        return
    if action == "unlock":
        if current == UNLOCK:
            raise ValueError("Already unlocked; the original value cannot be inferred.")
        if current != 0xFF:
            raise ValueError("Expected the observed stock value 0xFF. Investigate before writing.")
        save_backup(backup, current)
        target = UNLOCK
    else:
        target = load_backup(backup)
        if current != UNLOCK:
            raise ValueError("Current byte is not 0x35; refusing to overwrite an unexpected value.")
    write_byte(fd, target)
    print(f"Verified CMOS 0x{CMOS_ADDRESS:02X} = 0x{target:02X}.")
    print("Reboot manually when ready. No reboot was requested by this script.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action")
    sub.add_parser("status", help="Read the byte without changing it (default).")
    for action in ("unlock", "restore"):
        command = sub.add_parser(action)
        command.add_argument("--backup", type=Path, required=True,
                             help="Local JSON file holding this server's original byte.")
    args = parser.parse_args()
    action = args.action or "status"
    try:
        check_machine()
        flags = (os.O_RDONLY if action == "status" else os.O_RDWR) | os.O_EXCL
        fd = os.open("/dev/nvram", flags)
        try:
            device = os.fstat(fd)
            if not stat.S_ISCHR(device.st_mode) or device.st_rdev != os.makedev(10, 144):
                raise ValueError("/dev/nvram is not the expected Linux NVRAM character device.")
            operate(fd, action, getattr(args, "backup", None))
        finally:
            os.close(fd)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
