# Monitor Health

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; AEPs &gt; Monitor health**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xE6`, PE/section offset `0xE800`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [AEPs](5fbcd3def87d-0-fE2.md) via Monitor health, offset `0xE0DC`.
- [AEP](5fbcd3def87d-0-fE3.md) via Monitor health, offset `0xE74D`.

## Controls and information

### Sensor Type

Type: `OneOf`. Offset: `0xE816`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x48`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF48`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE80E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xE892`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x49`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF50`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE80E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xE8D3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x4A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF58`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE80E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE8C7`: 0x0. Expression result: stock false; CMOS unlock false.

### Critical lower threshold

Type: `Numeric`. Offset: `0xE916`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x4B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF68`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE80E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE90A`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xE94B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x4C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF70`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE80E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE90A`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xE98E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x4D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF78`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE80E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE982`: 0x0. Expression result: stock false; CMOS unlock false.

### State

Type: `OneOf`. Offset: `0xE9D1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x4E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF49`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE80E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE9C5`: 0x0. Expression result: stock false; CMOS unlock false.

### Sensor Type

Type: `OneOf`. Offset: `0xEA1C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x4F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF10`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEA14`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xEA98`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x50`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF18`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEA14`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xEAD9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x51`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF20`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEA14`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEACD`: 0x0. Expression result: stock false; CMOS unlock false.

### Critical lower threshold

Type: `Numeric`. Offset: `0xEB1C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x52`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF30`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEA14`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEB10`: 0x0. Expression result: stock false; CMOS unlock false.

### Critical upper threshold

Type: `Numeric`. Offset: `0xEB51`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x53`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF38`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEA14`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEB10`: 0x0. Expression result: stock false; CMOS unlock false.

### Fatal threshold

Type: `Numeric`. Offset: `0xEB94`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x54`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF40`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEA14`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEB88`: 0x0. Expression result: stock false; CMOS unlock false.

### State

Type: `OneOf`. Offset: `0xEBD7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x55`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF11`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEA14`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEBCB`: 0x0. Expression result: stock false; CMOS unlock false.

### Sensor Type

Type: `OneOf`. Offset: `0xEC22`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x56`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF80`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEC1A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xEC9E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x57`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF88`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEC1A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xECDF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x58`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF90`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEC1A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xECD3`: 0x0. Expression result: stock false; CMOS unlock false.

### Critical lower threshold

Type: `Numeric`. Offset: `0xED22`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x59`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFA0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEC1A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xED16`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xED57`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x5A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFA8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEC1A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xED16`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xED9A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x5B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFB0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEC1A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xED8E`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xEDDD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x5C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF81`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEC1A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEDD1`: 0x0. Expression result: stock false; CMOS unlock false.

### Sensor Type

