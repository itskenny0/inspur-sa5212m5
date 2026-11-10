"""Exercise byte writes and rollback using a temporary file, without hardware."""

import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest

import cmos_menu


class CmosMenuTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.device = self.root / "nvram"
        self.initial = bytes([0xFF] * 114)
        self.device.write_bytes(self.initial)
        self.fd = os.open(self.device, os.O_RDWR)
        self.addCleanup(os.close, self.fd)
        self.backup = self.root / "original.json"

    def operate(self, action):
        with contextlib.redirect_stdout(io.StringIO()):
            cmos_menu.operate(self.fd, action, self.backup)

    def test_status_does_not_write_or_create_backup(self):
        self.operate("status")
        self.assertEqual(self.device.read_bytes(), self.initial)
        self.assertFalse(self.backup.exists())

    def test_unlock_changes_only_target_byte_and_restore_is_exact(self):
        self.operate("unlock")
        expected = bytearray(self.initial)
        expected[0x46] = 0x35
        self.assertEqual(self.device.read_bytes(), expected)
        self.assertEqual(json.loads(self.backup.read_text())["original_value"], 0xFF)
        self.assertEqual(self.backup.stat().st_mode & 0o777, 0o600)
        self.operate("restore")
        self.assertEqual(self.device.read_bytes(), self.initial)

    def test_existing_backup_prevents_write(self):
        self.backup.write_text("keep this")
        with self.assertRaises(FileExistsError):
            self.operate("unlock")
        self.assertEqual(self.device.read_bytes(), self.initial)
        self.assertEqual(self.backup.read_text(), "keep this")

    def test_unexpected_current_value_prevents_unlock(self):
        os.pwrite(self.fd, b"\x12", 0x46)
        with self.assertRaises(ValueError):
            self.operate("unlock")
        self.assertEqual(os.pread(self.fd, 1, 0x46), b"\x12")
        self.assertFalse(self.backup.exists())

    def test_wrong_backup_prevents_restore(self):
        self.operate("unlock")
        data = json.loads(self.backup.read_text())
        data["bios"] = "4.1.29"
        self.backup.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            self.operate("restore")
        self.assertEqual(os.pread(self.fd, 1, 0x46), b"\x35")

    def test_repeated_unlock_preserves_original_backup(self):
        self.operate("unlock")
        backup = self.backup.read_bytes()
        with self.assertRaises(ValueError):
            self.operate("unlock")
        self.assertEqual(self.backup.read_bytes(), backup)


if __name__ == "__main__":
    unittest.main()
