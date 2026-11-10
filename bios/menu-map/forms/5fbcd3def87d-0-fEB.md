# Namespace

[Menu index](../README.md) | [Module index](../5fbcd3def87d-0.md)

Path: **Intel DIMM Gen 1 Configuration &gt; Namespace**

Source: `5038E34E-0774-47A0-A5EF-4B94AF1A43DA`. Formset `47879403-C5B6-46C4-A8AE-14211AC697BE`, form `0xEB`, PE/section offset `0x11ADC`.

Root evidence: First declared form; runtime driver registration not verified.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Controls and information

### View details for or modify selected Namespace

Type: `Subtitle`. Offset: `0x11AE2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### UUID

Type: `String`. Offset: `0x11B00`.

Firmware help: Universally Unique IDentifier of Namespace

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

MinSize: 0x0; MaxSize: 0x24.

Question ID: `0x108`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11AF4`: 0x1. Expression result: stock true; CMOS unlock true.

### ID

Type: `String`. Offset: `0x11B20`.

Firmware help: Internal ID of Namespace

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

MinSize: 0x0; MaxSize: 0xE.

Question ID: `0x109`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11B14`: 0x1. Expression result: stock true; CMOS unlock true.

### Namespace type

Type: `OneOf`. Offset: `0x11B40`.

Firmware help: Storage Mode or App Direct Namespace

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Storage | 1 | none | none |
| App Direct | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x10A`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16C8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11B34`: 0x1. Expression result: stock true; CMOS unlock true.

### Name

Type: `String`. Offset: `0x11B63`.

Firmware help: Name of Namespace

Access: No active IFR hide condition on this path.

MinSize: 0x1; MaxSize: 0x3F.

Question ID: `0xEB30`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Pool

Type: `Numeric`. Offset: `0x11B8A`.

Firmware help: Pool related to Namespace

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

Explicit static defaults: store 0x0: 0.

Size: 32; Min: 0x0; Max: 0x7FFFFFFF; Step: 0x1.

Question ID: `0x10B`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16CC`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11B7E`: 0x1. Expression result: stock true; CMOS unlock true.

### Health

Type: `OneOf`. Offset: `0x11BBD`.

Firmware help: Namespace health state

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| OK | 0 | none | none |
| Degraded | 1 | none | none |
| Non-recoverable error | 2 | none | none |
| Broken mirror | 3 | none | none |

Size: 16; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0x10C`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16C6`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11BB1`: 0x1. Expression result: stock true; CMOS unlock true.

### Optimize

Type: `OneOf`. Offset: `0x11C01`.

Firmware help: Optimize the Copy On Write function on Namespace

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| CopyOnWrite | 1 | none | none |
| None | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x10D`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16CA`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11BF5`: 0x1. Expression result: stock true; CMOS unlock true.

### Block size &#91;Byte&#93;

Type: `Numeric`. Offset: `0x11C30`.

Firmware help: Size of single block &#91;Byte&#93;

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

Explicit static defaults: store 0x0: 1.

Size: 64; Min: 0x1; Max: 0x7FFFFFFF; Step: 0x1.

Question ID: `0x10E`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16D8`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11C24`: 0x1. Expression result: stock true; CMOS unlock true.

### Capacity type

Type: `OneOf`. Offset: `0x11C67`.

Firmware help: Block count or capacity

Access: No active IFR hide condition on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Block count | 1 | none | none |
| Capacity | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x10F`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16D0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

### Block count

Type: `Numeric`. Offset: `0x11CA0`.

Firmware help: Number of Namespace blocks

Access: Conditional; no CMOS vendor gate on this path.

Explicit static defaults: store 0x0: 1.

Size: 64; Min: 0x1; Max: 0x7FFFFFFF; Step: 0x1.

Question ID: `0x110`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16E0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x11C88`: NVMDIMM_IFRDATA&#91;0x16D0&#93; (Capacity type) in &#91;2, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11C94`: NVMDIMM_IFRDATA&#91;0x16C8&#93; (Namespace type) in &#91;2, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Block count

Type: `Numeric`. Offset: `0x11CEF`.

Firmware help: Number of Namespace blocks

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes; read-only flag.

Explicit static defaults: store 0x0: 1.

Size: 64; Min: 0x1; Max: 0x7FFFFFFF; Step: 0x1.

