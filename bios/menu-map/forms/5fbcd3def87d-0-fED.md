# Create Namespace

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Namespaces &gt; Create Namespace**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xED`, PE/section offset `0x11E5D`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Namespaces](5fbcd3def87d-0-fEA.md) via Create Namespace, offset `0x11ABC`.

## Controls and information

### Create Namespace

Type: `Subtitle`. Offset: `0x11E63`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No pools defined in system. To create Namespace a pool id is required.

Type: `Subtitle`. Offset: `0x11E76`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E6C`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Name

Type: `String`. Offset: `0x11E8B`.

Firmware help: Name of Namespace

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

MinSize: 0x1; MaxSize: 0x3F.

Question ID: `0x116`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Namespace type

Type: `OneOf`. Offset: `0x11EC7`.

Firmware help: Storage Mode or App Direct Namespace

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Storage | 1 | none | none |
| App Direct | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0xED21`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16C8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Optimize

Type: `OneOf`. Offset: `0x11EE8`.

Firmware help: Optimize the Copy On Write function on Namespace

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| CopyOnWrite | 1 | none | none |
| None | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x117`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16CA`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Erase capable

Type: `OneOf`. Offset: `0x11F09`.

Firmware help: Only use the AEP Dimms that support secure erase of their persistent data

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Ignore | 0 | none | none |
| Yes | 1 | none | none |
| No | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x118`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16E8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Encryption

Type: `OneOf`. Offset: `0x11F31`.

Firmware help: Only use the AEP Dimms that have encryption enabled

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Ignore | 0 | none | none |
| Yes | 1 | none | none |
| No | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x119`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16E9`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Block size &#91;Byte&#93;

Type: `OneOf`. Offset: `0x11F65`.

Firmware help: Size of single block &#91;Byte&#93;

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 512 B | 512 | none | none |
| 514 B | 514 | none | none |
| 520 B | 520 | none | none |
| 528 B | 528 | none | none |
| 4096 B | 4096 | none | none |
| 4112 B | 4112 | none | none |
| 4160 B | 4160 | none | none |
| 4224 B | 4224 | none | none |

Size: 64; Min: 0x200; Max: 0x1080; Step: 0x0.

Question ID: `0x11A`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16D8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11F59`: NVMDIMM_IFRDATA&#91;0x16C8&#93; (Namespace type) in &#91;2, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Block size &#91;Byte&#93;

Type: `OneOf`. Offset: `0x1200B`.

Firmware help: Size of single block &#91;Byte&#93;

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 1 B | 1 | none | none |

Size: 64; Min: 0x1; Max: 0x1; Step: 0x0.

Question ID: `0x11B`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16D8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11FFF`: NVMDIMM_IFRDATA&#91;0x16C8&#93; (Namespace type) in &#91;1, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Capacity type

Type: `OneOf`. Offset: `0x12043`.

Firmware help: Block count or capacity

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Block count | 1 | none | none |
| Capacity | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x11C`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16D0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Block count

Type: `Numeric`. Offset: `0x12070`.

Firmware help: Number of Namespace blocks

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 1.

Size: 64; Min: 0x1; Max: 0x7FFFFFFF; Step: 0x1.

Question ID: `0x11D`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16E0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x12064`: NVMDIMM_IFRDATA&#91;0x16D0&#93; (Capacity type) in &#91;2, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Capacity &#91;GB&#93;

Type: `String`. Offset: `0x120B3`.

Firmware help: The size of the namespace in Gigabytes.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

MinSize: 0x1; MaxSize: 0x27.

Question ID: `0xED11`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11E81`: NVMDIMM_IFRDATA&#91;0x16EC&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x120A7`: NVMDIMM_IFRDATA&#91;0x16D0&#93; (Capacity type) in &#91;1, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Create Namespace

Type: `Ref`. Offset: `0x120DC`.

Firmware help: Create Namespace using provided configuration

Opens: [Namespaces](5fbcd3def87d-0-fEA.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xED16`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x120D2`: NVMDIMM_IFRDATA&#91;0x16ED&#93; in &#91;1&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Namespaces

Type: `Ref`. Offset: `0x120ED`.

Firmware help: Display, create, modify and delete namespaces.

Opens: [Namespaces](5fbcd3def87d-0-fEA.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x11E`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x120FC`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0x11F`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Numeric, Q0x120)

Type: `Numeric`. Offset: `0x1210F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x120`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16ED`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x121)

Type: `Numeric`. Offset: `0x12122`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x121`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16EC`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x122)

Type: `Numeric`. Offset: `0x12135`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x122`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF08`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x123)

Type: `Numeric`. Offset: `0x12148`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x123`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF06`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x124)

Type: `Numeric`. Offset: `0x1215B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x124`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF07`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x125)

Type: `Numeric`. Offset: `0x1216E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x125`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1512`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x126)

Type: `Numeric`. Offset: `0x12181`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x126`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEF8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x127)

Type: `Numeric`. Offset: `0x12194`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x127`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xED0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x128)

Type: `Numeric`. Offset: `0x121B0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x128`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xC6C`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x129)

Type: `Numeric`. Offset: `0x121CC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x129`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x175E`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x12A)

Type: `Numeric`. Offset: `0x121DF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x12A`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x175D`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x12B)

Type: `Numeric`. Offset: `0x121F2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x12B`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xF0A`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x12C)

Type: `Numeric`. Offset: `0x12205`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x12C`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1277`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x12D)

Type: `Numeric`. Offset: `0x12218`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x12D`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x12BB`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x12E)

Type: `Numeric`. Offset: `0x1222B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 16; Min: 0x0; Max: 0xFFFF; Step: 0x0.

Question ID: `0x12E`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x552`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x12F)

Type: `Numeric`. Offset: `0x12241`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x12F`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1276`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x130)

Type: `Numeric`. Offset: `0x12254`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x130`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1513`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x131)

Type: `Numeric`. Offset: `0x12267`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x131`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1269`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x132)

Type: `Numeric`. Offset: `0x1227A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x132`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1267`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x133)

Type: `Numeric`. Offset: `0x1228D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x133`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1268`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x134)

Type: `Numeric`. Offset: `0x122A0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x134`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x125A`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x135)

Type: `Numeric`. Offset: `0x122B3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x135`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1258`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x136)

Type: `Numeric`. Offset: `0x122C6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x136`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1259`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x137)

Type: `Numeric`. Offset: `0x122D9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x137`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x175F`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x138)

Type: `Numeric`. Offset: `0x122EC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x138`. Question flags: `0x0` (none of the decoded flags).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x1510`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE045`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x1210B`: 0x1. Expression result: stock true; CMOS unlock true.

## Runtime insertion labels

The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.

- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0xF
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x10