Type: `OneOf`. Offset: `0xEE28`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x5D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFB8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEE20`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xEEA4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x5E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFC0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEE20`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xEEE5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x5F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFC8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEE20`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEED9`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xEF28`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x60`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFD8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEE20`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEF1C`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xEF5D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x61`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFE0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEE20`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEF1C`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xEFA0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x62`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFE8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEE20`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEF94`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xEFE3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x63`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFB9`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEE20`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xEFD7`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0xF02E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x64`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFF0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF026`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xF0AA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x65`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFF8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF026`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xF0EB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x66`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1000`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF026`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF0DF`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xF12E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x67`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1010`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF026`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF122`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xF163`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x68`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1018`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF026`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF122`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xF1A6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x69`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1020`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF026`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF19A`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xF1E9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x6A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xFF1`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF026`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF1DD`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0xF234`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x6B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1028`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF22C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xF2B0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x6C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1030`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF22C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xF2F1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x6D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1038`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF22C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF2E5`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xF334`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x6E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1048`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF22C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF328`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xF369`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x6F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1050`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF22C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF328`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xF3AC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x70`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1058`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF22C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xF3EF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x71`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1029`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF22C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF3E3`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0xF43A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x72`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1060`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF432`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xF4B6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x73`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1068`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF432`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xF4F7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x74`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1070`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF432`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF4EB`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xF53A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x75`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1080`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF432`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF52E`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xF56F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x76`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1088`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF432`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF52E`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xF5B2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x77`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1090`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF432`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF5A6`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xF5F5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x78`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1061`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF432`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF5E9`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0xF640`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x79`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1098`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF638`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xF6BC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x7A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10A0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF638`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xF6FD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x7B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10A8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF638`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF6F1`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xF740`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x7C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10B8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF638`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF734`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xF775`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x7D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10C0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF638`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF734`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xF7B8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x7E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10C8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF638`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF7AC`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xF7FB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x7F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1099`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF638`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF7EF`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0xF846`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x80`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10D0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF83E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xF8C2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x81`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10D8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF83E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xF903`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x82`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10E0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF83E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF8F7`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xF946`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x83`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10F0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF83E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF93A`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xF97B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x84`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10F8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF83E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF93A`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xF9BE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x85`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1100`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF83E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF9B2`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xFA01`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x86`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x10D1`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xF83E`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF9F5`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0xFA4C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x87`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1108`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFA44`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xFAC8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x88`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1110`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFA44`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xFB09`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x89`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1118`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFA44`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFAFD`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xFB4C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x8A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1128`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFA44`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFB40`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xFB81`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x8B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1130`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFA44`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFB40`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xFBC4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x8C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1138`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFA44`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFBB8`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xFC07`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x8D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1109`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFA44`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFBFB`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0xFC52`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x8E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1140`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFC4A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xFCCE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x8F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1148`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFC4A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xFD0F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x90`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1150`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFC4A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFD03`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xFD52`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x91`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1160`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFC4A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFD46`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xFD87`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x92`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1168`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFC4A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFD46`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xFDCA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x93`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1170`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFC4A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFDBE`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0xFE0D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x94`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1141`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFC4A`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFE01`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0xFE58`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x95`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1178`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFE50`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0xFED4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x96`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1180`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFE50`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0xFF15`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x97`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1188`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFE50`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFF09`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0xFF58`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x98`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1198`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFE50`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFF4C`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0xFF8D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x99`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11A0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFE50`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFF4C`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0xFFD0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x9A`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11A8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFE50`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xFFC4`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0x10013`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0x9B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1179`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xFE50`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10007`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0x1005E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0x9C`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11B0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10056`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0x100DA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x9D`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11B8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10056`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0x1011B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x9E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11C0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10056`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1010F`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0x1015E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0x9F`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11D0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10056`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10152`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0x10193`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xA0`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11D8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10056`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10152`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0x101D6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xA1`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11E0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10056`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x101CA`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0x10219`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0xA2`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11B1`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10056`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1020D`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0x10264`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0xA3`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11E8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x1025C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0x102E0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xA4`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11F0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x1025C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0x10321`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xA5`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11F8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x1025C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10315`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0x10364`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xA6`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1208`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x1025C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10358`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0x10399`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xA7`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1210`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x1025C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10358`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0x103DC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xA8`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1218`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x1025C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x103D0`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0x1041F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0xA9`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x11E9`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x1025C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10413`: 0x1. Expression result: stock true; CMOS unlock true.

### Sensor Type

Type: `OneOf`. Offset: `0x1046A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Media temperature | 0 | none | none |
| Controller temperature | 1 | none | none |
| Spare capacity | 2 | none | none |
| Wear level | 3 | none | none |
| Unsafe shutdowns | 4 | none | none |
| Power on time | 5 | none | none |
| Up time | 6 | none | none |
| Power cycles | 7 | none | none |
| FW error count | 8 | none | none |
| Power limited | 9 | none | none |
| MediaErrorsUncorrected | 10 | none | none |
| MediaErrorsCorrected | 11 | none | none |
| MediaErrorsErasureCoded | 12 | none | none |
| MediaErrorsHost | 13 | none | none |
| MediaErrorsNonHost | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0xAA`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1220`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10462`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Value

Type: `Numeric`. Offset: `0x104E6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xAB`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1228`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10462`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Non-critical threshold

Type: `Numeric`. Offset: `0x10527`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xAC`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1230`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10462`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1051B`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical lower threshold

Type: `Numeric`. Offset: `0x1056A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xAD`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1240`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10462`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1055E`: 0x1. Expression result: stock true; CMOS unlock true.

### Critical upper threshold

Type: `Numeric`. Offset: `0x1059F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xAE`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1248`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10462`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1055E`: 0x1. Expression result: stock true; CMOS unlock true.

### Fatal threshold

Type: `Numeric`. Offset: `0x105E2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 64; Min: 0x0; Max: 0xFFFF; Step: 0x1.

Question ID: `0xAF`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1250`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10462`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x105D6`: 0x1. Expression result: stock true; CMOS unlock true.

### State

Type: `OneOf`. Offset: `0x10625`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | none | none |
| NonCritical | 1 | none | none |
| Critical | 2 | none | none |
| Fatal | 3 | none | none |
| Unknown | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0xB0`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1221`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE806`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10462`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10619`: 0x1. Expression result: stock true; CMOS unlock true.

