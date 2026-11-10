# Diagnostics Results

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Diagnostics &gt; Execute tests**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xF6`, PE/section offset `0x118EA`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Diagnostics](5fbcd3def87d-0-fF5.md) via Execute tests, offset `0x1182C`.

## Controls and information

### Back to Diagnostics

Type: `Ref`. Offset: `0x118F0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Opens: [Diagnostics](5fbcd3def87d-0-fF5.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0x100`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x118FF`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0x101`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Action, Q0xF610)

Type: `Action`. Offset: `0x11941`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; read-only flag.

Question ID: `0xF610`. Question flags: `0x5` (read-only, callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

## Runtime insertion labels

The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.

- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0xB
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0xC
