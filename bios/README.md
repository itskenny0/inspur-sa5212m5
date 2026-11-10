# Hidden BIOS menus

The Alibaba BIOS contains a CMOS switch for showing settings that are normally hidden. In the researched **3.0.29** firmware, CMOS byte **0x54** selects the menu restrictions:

| CMOS 0x54 | Result in the firmware code |
| --- | --- |
| `0x35` | Clear the second byte of all four setup restriction variables |
| Any other value | Set that byte to `1` |

The running server had `0xFF`. No firmware patch or ME access is needed to select this switch.

The [full menu map](menu-map/README.md) lists the static forms, setting help, choices, defaults and access conditions. Read [the risks and recovery notes](risks.md) before testing the switch or changing newly exposed controls.

## Status and scope

The code has been disassembled and the relevant block has been emulated for all 256 possible byte values. A read-only check of the running server confirmed its board ID, BIOS version and current CMOS value. **The unlock has not been written or tested across a real reboot.** The first hardware test is planned for a spare server before trying it on production hardware.

The dump came from this system:

| Field | Value |
| --- | --- |
| System | Inspur AliServer Thor02-2U |
| Board | YZMB-00824-103 |
| DMI board version | SA5212H5 |
| BIOS | Inspur 3.0.29, dated 2018-08-15 |
| Full image size | 32 MiB |
| BIOS region | `0x01000000` through `0x01FFFFFF`, 16 MiB |
| Image SHA-256 | `927b893e0f5ae8c47702be9251307087f8f3523cc8e6e488437b787eca9d12ee` |

This finding has not been checked against the 4.1.29 BIOS archive elsewhere in this repo, other board revisions, or the Inventec and Foxconn variants. The write script requires the board ID and BIOS version above. Check these on the spare server first, even if the chassis and product name match.

## Which settings should become visible?

The general setup forms hide these entries when `InspurGenSetupFeature[1]` is `1`:

- ACPI Settings
- Super IO Configuration
- Serial Port Console Redirection, including Legacy Console Redirection Settings
- Network Stack Configuration
- CSM Configuration, including CSM Support and Option ROM Messages
- Ali Config and X-Dragon
- Setup Prompt Timeout

The socket setup forms use `InspurSocketSetupFeatures[1]` for a much larger set of restrictions. Examples include:

| Area | Examples behind the vendor restriction |
| --- | --- |
| CPU | Active Cores, MSR Lock Control, PPIN Control, additional processor controls |
| Interconnect and PCIe | UPI Configuration, IIO Configuration, IOAT Configuration, IIO General Configuration, port controls, some IOU lane configuration choices |
| Memory | Memory Training, Memory Timings Override, Memory Map, Memory RAS Configuration, Page Policy |
| Power | CPU C State Control, Package C State Control, CPU Thermal Management, CPU - Advanced PM Tuning, SOCKET RAPL Config |
| Memory power | Memory Power & Thermal Configuration |

The code also clears the PCH and management setup restriction variables. Their settings and conditions are included in the full menu map under Chipset and Server Mgmt.

These are menu visibility changes inferred from the firmware forms. Other conditions still apply, including hardware presence, administrator access and Secure Boot state. The CSM page also contains boot-mode-dependent conditions. Exposing CSM Support does not itself disable CSM. The forms include an Overclocking page, but that does not establish that the installed processors support its controls.

This switch does not remove every suppression. The Chipset reference inside Setup has an unconditional `SuppressIf True`, independent of these variables. However, AMITSE also contains a separate root entry pointing to Platform's Chipset form, alongside Processor, FPGA Configuration and Server Mgmt. The hidden Setup reference therefore does not establish that the whole Chipset area stays inaccessible. Which AMITSE menu table is selected still needs checking on hardware.

## Reading and changing the byte

Run these commands on the server itself. The script uses Python's standard library and Linux `/dev/nvram`. It defaults to reading the byte and never reboots the machine.

```bash
sudo python3 bios/cmos_menu.py status
```

Linux exposes CMOS addresses `0x0E` onward through `/dev/nvram`, so CMOS `0x54` is at device offset **0x46**, or 70 decimal. The kernel driver handles the RTC lock and its standard CMOS checksum. If the device is missing or reports a checksum error, stop and investigate. The script does not load modules, repair checksums or fall back to raw port I/O.

To select the unlock on the spare server:

```bash
mkdir -p bios/backups
sudo python3 bios/cmos_menu.py unlock --backup bios/backups/spare-original.json
```

This saves the original byte before writing `0x35`, then reads it back. It refuses to overwrite an existing backup, an already selected unlock, or a current value other than the observed stock `0xFF`. Keep the backup for that specific server. The script does not write BIOS flash or other setup variables. The kernel's NVRAM driver also maintains its standard checksum, as explained in the risk notes.

Reboot manually when ready and enter BIOS Setup. For the first test, check the menus before changing other settings. CSM Support is the original target, but its behavior after saving still needs testing.