### Current non-critical thresholds

Type: `Subtitle`. Offset: `0x10672`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1066A`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Controller temperature: different values on AEPs

Type: `Subtitle`. Offset: `0x10683`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1066A`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1067B`: (NVMDIMM_IFRDATA&#91;0x1259&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Controller temperature &#91;C&#93;

Type: `Numeric`. Offset: `0x10696`.

Firmware help: Controller temperature in Celsius

Access: Conditional; no CMOS vendor gate on this path; read-only flag.

Explicit static defaults: store 0x0: 20.

Size: 64; Min: 0x14; Max: 0x69; Step: 0x1.

Question ID: `0xB1`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF58`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1066A`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1068E`: (NVMDIMM_IFRDATA&#91;0x1259&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Media temperature: different values on AEPs

Type: `Subtitle`. Offset: `0x106D5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1066A`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x106CD`: (NVMDIMM_IFRDATA&#91;0x1258&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Media temperature &#91;C&#93;

Type: `Numeric`. Offset: `0x106E8`.

Firmware help: Media temperature in Celsius

Access: Conditional; no CMOS vendor gate on this path; read-only flag.

Explicit static defaults: store 0x0: 20.

Size: 64; Min: 0x14; Max: 0x55; Step: 0x1.

Question ID: `0xB2`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF20`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1066A`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x106E0`: (NVMDIMM_IFRDATA&#91;0x1258&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Spare capacity: different values on AEPs

Type: `Subtitle`. Offset: `0x10727`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1066A`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1071F`: (NVMDIMM_IFRDATA&#91;0x125A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Spare capacity &#91;%&#93;

Type: `Numeric`. Offset: `0x1073A`.

Firmware help: Spare capacity in percents

Access: Conditional; no CMOS vendor gate on this path; read-only flag.

Explicit static defaults: store 0x0: 1.

Size: 64; Min: 0x1; Max: 0x63; Step: 0x1.

Question ID: `0xB3`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF90`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1066A`: (NVMDIMM_IFRDATA&#91;0xF0A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10732`: (NVMDIMM_IFRDATA&#91;0x125A&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Modify non-critical thresholds

Type: `Subtitle`. Offset: `0x10784`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1077C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Controller temperature &#91;C&#93;

Type: `Numeric`. Offset: `0x1078D`.

Firmware help: Controller temperature in Celsius

Access: Conditional; no CMOS vendor gate on this path.

Explicit static defaults: store 0x0: 20.

Size: 64; Min: 0x14; Max: 0x69; Step: 0x1.

Question ID: `0xE604`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF60`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1077C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Media temperature &#91;C&#93;

Type: `Numeric`. Offset: `0x107C2`.

Firmware help: Media temperature in Celsius

Access: Conditional; no CMOS vendor gate on this path.

Explicit static defaults: store 0x0: 20.

Size: 64; Min: 0x14; Max: 0x55; Step: 0x1.

Question ID: `0xE603`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF28`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1077C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Spare capacity &#91;%&#93;

Type: `Numeric`. Offset: `0x107F7`.

Firmware help: Spare capacity in percents

Access: Conditional; no CMOS vendor gate on this path.

Explicit static defaults: store 0x0: 1.

Size: 64; Min: 0x1; Max: 0x63; Step: 0x1.

Question ID: `0xE605`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF98`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1077C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Apply changes

Type: `Action`. Offset: `0x10851`.

Firmware help: Apply changes

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xE606`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x10837`: (((NVMDIMM_IFRDATA&#91;0x1268&#93; == 0x0) and (NVMDIMM_IFRDATA&#91;0x1267&#93; == 0x0)) and (NVMDIMM_IFRDATA&#91;0x1269&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to AEP details

Type: `Ref`. Offset: `0x1086C`.

Firmware help: View AEP details

Opens: [AEP](5fbcd3def87d-0-fE3.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xB4`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10864`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### View AEPs

Type: `Ref`. Offset: `0x10885`.

Firmware help: View and configure installed AEPs.

Opens: [AEPs](5fbcd3def87d-0-fE2.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xB5`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1087D`: (NVMDIMM_IFRDATA&#91;0xF06&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Pools menu

Type: `Ref`. Offset: `0x1089E`.

Firmware help: View and configure AEPs pools

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xB6`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x10896`: (NVMDIMM_IFRDATA&#91;0xF08&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x108AF`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0xB7`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Action, Q0xE610)

Type: `Action`. Offset: `0x108BE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; read-only flag.

Question ID: `0xE610`. Question flags: `0x5` (read-only, callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
