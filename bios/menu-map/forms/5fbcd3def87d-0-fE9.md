# Pool

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Pool**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xE9`, PE/section offset `0x11112`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Controls and information

### View settings.

Type: `Subtitle`. Offset: `0x11118`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### Pool Id:

Type: `String`. Offset: `0x1112A`.

Firmware help: Pool Id

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0xCB`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Capacity:

Type: `String`. Offset: `0x1113C`.

Firmware help: Capacity

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0xCC`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Health:

Type: `String`. Offset: `0x1114E`.

Firmware help: Health

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0x9.

Question ID: `0xCD`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Available capacity:

Type: `String`. Offset: `0x11160`.

Firmware help: Available capacity

Access: No active IFR hide condition on this path; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0xCE`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Back to AEP details

Type: `Ref`. Offset: `0x11183`.

Firmware help: View AEP details

Opens: [AEP](5fbcd3def87d-0-fE3.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xCF`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x1117B`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### View AEPs

Type: `Ref`. Offset: `0x1119C`.

Firmware help: View and configure installed AEPs.

Opens: [AEPs](5fbcd3def87d-0-fE2.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xD0`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x11194`: (NVMDIMM_IFRDATA&#91;0xF06&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Pools menu

Type: `Ref`. Offset: `0x111B5`.

Firmware help: View and configure AEPs pools

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xD1`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x111AD`: (NVMDIMM_IFRDATA&#91;0xF08&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x111C6`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: No active IFR hide condition on this path.

Question ID: `0xD2`. Question flags: `0x0` (none of the decoded flags).

### (internal Action, Q0xE910)

Type: `Action`. Offset: `0x111D5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; read-only flag.

Question ID: `0xE910`. Question flags: `0x5` (read-only, callback).
