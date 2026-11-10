# Namespaces

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Namespaces**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xEA`, PE/section offset `0x11A71`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md) via Namespaces, offset `0xE04D`.
- [Namespace](5fbcd3def87d-0-fEB.md) via Save, offset `0x11E0E`.
- [Namespace](5fbcd3def87d-0-fEB.md) via Delete, offset `0x11E1D`.
- [Namespace](5fbcd3def87d-0-fEB.md) via Back to Namespaces, offset `0x11E2C`.
- [Create Namespace](5fbcd3def87d-0-fED.md) via Create Namespace, offset `0x120DC`.
- [Create Namespace](5fbcd3def87d-0-fED.md) via Back to Namespaces, offset `0x120ED`.

## Controls and information

### Select a Namespace to view more information

Type: `Subtitle`. Offset: `0x11A77`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Create Namespace

Type: `Ref`. Offset: `0x11ABC`.

Firmware help: Create Namespace with desired configuration

Opens: [Create Namespace](5fbcd3def87d-0-fED.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xED10`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x11ACB`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x107`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

## Runtime insertion labels

The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.

- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0xD
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0xE
