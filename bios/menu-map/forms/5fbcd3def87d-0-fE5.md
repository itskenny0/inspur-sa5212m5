# Update Firmware

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; AEPs &gt; Update firmware**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xE5`, PE/section offset `0x108D1`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [AEPs](5fbcd3def87d-0-fE2.md) via Update firmware, offset `0xE0F3`.
- [AEP](5fbcd3def87d-0-fE3.md) via Update firmware, offset `0xE764`.
- [Update Firmware](5fbcd3def87d-0-fE5.md) via Update, offset `0x109B3`.

## Controls and information

### Specify the firmware image to load on the AEP on the next system restart and select Update.

Type: `Subtitle`. Offset: `0x108DF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x108D7`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### WARNING: Modifying the settings of a single AEP may result in an unusable configuration.

Type: `Subtitle`. Offset: `0x108E8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x108D7`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Specify the firmware image to load on ALL the AEPs on the next system restart and select Update.

Type: `Subtitle`. Offset: `0x108FB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x108F3`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Current FW Version:

Type: `String`. Offset: `0x10929`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x13.

Question ID: `0xB8`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10921`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Current FW Version:

Type: `String`. Offset: `0x10945`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x13.

Question ID: `0xB9`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1093D`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Selected FW Version:

Type: `String`. Offset: `0x10962`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x13.

Question ID: `0xBA`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### File:

Type: `String`. Offset: `0x10974`.

Firmware help: Please provide file path relative to the root directory of the device containing the new Firmware. For example: "\firmware\newFirmware.bin"

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

MinSize: 0x2; MaxSize: 0xFF.

Question ID: `0xE502`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### WARNING: Selected firmware is older than the installed version.

Type: `Subtitle`. Offset: `0x10997`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1098F`: (NVMDIMM_IFRDATA&#91;0x1513&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Update

Type: `Ref`. Offset: `0x109B3`.

Firmware help: Perform the FW Update

Opens: [Update Firmware](5fbcd3def87d-0-fE5.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xE501`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x109AB`: (NVMDIMM_IFRDATA&#91;0x1276&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to AEP details

Type: `Ref`. Offset: `0x109CC`.

Firmware help: View AEP details

Opens: [AEP](5fbcd3def87d-0-fE3.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xBB`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x109C4`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### View AEPs

Type: `Ref`. Offset: `0x109E5`.

Firmware help: View and configure installed AEPs.

Opens: [AEPs](5fbcd3def87d-0-fE2.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xBC`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x109DD`: (NVMDIMM_IFRDATA&#91;0xF06&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Pools menu

Type: `Ref`. Offset: `0x109FE`.

Firmware help: View and configure AEPs pools

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xBD`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x109F6`: (NVMDIMM_IFRDATA&#91;0xF08&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x10A0F`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xBE`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Action, Q0xE510)

Type: `Action`. Offset: `0x10A1E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Question ID: `0xE510`. Question flags: `0x5` (read-only, callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
