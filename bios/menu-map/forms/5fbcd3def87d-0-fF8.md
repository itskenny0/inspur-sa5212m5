# Configure Data Policy

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; AEPs &gt; Configure data policy**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xF8`, PE/section offset `0x10E8A`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [AEPs](5fbcd3def87d-0-fE2.md) via Configure data policy, offset `0xE125`.
- [AEP](5fbcd3def87d-0-fE3.md) via Configure data policy, offset `0xE782`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Enable First Fast Refresh, offset `0x10ED8`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Disable First Fast Refresh, offset `0x10EF1`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Enable Viral Policy, offset `0x10F0A`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Disable Viral Policy, offset `0x10F23`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Enable First Fast Refresh, offset `0x10F69`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Disable First Fast Refresh, offset `0x10F82`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Enable Viral Policy, offset `0x10FA5`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Disable Viral Policy, offset `0x10FBE`.

## Controls and information

### Specify the data policy settings on ALL the AEPs

Type: `Subtitle`. Offset: `0x10E98`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10E90`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Specify the data policy settings on the AEP

Type: `Subtitle`. Offset: `0x10EB4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10EAC`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Enable First Fast Refresh

Type: `Ref`. Offset: `0x10ED8`.

Firmware help: Enable acceleration of first fast refresh

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF803`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10EBF`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10ED0`: (NVMDIMM_IFRDATA&#91;0x872&#93; (First fast refresh) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Disable First Fast Refresh

Type: `Ref`. Offset: `0x10EF1`.

Firmware help: Disable acceleration of first fast refresh

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF805`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10EBF`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10EE9`: (NVMDIMM_IFRDATA&#91;0x872&#93; (First fast refresh) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Enable Viral Policy

Type: `Ref`. Offset: `0x10F0A`.

Firmware help: Enable viral policy

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF807`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10EBF`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F02`: (NVMDIMM_IFRDATA&#91;0x873&#93; (Viral policy) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Disable Viral Policy

Type: `Ref`. Offset: `0x10F23`.

Firmware help: Disable viral policy

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF809`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10EBF`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F1B`: (NVMDIMM_IFRDATA&#91;0x873&#93; (Viral policy) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Enable First Fast Refresh

Type: `Ref`. Offset: `0x10F69`.

Firmware help: Enable acceleration of first fast refresh

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF802`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F48`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F59`: (NVMDIMM_IFRDATA&#91;0x175D&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F61`: (NVMDIMM_IFRDATA&#91;0x872&#93; (First fast refresh) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Disable First Fast Refresh

Type: `Ref`. Offset: `0x10F82`.

Firmware help: Disable acceleration of first fast refresh

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF804`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F48`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F59`: (NVMDIMM_IFRDATA&#91;0x175D&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F7A`: (NVMDIMM_IFRDATA&#91;0x872&#93; (First fast refresh) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Enable Viral Policy

Type: `Ref`. Offset: `0x10FA5`.

Firmware help: Enable viral policy

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF806`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F48`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F95`: (NVMDIMM_IFRDATA&#91;0x175E&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F9D`: (NVMDIMM_IFRDATA&#91;0x873&#93; (Viral policy) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Disable Viral Policy

Type: `Ref`. Offset: `0x10FBE`.

Firmware help: Disable viral policy

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF808`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F48`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10F95`: (NVMDIMM_IFRDATA&#91;0x175E&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FB6`: (NVMDIMM_IFRDATA&#91;0x873&#93; (Viral policy) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to AEP details

Type: `Ref`. Offset: `0x10FED`.

Firmware help: View AEP details

Opens: [AEP](5fbcd3def87d-0-fE3.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xC6`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### View AEPs

Type: `Ref`. Offset: `0x11006`.

Firmware help: View and configure installed AEPs.

Opens: [AEPs](5fbcd3def87d-0-fE2.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xC7`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FFE`: (NVMDIMM_IFRDATA&#91;0xF06&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Pools menu

Type: `Ref`. Offset: `0x1101F`.

Firmware help: View and configure AEPs pools

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xC8`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11017`: (NVMDIMM_IFRDATA&#91;0xF08&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x11030`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xC9`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Action, Q0xF810)

Type: `Action`. Offset: `0x1103F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Question ID: `0xF810`. Question flags: `0x5` (read-only, callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