To restore the original menu switch:

```bash
sudo python3 bios/cmos_menu.py restore --backup bios/backups/spare-original.json
```

Reboot again to have the firmware rebuild its restriction variables. Restoring this byte does not undo settings changed through the newly visible menus.

The switch is expected to persist across normal reboots and shutdowns while CMOS retains its contents. The examined code reads it each boot and does not consume or clear it. A CMOS clear, battery loss, or a firmware update could reset it. Persistence has not yet been tested on hardware.

## How it works

The switch is in the `CBB_Dxe` driver, FFS GUID `3F50183A-9A93-476B-9140-D81722239CCE`. The extracted PE32 body has SHA-256 `9a1b82b4738d6086bb9ae622001bc52529c407a093afef0bf7937fd0c8f779bb`.

Relevant PE32 addresses:

```asm
0x529  mov edx, 0x70
0x52e  mov al, 0x54
0x537  out dx, al
0x538  mov edx, 0x71
0x540  in al, dx
0x54b  cmp al, 0x35
0x561  setne byte ptr [rsp + 0x241]
```

The code then calls `SetVariable` four times with a two-byte payload. The compared value determines the second byte; the emulation does not establish the first byte's meaning.

| Variable | GUID |
| --- | --- |
| InspurPchSetupFeatures | `D19A26A3-17F1-48C3-8A1E-11EB0A7F6E4E` |
| InspurSocketSetupFeatures | `07013588-C789-4E12-A7C3-88FAFAE79F7C` |
| InspurGenSetupFeature | `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9` |
| InspurMgmtSetupFeature | `01239999-FC0E-4B6E-9E79-D54D5DB6CD20` |

Each call uses attributes `0x2`, or boot-service access without nonvolatile storage. The CMOS byte supplies the persistent input; the restriction variables are populated during boot.

In the Setup IFR, question `0xC5` maps to `InspurGenSetupFeature` at offset `1`. The CSM Configuration reference at PE32 offset `0x1439D` is suppressed when this question equals `1`. CSM Support at `0x15B0C` has the same vendor condition and maps to `Setup[0x6B]`, with `0` for Disabled and `1` for Enabled. It also has independent access, CSM-state and Secure Boot conditions.

In SocketSetup, question `0x14FD` maps to `InspurSocketSetupFeatures` at offset `1` and controls many of the processor, memory and IIO suppressions.

## Reproducing the offline analysis

Use [UEFIExtract](https://github.com/LongSoft/UEFITool) to unpack a copy of the original image. The analysis used UEFIExtract A76 and [IFRExtractor-RS](https://github.com/LongSoft/IFRExtractor-RS) 1.6.1.

```bash
/path/to/uefiextract /path/to/original.bin all
```

In the resulting `.dump` tree, find `CBB_Dxe`, then its nested `PE32 image section/body.bin`. Copy that file as `CBB_Dxe.bin`. Use the PE32 body, without its section header. Do the same for Setup and SocketSetup if inspecting the menu conditions, then run `ifrextractor Setup.bin verbose` and `ifrextractor SocketSetup.bin verbose`.

The emulator checks the CBB_Dxe hash before running the menu-gate block. It mocks the CMOS input and runtime-service calls, verifies the four variable names and GUIDs, and checks the payload for all 256 inputs. It uses `0xA5` as a marker for the first payload byte, which is outside the block being studied. It does not emulate a full boot or access hardware.

```bash
python3 -m venv bios/.venv
bios/.venv/bin/pip install -r bios/requirements-analysis.txt
bios/.venv/bin/python bios/validate_menu_gate.py /path/to/CBB_Dxe.bin
```

To test the CMOS script's write and restore logic against a temporary file:

```bash
python3 -m unittest discover -s bios -p 'test_*.py' -v
```

These tests do not write real CMOS. Dumps, extracted modules and per-server backups are not included here.

## ME access and BIOS flashing

The supplied 32 MiB image contains zeros throughout the ME region at `0x00003000` through `0x00A25FFF`. It is a partial read stored in a full-sized file, so it is not a complete recovery image.

A read-only flashrom attempt on the running server confirmed that ME is locked and failed on the first transaction at `0x3000`. The probe also reported BIOS Lock Enable, SMM BIOS write protection and SPI configuration lockdown. Descriptor permissions describing the BIOS region as read-write do not override these additional protections.

A BIOS-only patch can in principle leave an unreadable ME region untouched. [Flashrom documents region-limited access](https://chromium.googlesource.com/external/coreboot.org/flashrom/+/refs/heads/main/doc/user_docs/management_engine.rst), including `--ifd -i bios --noverify-all` for BIOS-only writes and verification. That does not establish that this board would accept a modified BIOS. The image also contains Boot Guard manifests and AMI protected-range metadata; enforcement has not been established.

No flash write was attempted. The CMOS switch avoids those patching questions for the menu restrictions described above.
