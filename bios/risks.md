# Menu unlock risks and recovery

The CMOS switch is a built-in firmware path, and the examined block changes menu restriction variables. It does not itself program CPU voltage, erase storage, disable CSM, or write a modified BIOS. That makes it a smaller change than patching and reflashing the image. It has **not** been tested by writing the byte and rebooting, so there is no hardware evidence yet that it is harmless on this board.

The main danger is what becomes available afterward. Some of the forms are reference-code and debug controls, and several explicitly describe destructive or disruptive operations. A setting being visible is not evidence that it is supported by the installed hardware or safe to change.

## The CMOS write itself

| Issue | Evidence and limits |
| --- | --- |
| Wrong address or device | The target is CMOS `0x54`, mapped to `/dev/nvram` offset `0x46`. Writing device offset `0x54` would touch a different CMOS byte. The script fixes the address and checks the device type. |
| Different firmware | The code is confirmed only in the researched 3.0.29 image. Matching server branding is insufficient. The script checks board ID and BIOS version, but those checks are not a substitute for verifying a different firmware image. |
| Checksum handling | Linux checks the standard PC CMOS checksum before reading or writing. A checksum error stops the script. It must not be bypassed by clearing NVRAM or forcing a checksum update. |
| Other consumers of the byte | A limited scan of 390 x86 PE images found only the CBB_Dxe gate using the literal `mov al, 0x54` near port output. That does not rule out table-driven access, helpers using another instruction encoding, TE code, SMM activity, or BMC access. |
| Unexpected setup behavior | Only the gate block was emulated. Driver callbacks, alternate AMITSE menu tables and interactions during a full boot have not been tested. An exposed form could behave incorrectly even if no setting is intentionally changed. |
| Persistent exposure | The CMOS value is expected to survive normal boots. Leaving it selected leaves more configuration controls available to someone with setup access. Administrator checks and other restrictions still exist. |
| Incomplete reversal | Restoring `0xFF` restores the menu switch. It does not undo values changed in setup, storage operations, firmware updates, or BMC user changes. |

