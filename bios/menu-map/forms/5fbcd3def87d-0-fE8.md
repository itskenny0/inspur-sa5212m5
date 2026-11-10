# Pools

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Pools**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xE8`, PE/section offset `0x11052`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md) via Pools, offset `0xE034`.
- [AEP](5fbcd3def87d-0-fE3.md) via Back to Pools menu, offset `0xE7CD`.
- [Monitor Health](5fbcd3def87d-0-fE6.md) via Back to Pools menu, offset `0x1089E`.
- [Update Firmware](5fbcd3def87d-0-fE5.md) via Back to Pools menu, offset `0x109FE`.
- [Configure Security](5fbcd3def87d-0-fE7.md) via Back to Pools menu, offset `0x10E57`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Back to Pools menu, offset `0x1101F`.
- [Pool](5fbcd3def87d-0-fE9.md) via Back to Pools menu, offset `0x111B5`.
- [Goal Details](5fbcd3def87d-0-fF0.md) via Back to Pools menu, offset `0x11305`.
- [Create goal config](5fbcd3def87d-0-fF1.md) via Create goal config, offset `0x116FF`.
- [Create goal config](5fbcd3def87d-0-fF1.md) via Back to Pools menu, offset `0x11748`.
- [Delete goal config](5fbcd3def87d-0-fF4.md) via Delete goal config, offset `0x11A06`.
- [Delete goal config](5fbcd3def87d-0-fF4.md) via Back to Pools menu, offset `0x11A4F`.

## Controls and information

### Current Configuration

Type: `Subtitle`. Offset: `0x11058`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Goal Configuration

Type: `Subtitle`. Offset: `0x11094`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Create goal config

Type: `Ref`. Offset: `0x110D0`.

Firmware help: Create goal configuration of Pools

Opens: [Create goal config](5fbcd3def87d-0-fF1.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF110`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Delete goal config

Type: `Ref`. Offset: `0x110E7`.

Firmware help: Discard goal configuration of AEPs Pools

Opens: [Delete goal config](5fbcd3def87d-0-fF4.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF410`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x110DF`: (NVMDIMM_IFRDATA&#91;0xC6C&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x11101`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xCA`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

## Runtime insertion labels

The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.

- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x3
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x4
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x5
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x6