Question ID: `0x111`. Question flags: `0x1` (read-only).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16E0`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x11C88`: NVMDIMM_IFRDATA&#91;0x16D0&#93; (Capacity type) in &#91;2, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11CD7`: NVMDIMM_IFRDATA&#91;0x16C8&#93; (Namespace type) in &#91;1, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x11CE3`: 0x1. Expression result: stock true; CMOS unlock true.

### Units

Type: `OneOf`. Offset: `0x11D36`.

Firmware help: Change the units the namespace capacity is displayed in.

Access: Conditional; no CMOS vendor gate on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| GiB | 0 | none | none |
| GB | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEB1F`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16CB`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x11D2A`: NVMDIMM_IFRDATA&#91;0x16D0&#93; (Capacity type) in &#91;1, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Capacity

Type: `String`. Offset: `0x11D63`.

Firmware help: The size of the namespace. Units depends on the parameter 'Units'

Access: Conditional; no CMOS vendor gate on this path.

MinSize: 0x1; MaxSize: 0x27.

Question ID: `0xEB11`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x11D2A`: NVMDIMM_IFRDATA&#91;0x16D0&#93; (Capacity type) in &#91;1, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11D57`: NVMDIMM_IFRDATA&#91;0x16C8&#93; (Namespace type) in &#91;2, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Capacity

Type: `String`. Offset: `0x11D8F`.

Firmware help: The size of the namespace. Units depends on the parameter 'Units'

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

MinSize: 0x1; MaxSize: 0x27.

Question ID: `0x112`. Question flags: `0x4` (callback).

Storage: `NVMDIMM_IFRDATA` (no fixed byte offset in this record), GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x11D2A`: NVMDIMM_IFRDATA&#91;0x16D0&#93; (Capacity type) in &#91;1, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11D77`: NVMDIMM_IFRDATA&#91;0x16C8&#93; (Namespace type) in &#91;1, 0&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x11D83`: 0x1. Expression result: stock true; CMOS unlock true.

### Encryption

Type: `OneOf`. Offset: `0x11DB3`.

Firmware help: Encryption enabled state of the underlying AEP Dimms for the namespace

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 0 | 0 | none | none |
| 1 | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x113`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16EB`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11DA7`: 0x1. Expression result: stock true; CMOS unlock true.

### Erase capable

Type: `OneOf`. Offset: `0x11DE2`.

Firmware help: Erase Capability of the underlying AEP Dimms for the namespace

Access: No active IFR hide condition on this path; disabled after unlock: yes; read-only flag.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 0 | 0 | none | none |
| 1 | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x114`. Question flags: `0x5` (read-only, callback).

Storage: `NVMDIMM_IFRDATA` at byte offset `0x16EA`, GUID `47879403-C5B6-46C4-A8AE-14211AC697BE`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x11DD6`: 0x1. Expression result: stock true; CMOS unlock true.

### Save

Type: `Ref`. Offset: `0x11E0E`.

Firmware help: Save configuration of current Namespace

Opens: [Namespaces](5fbcd3def87d-0-fEA.md).

Access: No active IFR hide condition on this path.

Question ID: `0xEB0B`. Question flags: `0x4` (callback).

### Delete

Type: `Ref`. Offset: `0x11E1D`.

Firmware help: Delete current Namespace

Opens: [Namespaces](5fbcd3def87d-0-fEA.md).

Access: No active IFR hide condition on this path.

Question ID: `0xEB0C`. Question flags: `0x4` (callback).

### Back to Namespaces

Type: `Ref`. Offset: `0x11E2C`.

Firmware help: Display, create, modify and delete namespaces.

Opens: [Namespaces](5fbcd3def87d-0-fEA.md).

Access: No active IFR hide condition on this path.

Question ID: `0xEB14`. Question flags: `0x4` (callback).

### Back to Main menu

Type: `Ref`. Offset: `0x11E3B`.

Firmware help: Return to the Main menu

Opens: [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0-fE1.md).

Access: No active IFR hide condition on this path.

Question ID: `0x115`. Question flags: `0x0` (none of the decoded flags).

### (internal Action, Q0xEB10)

Type: `Action`. Offset: `0x11E4A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; read-only flag.

Question ID: `0xEB10`. Question flags: `0x5` (read-only, callback).