The [Linux 6.8 NVRAM driver](https://github.com/torvalds/linux/blob/v6.8/drivers/char/nvram.c) holds the RTC lock and maintains the standard checksum. Its checksum covers CMOS `0x10` through `0x2D`, with the result at `0x2E` and `0x2F`. The target `0x54` is outside that range. The driver still rewrites the two checksum bytes after a write; their values should remain the same if the covered bytes have not changed. This does not establish whether the vendor has any additional integrity checks.

Use the kernel device rather than manually writing ports `0x70` and `0x71` from userspace. Those ports share an index register with other RTC users, and raw accesses do not participate in the kernel's lock. The script deliberately has no raw-port fallback.

The limited direct-access search can be reproduced offline after installing `requirements-analysis.txt`:

```bash
bios/.venv/bin/python bios/scan_cmos_access.py /path/to/original.bin.dump
```

## Controls that deserve particular care

These examples are present in this image. The effects below distinguish explicit firmware help from consequences inferred from the kind of control. The menu map preserves the exact help, choices and conditions for each record.

| Controls and location | Risk |
| --- | --- |
| [Advanced > CSM Configuration](menu-map/forms/53022c42f931-0-f2743.md) | Disabling CSM removes legacy boot services. A legacy OS loader or an adapter with only a legacy option ROM may stop working. UEFI video support also matters for the local display and BMC console. The inspected host had no `/sys/firmware/efi`; a working UEFI boot path has not been demonstrated. |
| [Chipset > PCH SATA Configuration](menu-map/forms/f44ace4934bd-0-f68.md), plus the RSTe/VROC driver forms | Changing controller mode, port enablement, RAID configuration, or boot device selection can make the existing OS or disks unavailable. Array creation, deletion and reset actions can destroy data. Exact consequences depend on the controller and its driver. |
| [Processor > Processor Configuration](menu-map/forms/c4ed43ec5ea4-0-f513.md), Active Cores | Firmware help says `0` enables all cores and `3fff` disables all cores. Do not interpret this numeric control as a simple count. The label and help suggest a mask, and an unsuitable value may prevent startup. Its complete implementation has not been audited. |
| [Processor > Memory Configuration](menu-map/forms/c4ed43ec5ea4-0-f540.md) and [Memory Timings Override](menu-map/forms/c4ed43ec5ea4-0-f581.md) | Frequency, training, timing, voltage and interleave changes can prevent POST or cause memory instability. The Memory Frequency help explicitly says not to select Reserved values. Enforce POR controls reference-code restrictions for DDR4 frequency and voltage. |
| [Memory Thermal](menu-map/forms/c4ed43ec5ea4-0-f580.md) | Throttling Mode has a Disabled choice. EN_MEMTRIP help says a zero value makes the processor ignore MEMtrip. Changing thermal protections can increase the risk of overheating or damage. The system's other protections have not been audited. |
| [Chipset > OverClocking Feature > Processor](menu-map/forms/f44ace4934bd-0-f3F6.md) and [CLR/Ring](menu-map/forms/f44ace4934bd-0-f3F3.md) | Voltage override and offset controls can cause instability, excess heat or hardware damage if the processor applies them. A displayed range is an encoding range, not a safe operating range. The UI does not prove that the installed Xeons support these controls. |
| [Chipset > OverClocking Feature > SVID/FIVR](menu-map/forms/f44ace4934bd-0-f3F5.md), FIVR Faults | The firmware explicitly warns that disabling FIVR faults masks overvoltage and overcurrent protection. This is a hardware-protection control with an explicit danger warning in the vendor help. |
| [NGNVM DIMM Secure Erase Unit](menu-map/forms/c4ed43ec5ea4-0-f58E.md) | The help explicitly says Erase All DIMMs erases the persistent-memory region of all NVMDIMMs. Individual socket/channel controls are also present. Restoring CMOS cannot recover erased data. |
| [Intel DIMM Gen 1 Configuration](menu-map/5fbcd3def87d-0.md) | Contains security, namespace, firmware-update and other persistent-memory management forms. These can affect stored data or DIMM firmware when compatible devices are installed. They are not all tied to the CMOS vendor gate. |
| [Chipset > Runtime Error Logging](menu-map/forms/f44ace4934bd-0-f500.md) and [Error Injection Settings](menu-map/forms/f44ace4934bd-0-f503.md) | Error injection is intended to provoke hardware error handling. FatalErrDebugHalt explicitly warns that a thread will halt in the fatal-error flow and says to use it with ITP. These are debug functions, not performance tuning. |
| Processor > IIO Configuration, UPI and individual PCIe port pages | Lane configuration, link width/speed, port disablement, MMIO windows and interconnect changes can remove access to storage, NICs or other devices, or prevent boot. Incorrect settings can also affect passthrough and isolation. |
| [Chipset > PCH Configuration > Security Configuration](menu-map/forms/f44ace4934bd-0-f10F.md) | SMM BIOS Write Protect and related controls affect firmware protection. Clearing the menu restrictions does not itself disable these protections. Do not assume that turning a UI option off will bypass a lock already established during boot. |
| [Security](menu-map/forms/53022c42f931-0-f2714.md) and its referenced pages | Passwords, TPM controls and Secure Boot keys can affect boot authorization and access. Key deletion, password changes and TPM operations require their own recovery plan. They are separate from exposing menus. |
| [Server Mgmt > BMC User Settings](menu-map/forms/24368718aeae-0-f834.md), network settings and log actions | A user or network change can remove remote management access. Erasing logs removes diagnostic evidence. BMC user actions may run through callbacks rather than waiting for a normal BIOS save. |
| [Recovery](menu-map/bdc5290bdcb5-0.md) | The forms include a flash-update workflow. Using it writes firmware, and the supplied image is not a full recovery backup. |

The CSM/video concern is also documented by another AMI server vendor in [Supermicro FAQ 21167](https://www.supermicro.com/en/support/faqs/faq.php?faq=21167). That supports the general dependency on UEFI video support; it does not confirm GOP support on this Inspur board.

The forms contain callback flags on controls such as CSM Support. A callback may perform work when a question changes or a form is opened. Do not assume that Exit Without Saving can reverse every action. The flag definitions are in the [EDK II IFR header](https://github.com/tianocore/edk2/blob/master/MdePkg/Include/Uefi/UefiInternalFormRepresentation.h); the particular handlers would need auditing to establish all side effects.

## First test on the spare server

The first test should isolate the switch: record the existing byte and setup values, write the switch with the backup script, reboot, inspect the menus, and leave the other settings alone. Then restore the byte and check the next boot. This tests whether the switch works and persists without mixing in a CSM conversion or tuning changes.

The next test can address CSM separately, after confirming that the spare has a working UEFI OS loader and compatible option ROMs. Physical access matters because changes to video, boot, networking or PCIe settings can remove both the normal boot path and remote access.

The generated map identifies hidden and disabled conditions, but it is not a recommendation to change every newly available control. Reserved values, fake varstore items, empty internal questions, DFX pages and error-injection controls should not be treated as ordinary configuration options.

## Recovery limits

If Linux still boots, use the saved per-server JSON backup with `cmos_menu.py restore`. A manual write of the previously observed value is also possible, but the backup avoids assuming every server started at `0xFF`.

If it no longer boots, software rollback may be unavailable. The [SA5212M5 manual V2.5](<../浪潮英信服务器 SA5212M5 用户手册 V2.5.pdf>), section 3.6, printed page 18, describes a CLR_CMOS jumper labelled J81, with normal pins 1-2 and clear pins 2-3. The researched board reports SA5212H5 and dates from an older firmware generation. **Confirm the physical board and the applicable procedure before relying on that jumper designation.** Disconnect power before moving jumpers and follow the matched board's full procedure.

A CMOS clear can discard other configuration and is not proven to clear every UEFI variable or BMC setting. It cannot undo a storage erase or repair a failed component firmware update. The dump's ME region is zero-filled, so it cannot be used as a complete chip restore. An external programmer and a valid full backup would be needed for that kind of recovery.

The spare-server test has not happened yet. No CMOS, setup-variable or firmware writes were performed during this research.
