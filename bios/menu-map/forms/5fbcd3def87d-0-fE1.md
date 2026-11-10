# Intel DIMM Gen 1 Configuration

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xE1`, PE/section offset `0xDF51`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [AEPs](5fbcd3def87d-0-fE2.md) via Back to Main menu, offset `0xE136`.
- [AEP](5fbcd3def87d-0-fE3.md) via Back to Main menu, offset `0xE7DE`.
- [Monitor Health](5fbcd3def87d-0-fE6.md) via Back to Main menu, offset `0x108AF`.
- [Update Firmware](5fbcd3def87d-0-fE5.md) via Back to Main menu, offset `0x10A0F`.
- [Configure Security](5fbcd3def87d-0-fE7.md) via Back to Main menu, offset `0x10E68`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Back to Main menu, offset `0x11030`.
- [Pools](5fbcd3def87d-0-fE8.md) via Back to Main menu, offset `0x11101`.
- [Pool](5fbcd3def87d-0-fE9.md) via Back to Main menu, offset `0x111C6`.
- [Goal Details](5fbcd3def87d-0-fF0.md) via Back to Main menu, offset `0x11316`.
- [Create goal config](5fbcd3def87d-0-fF1.md) via Back to Main menu, offset `0x11759`.
- [Total Capacity](5fbcd3def87d-0-fF2.md) via Back to Main menu, offset `0x1180C`.
- [Diagnostics](5fbcd3def87d-0-fF5.md) via Back to Main menu, offset `0x1183B`.
- [Diagnostics Results](5fbcd3def87d-0-fF6.md) via Back to Main menu, offset `0x118FF`.
- [Delete goal config](5fbcd3def87d-0-fF4.md) via Back to Main menu, offset `0x11A60`.
- [Namespaces](5fbcd3def87d-0-fEA.md) via Back to Main menu, offset `0x11ACB`.
- [Namespace](5fbcd3def87d-0-fEB.md) via Back to Main menu, offset `0x11E3B`.
- [Create Namespace](5fbcd3def87d-0-fED.md) via Back to Main menu, offset `0x120FC`.

## Controls and information

### There are no AEPs detected in the system.

Type: `Subtitle`. Offset: `0xDF63`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF57`: Not((NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Select an action below.

Type: `Subtitle`. Offset: `0xDF7F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Detected AEPs:

Type: `Numeric`. Offset: `0xDF91`.

Firmware help: Detected AEPs:

Access: Conditional; no CMOS vendor gate on this path; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 32; Min: 0x0; Max: 0x64; Step: 0x1.

Question ID: `0x1`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Warning! Problem detected on one or more AEPs. Please go to the AEPs for more information.

Type: `Subtitle`. Offset: `0xDFBE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDFB6`: (NVMDIMM_IFRDATA&#91;0x1510&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### All AEPs are healthy.

Type: `Subtitle`. Offset: `0xDFD1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDFC9`: (NVMDIMM_IFRDATA&#91;0x1510&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Warning! Mixed SKU detected. Driver functionalities limited.

Type: `Subtitle`. Offset: `0xDFED`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDFE5`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Warning! ARS is currently in progress on the system.

Type: `Subtitle`. Offset: `0xE009`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE001`: (NVMDIMM_IFRDATA&#91;0x175F&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### AEPs

Type: `Ref`. Offset: `0xE01D`.

Firmware help: View and configure installed AEPs.

Opens: [AEPs](5fbcd3def87d-0-fE2.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xE210`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Pools

Type: `Ref`. Offset: `0xE034`.

Firmware help: View and configure AEPs pools

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xE810`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Namespaces

Type: `Ref`. Offset: `0xE04D`.

Firmware help: Display, create, modify and delete namespaces.

Opens: [Namespaces](5fbcd3def87d-0-fEA.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xEA10`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Total capacity

Type: `Ref`. Offset: `0xE05E`.

Firmware help: Show total AEP resource allocation across the host server

Opens: [Total Capacity](5fbcd3def87d-0-fF2.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xF210`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Diagnostics

Type: `Ref`. Offset: `0xE06D`.

Firmware help: Perform detailed AEP diagnostics procedure.

Opens: [Diagnostics](5fbcd3def87d-0-fF5.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xF510`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Action, Q0xE110)

Type: `Action`. Offset: `0xE07C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; read-only flag.

Question ID: `0xE110`. Question flags: `0x5` (read-only, callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
