# Diagnostics

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Diagnostics**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xF5`, PE/section offset `0x1181D`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md) via Diagnostics, offset `0xE06D`.
- [Diagnostics Results](5fbcd3def87d-0-fF6.md) via Back to Diagnostics, offset `0x118F0`.

## Controls and information

### Perform Diagnostics tests on AEPs

Type: `Subtitle`. Offset: `0x11823`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Execute tests

Type: `Ref`. Offset: `0x1182C`.

Firmware help: Execute selected diagnostics tests

Opens: [Diagnostics Results](5fbcd3def87d-0-fF6.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xF522`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x1183B`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xFA`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Choose diagnostics type:

Type: `Subtitle`. Offset: `0x11853`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Quick Diagnostics

Type: `CheckBox`. Offset: `0x1185C`.

Firmware help: Perform Quick Diagnostics test

Access: Conditional; no CMOS vendor gate on this path.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0xFB`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16F8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Config Diagnostics

Type: `CheckBox`. Offset: `0x1186C`.

Firmware help: Perform Config Diagnostics test

Access: Conditional; no CMOS vendor gate on this path.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0xFC`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16F9`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PM Diagnostics

Type: `CheckBox`. Offset: `0x1187C`.

Firmware help: Perform Persistent Memory Diagnostics test

Access: Conditional; no CMOS vendor gate on this path.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0xFD`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16FA`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### FW Diagnostics

Type: `CheckBox`. Offset: `0x1188C`.

Firmware help: Perform Firmware Diagnostics test

Access: Conditional; no CMOS vendor gate on this path.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0xFE`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16FB`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Security Diagnostics

Type: `CheckBox`. Offset: `0x1189C`.

Firmware help: Perform Security Diagnostics test

Access: Conditional; no CMOS vendor gate on this path.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0xFF`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16FC`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Choose AEPs to diagnose:

Type: `Subtitle`. Offset: `0x118B5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

## Runtime insertion labels

The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.

- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x11
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x12
