# Goal Details

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Goal Details**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xF0`, PE/section offset `0x111E8`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Controls and information

### View settings of Pool goal

Type: `Subtitle`. Offset: `0x111EE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### SocketId:

Type: `String`. Offset: `0x11200`.

Firmware help: SocketId

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0xD3`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### PhysicalId:

Type: `String`. Offset: `0x11212`.

Firmware help: PhysicalId

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0xD4`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Memory Size:

Type: `String`. Offset: `0x11224`.

Firmware help: Memory Mode Size

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xC.

Question ID: `0xD5`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### App Direct #1 Size:

Type: `String`. Offset: `0x11236`.

Firmware help: App Direct #1 Size

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xC.

Question ID: `0xD6`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### App Direct #1 Index:

Type: `Numeric`. Offset: `0x11248`.

Firmware help: App Direct #1 Index

Access: No active IFR hide condition on this path; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0x64; Step: 0x1.

Question ID: `0xD7`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xD18`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### App Direct #1 Settings:

Type: `String`. Offset: `0x11261`.

Firmware help: App Direct #1 Settings

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0x20.

Question ID: `0xD8`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### App Direct #2 Size:

Type: `String`. Offset: `0x11273`.

Firmware help: App Direct #2 Size

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xC.

Question ID: `0xD9`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### App Direct #2 Index:

Type: `Numeric`. Offset: `0x11285`.

Firmware help: App Direct #2 Index

Access: No active IFR hide condition on this path; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0x64; Step: 0x1.

Question ID: `0xDA`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xD72`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### App Direct #2 Settings:

Type: `String`. Offset: `0x1129E`.

Firmware help: App Direct #2 Settings

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0x20.

Question ID: `0xDB`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Storage Capacity:

Type: `String`. Offset: `0x112B0`.

Firmware help: Storage Mode Size

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xC.

Question ID: `0xDC`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Back to AEP details

Type: `Ref`. Offset: `0x112D3`.

Firmware help: View AEP details

Opens: [AEP](5fbcd3def87d-0-fE3.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xDD`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x112CB`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### View AEPs

Type: `Ref`. Offset: `0x112EC`.

Firmware help: View and configure installed AEPs.

Opens: [AEPs](5fbcd3def87d-0-fE2.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xDE`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x112E4`: (NVMDIMM_IFRDATA&#91;0xF06&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Pools menu

Type: `Ref`. Offset: `0x11305`.

Firmware help: View and configure AEPs pools

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xDF`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x112FD`: (NVMDIMM_IFRDATA&#91;0xF08&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x11316`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: No active IFR hide condition on this path.

Question ID: `0xE0`. Question flags: `0x0` (none of the decoded flags).

### (internal Action, Q0xF010)

Type: `Action`. Offset: `0x11325`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; read-only flag.

Question ID: `0xF010`. Question flags: `0x5` (read-only, callback).
