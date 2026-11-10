# AEP

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; AEPs &gt; Configure data policy &gt; Back to AEP details**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xE3`, PE/section offset `0xE147`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [AEP](5fbcd3def87d-0-fE3.md) via Back to AEP details, offset `0xE79B`.
- [Monitor Health](5fbcd3def87d-0-fE6.md) via Back to AEP details, offset `0x1086C`.
- [Update Firmware](5fbcd3def87d-0-fE5.md) via Back to AEP details, offset `0x109CC`.
- [Configure Security](5fbcd3def87d-0-fE7.md) via Back to AEP details, offset `0x10E25`.
- [Configure Data Policy](5fbcd3def87d-0-fF8.md) via Back to AEP details, offset `0x10FED`.
- [Pool](5fbcd3def87d-0-fE9.md) via Back to AEP details, offset `0x11183`.
- [Goal Details](5fbcd3def87d-0-fF0.md) via Back to AEP details, offset `0x112D3`.
- [Create goal config](5fbcd3def87d-0-fF1.md) via Back to AEP details, offset `0x11716`.
- [Delete goal config](5fbcd3def87d-0-fF4.md) via Back to AEP details, offset `0x11A1D`.

## Controls and information

### View settings or select an action below.

Type: `Subtitle`. Offset: `0xE14D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Dimm UID

Type: `String`. Offset: `0xE15F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x16.

Question ID: `0x7`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Manageability state

Type: `OneOf`. Offset: `0xE171`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Manageable | 1 | none | none |
| Unmanageable | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8`. Question flags: `0x11` (read-only, reset required).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x861`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Firmware version

Type: `String`. Offset: `0xE192`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x13.

Question ID: `0x9`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Health state

Type: `OneOf`. Offset: `0xE1A4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Healthy | 0 | none | none |
| Non-critical failure | 1 | none | none |
| Critical failure | 2 | none | none |
| Fatal error | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0xA`. Question flags: `0x11` (read-only, reset required).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x862`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Capacity

Type: `String`. Offset: `0xE1D3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x12.

Question ID: `0xB`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Manufacturer

Type: `String`. Offset: `0xE1E5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x13.

Question ID: `0xC`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Firmware API version

Type: `String`. Offset: `0xE1F7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x6.

Question ID: `0xD`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Lock state

Type: `OneOf`. Offset: `0xE209`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Unlocked | 3 | none | none |
| Locked | 2 | none | none |
| Frozen | 4 | none | none |
| Count Expired | 5 | none | none |
| Not supported | 6 | none | none |

Size: 8; Min: 0x1; Max: 0x6; Step: 0x0.

Question ID: `0xE`. Question flags: `0x11` (read-only, reset required).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x860`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Show more details +

Type: `CheckBox`. Offset: `0xE246`.

Firmware help: Show or hide additional details about the AEP.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0xF`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF09`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Serial number

Type: `String`. Offset: `0xE267`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x13.

Question ID: `0x10`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket

Type: `String`. Offset: `0xE279`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x11`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Memory controller ID

Type: `String`. Offset: `0xE28B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x12`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Vendor ID

Type: `String`. Offset: `0xE29D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x13`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Device ID

Type: `String`. Offset: `0xE2AF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x14`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Subsystem vendor ID

Type: `String`. Offset: `0xE2C1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x15`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Subsystem device ID

Type: `String`. Offset: `0xE2D3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x16`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Device locator

Type: `String`. Offset: `0xE2E5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x80.

Question ID: `0x17`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Dimm handle

Type: `Numeric`. Offset: `0xE2F7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x1.

Question ID: `0x18`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x850`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Revision ID

Type: `String`. Offset: `0xE31C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x19`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Subsystem revision ID

Type: `String`. Offset: `0xE32E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x1A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Interface format code

Type: `String`. Offset: `0xE340`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x20.

Question ID: `0x1B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Manufacturer ID

Type: `String`. Offset: `0xE352`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x1C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Manufacturing info valid

Type: `Numeric`. Offset: `0xE364`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x1D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x876`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Manufacturing date

Type: `Numeric`. Offset: `0xE37D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 16; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x1E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x85E`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Manufacturing location

Type: `Numeric`. Offset: `0xE39A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x1F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x875`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Model

Type: `String`. Offset: `0xE3B3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x14.

Question ID: `0x20`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Memory type

Type: `String`. Offset: `0xE3C5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x12.

Question ID: `0x21`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Is new

Type: `Numeric`. Offset: `0xE3D7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x22`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x863`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Form factor

Type: `OneOf`. Offset: `0xE3F0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Unknown | 0 | none | none |
| Unknown | 2 | none | none |
| DIMM | 9 | none | none |
| SODIMM | 13 | none | none |

Size: 8; Min: 0x0; Max: 0xD; Step: 0x0.

Question ID: `0x23`. Question flags: `0x11` (read-only, reset required).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x864`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Memory capacity

Type: `String`. Offset: `0xE41F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x24`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct capacity

Type: `String`. Offset: `0xE431`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x25`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Unconfigured capacity

Type: `String`. Offset: `0xE443`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x26`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Inaccessible capacity

Type: `String`. Offset: `0xE455`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x27`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Reserved capacity

Type: `String`. Offset: `0xE467`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x28`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Part number

Type: `String`. Offset: `0xE479`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x20.

