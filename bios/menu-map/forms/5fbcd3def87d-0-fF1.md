# Create goal config

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Pools &gt; Create goal config**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xF1`, PE/section offset `0x11338`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Pools](5fbcd3def87d-0-fE8.md) via Create goal config, offset `0x110D0`.

## Controls and information

### Select the scope of the new Pool then set the desired sizes.

Type: `Subtitle`. Offset: `0x1133E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Create goal config for:

Type: `OneOf`. Offset: `0x1135C`.

Firmware help: Select target to create goal config

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Platform | 0 | none | none |
| Socket | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xE1`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xD90`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11350`: Not((NVMDIMM_IFRDATA&#91;0xED0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Create goal config for:

Type: `OneOf`. Offset: `0x11387`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Platform | 0 | none | none |
| Socket | 1 | none | none |
| Unconfigured AEPs | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0xE2`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xD90`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1137F`: (NVMDIMM_IFRDATA&#91;0xED0&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Memory Mode:

Type: `OneOf`. Offset: `0x1142A`.

Firmware help: Enter the Memory Mode size or use whole remaining capacity

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| None | 0 | none | none |
| Manual | 2 | none | none |
| Remaining | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0xE3`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEEE`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Memory Mode capacity is unusable with the currently selected platform BIOS volatile mode.

Type: `Subtitle`. Offset: `0x11464`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11452`: ((NVMDIMM_IFRDATA&#91;0xEEE&#93; (Memory Mode:) == 0x0) or (NVMDIMM_IFRDATA&#91;0xEF8&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Memory Mode Capacity:

Type: `Numeric`. Offset: `0x1147B`.

Firmware help: Set Memory Mode capacity in gibibytes. Due to platform memory alignment requirements, the capacity will be aligned automatically.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 1.

Size: 64; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x1.

Question ID: `0xE4`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEF0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1146F`: Not((NVMDIMM_IFRDATA&#91;0xEEE&#93; (Memory Mode:) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Number of pools:

Type: `OneOf`. Offset: `0x114B2`.

Firmware help: Select number of pools

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 0 | 0 | none | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0xE5`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xD91`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #1 size type:

Type: `OneOf`. Offset: `0x114EB`.

Firmware help: Provide App Direct size in gibibytes. Due to platform memory alignment requirements, the capacity will be aligned automatically.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Remaining | 0 | none | none |
| Manual | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xE6`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xED4`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x114E3`: (NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #1 size:

Type: `Numeric`. Offset: `0x11518`.

Firmware help: Provide App Direct size in gibibytes. Due to platform memory alignment requirements, the capacity will be aligned automatically.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Size: 64; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x1.

Question ID: `0xE7`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xED8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x114E3`: (NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1150C`: Not((NVMDIMM_IFRDATA&#91;0xED4&#93; (App Direct #1 size type:) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #1 type:

Type: `OneOf`. Offset: `0x11542`.

Firmware help: Select App Direct type

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Non-interleaved | 2 | none | none |
| Interleaved | 1 | none | none |
| Mirrored | 3 | none | none |

Size: 8; Min: 0x1; Max: 0x3; Step: 0x0.

Question ID: `0xE8`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEE8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x114E3`: (NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #1 iMc interleave size:

Type: `OneOf`. Offset: `0x1156A`.

Firmware help: Select interleave size

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Recommended | 0 | none | none |
| 64 B | 1 | none | none |
| 128 B | 2 | none | none |
| 256 B | 4 | none | none |
| 4 kB | 64 | none | none |
| 1 GB | 128 | none | none |

Size: 8; Min: 0x0; Max: 0x80; Step: 0x0.

Question ID: `0xE9`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEEA`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x114E3`: (NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #1 channel interleave size:

Type: `OneOf`. Offset: `0x115A7`.

Firmware help: Select channel interleave size

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Recommended | 0 | none | none |
| 64 B | 1 | none | none |
| 128 B | 2 | none | none |
| 256 B | 4 | none | none |
| 4 kB | 64 | none | none |
| 1 GB | 128 | none | none |

Size: 8; Min: 0x0; Max: 0x80; Step: 0x0.

Question ID: `0xEA`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEEC`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x114E3`: (NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #2 size type:

Type: `OneOf`. Offset: `0x115FB`.

Firmware help: Provide App Direct size in gibibytes. Due to platform memory alignment requirements, the capacity will be aligned automatically.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Remaining | 0 | none | none |
| Manual | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEB`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xED5`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x115E6`: Not((NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #2 size:

Type: `Numeric`. Offset: `0x11628`.

Firmware help: Provide App Direct size in gibibytes. Due to platform memory alignment requirements, the capacity will be aligned automatically.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Size: 64; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x1.

Question ID: `0xEC`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEE0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x115E6`: Not((NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1161C`: Not((NVMDIMM_IFRDATA&#91;0xED5&#93; (App Direct #2 size type:) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #2 type:

Type: `OneOf`. Offset: `0x11652`.

Firmware help: Select App Direct type

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Non-interleaved | 2 | none | none |
| Interleaved | 1 | none | none |
| Mirrored | 3 | none | none |

Size: 8; Min: 0x1; Max: 0x3; Step: 0x0.

Question ID: `0xED`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEE9`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x115E6`: Not((NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #2 iMc interleave size:

Type: `OneOf`. Offset: `0x1167A`.

Firmware help: Select interleave size

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Recommended | 0 | none | none |
| 64 B | 1 | none | none |
| 128 B | 2 | none | none |
| 256 B | 4 | none | none |
| 4 kB | 64 | none | none |
| 1 GB | 128 | none | none |

Size: 8; Min: 0x0; Max: 0x80; Step: 0x0.

Question ID: `0xEE`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEEB`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x115E6`: Not((NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### App Direct #2 channel interleave size:

Type: `OneOf`. Offset: `0x116B7`.

Firmware help: Select channel interleave size

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Recommended | 0 | none | none |
| 64 B | 1 | none | none |
| 128 B | 2 | none | none |
| 256 B | 4 | none | none |
| 4 kB | 64 | none | none |
| 1 GB | 128 | none | none |

Size: 8; Min: 0x0; Max: 0x80; Step: 0x0.

Question ID: `0xEF`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0xEED`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x115E6`: Not((NVMDIMM_IFRDATA&#91;0xD91&#93; (Number of pools:) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Create goal config

Type: `Ref`. Offset: `0x116FF`.

Firmware help: Create goal config on selected target

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF107`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to AEP details

Type: `Ref`. Offset: `0x11716`.

Firmware help: View AEP details

Opens: [AEP](5fbcd3def87d-0-fE3.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF0`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1170E`: (NVMDIMM_IFRDATA&#91;0xF07&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### View AEPs

Type: `Ref`. Offset: `0x1172F`.

Firmware help: View and configure installed AEPs.

Opens: [AEPs](5fbcd3def87d-0-fE2.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF1`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11727`: (NVMDIMM_IFRDATA&#91;0xF06&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Pools menu

Type: `Ref`. Offset: `0x11748`.

Firmware help: View and configure AEPs pools

Opens: [Pools](5fbcd3def87d-0-fE8.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF2`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11740`: (NVMDIMM_IFRDATA&#91;0xF08&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Back to Main menu

Type: `Ref`. Offset: `0x11759`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Question ID: `0xF3`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0xDF77`: (NVMDIMM_IFRDATA&#91;0x0&#93; (Detected AEPs:) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xE02C`: (NVMDIMM_IFRDATA&#91;0x1512&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

## Runtime insertion labels

The firmware may add controls or device names here. They cannot be fully enumerated from the static forms.

- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x7
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x8
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0x9
- Guid Guid: 0F0B1735-87A0-4193-B266-538C38AF48CE, ExtendedOpCode: Label, LabelNumber: 0xA
