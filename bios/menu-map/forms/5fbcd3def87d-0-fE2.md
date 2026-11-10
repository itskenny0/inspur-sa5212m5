# AEPs

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; AEPs**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xE2`, PE/section offset `0xE091`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md) via AEPs, offset `0xE01D`.
- [AEP](5fbcd3def87d-0-fE3.md) via View AEPs, offset `0xE7B4`.
- [Monitor Health](5fbcd3def87d-0-fE6.md) via View AEPs, offset `0x10885`.
- [Update Firmware](5fbcd3def87d-0-fE5.md) via View AEPs, offset `0x109E5`.
- [Configure Security](5fbcd3def87d-0-fE7.md) via View AEPs, offset `0x10E3E`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via View AEPs, offset `0x11006`.
- [Pool](5fbcd3def87d-0-fE9.md) via View AEPs, offset `0x1119C`.
- [Goal Details](5fbcd3def87d-0-fF0.md) via View AEPs, offset `0x112EC`.
- [Create goal config](5fbcd3def87d-0-fF1.md) via View AEPs, offset `0x1172F`.
- [Delete goal config](5fbcd3def87d-0-fF4.md) via View AEPs, offset `0x11A36`.

## Controls and information

### Select a specific AEP to view more information.

Type: `Subtitle`. Offset: `0xE097`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Monitor health

Type: `Ref`. Offset: `0xE0DC`.

Firmware help: Display AEPs health status and thresholds.

Opens: [Monitor Health](5fbcd3def87d-0-fE6.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0x2`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Update firmware

Type: `Ref`. Offset: `0xE0F3`.

Firmware help: Go to the update firmware page

Opens: [Update Firmware](5fbcd3def87d-0-fE5.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x3`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE0EB`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Configure security

Type: `Ref`. Offset: `0xE10C`.

Firmware help: Go to the configure security page

Opens: [Configure Security](5fbcd3def87d-0-fE7.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x4`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE104`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Configure data policy

Type: `Ref`. Offset: `0xE125`.

Firmware help: Go to the configure data policy page

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x5`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0xE136`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0x6`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

## Runtime insertion labels

The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.

- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x1
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x2