Question ID: `0x29`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Memory bank label

Type: `String`. Offset: `0xE48B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0x20.

Question ID: `0x2A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Data width label &#91;b&#93;

Type: `String`. Offset: `0xE49D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x2B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Total width &#91;b&#93;

Type: `String`. Offset: `0xE4AF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x2C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Speed &#91;MHz&#93;

Type: `String`. Offset: `0xE4C1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x2D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### FW logging level

Type: `OneOf`. Offset: `0xE4D3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Error | 1 | none | none |
| Warning | 2 | none | none |
| Info | 3 | none | none |
| Debug | 4 | none | none |
| Unknown | 5 | none | none |

Size: 8; Min: 0x0; Max: 0x5; Step: 0x0.

Question ID: `0x2E`. Question flags: `0x11` (read-only, reset required).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x865`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Power management enabled

Type: `Numeric`. Offset: `0xE510`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x2F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x866`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Power limit &#91;W&#93;

Type: `Numeric`. Offset: `0xE529`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 10.

Size: 8; Min: 0xA; Max: 0xFF; Step: 0x1.

Question ID: `0x30`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x867`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Peak power budget &#91;mW&#93;

Type: `Numeric`. Offset: `0xE542`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 10000.

Size: 16; Min: 0x2710; Max: 0xFFFF; Step: 0x1.

Question ID: `0x31`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x856`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Avg power budget &#91;mW&#93;

Type: `Numeric`. Offset: `0xE55F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 10000.

Size: 16; Min: 0x2710; Max: 0xFFFF; Step: 0x1.

Question ID: `0x32`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x858`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Die sparing capable

Type: `Numeric`. Offset: `0xE57C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x33`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x868`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Die sparing enabled

Type: `Numeric`. Offset: `0xE595`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x34`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x869`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Die sparing level

Type: `Numeric`. Offset: `0xE5AE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x35`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x86A`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Die spares used

Type: `Numeric`. Offset: `0xE5C7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 16; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x36`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x85A`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Configuration status

Type: `OneOf`. Offset: `0xE5E4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Valid | 0 | none | none |
| Not Configured | 1 | none | none |
| Failed - Bad configuration | 2 | none | none |
| Failed - Broken interleave | 3 | none | none |
| Failed - Reverted | 4 | none | none |
| Failed - Unsupported | 5 | none | none |

Size: 8; Min: 0x0; Max: 0x5; Step: 0x0.

Question ID: `0x37`. Question flags: `0x11` (read-only, reset required).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x86F`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### SKU violation

Type: `Numeric`. Offset: `0xE621`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x38`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x870`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### ARS status

Type: `OneOf`. Offset: `0xE63A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Unknown | 0 | none | none |
| Not Started | 1 | none | none |
| In Progress | 2 | none | none |
| Completed | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0x39`. Question flags: `0x11` (read-only, reset required).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x871`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Last shutdown time &#91;ms&#93;

Type: `Numeric`. Offset: `0xE669`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x1.

Question ID: `0x3A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x848`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### First fast refresh

Type: `Numeric`. Offset: `0xE69E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x3B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x872`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Viral policy

Type: `Numeric`. Offset: `0xE6B7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x3C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x873`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Viral state

Type: `Numeric`. Offset: `0xE6D0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x3D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x874`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Channel ID

Type: `String`. Offset: `0xE6E9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x3E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Channel pos

Type: `Numeric`. Offset: `0xE6FB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 16; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x3F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x85C`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE25F`: (NVMDIMM_IFRDATA&#91;0xF09&#93; (Show more details +) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Monitor health

Type: `Ref`. Offset: `0xE74D`.

Firmware help: Display AEPs health status and thresholds.

Opens: [Monitor Health](5fbcd3def87d-0-fE6.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x40`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Update firmware

Type: `Ref`. Offset: `0xE764`.

Firmware help: Go to the update firmware page

Opens: [Update Firmware](5fbcd3def87d-0-fE5.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x41`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE75C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Configure security

Type: `Ref`. Offset: `0xE773`.

Firmware help: Go to the configure security page

Opens: [Configure Security](5fbcd3def87d-0-fE7.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x42`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE75C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Configure data policy

Type: `Ref`. Offset: `0xE782`.

Firmware help: Go to the configure data policy page

Opens: [Configure Data Policy](5fbcd3def87d-0-fF8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x43`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE75C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to AEP details

Type: `Ref`. Offset: `0xE79B`.

Firmware help: View AEP details

Opens: [AEP](5fbcd3def87d-0-fE3.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x44`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE793`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### View AEPs

Type: `Ref`. Offset: `0xE7B4`.

Firmware help: View and configure installed AEPs.

Opens: [AEPs](5fbcd3def87d-0-fE2.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x45`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE7AC`: (NVMDIMM_IFRDATA&#91;0xF06&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Pools menu

Type: `Ref`. Offset: `0xE7CD`.

Firmware help: View and configure AEPs pools

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x46`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE7C5`: (NVMDIMM_IFRDATA&#91;0xF08&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0xE7DE`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x47`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Action, Q0xE310)

Type: `Action`. Offset: `0xE7ED`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Question ID: `0xE310`. Question flags: `0x5` (read-only, callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE11D`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10FE5`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

## Runtime insertion labels

The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.

- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x13
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x14
