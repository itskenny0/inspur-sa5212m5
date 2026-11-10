# Socket 3 Dfx PcieBr0D00F0 - Port 0

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Socket 3 Dfx PcieBr0D00F0 - Port 0**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x70A`, PE/section offset `0x1C97B`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Incoming references

- [Socket3 Configuration](c4ed43ec5ea4-0-f722.md) via Socket 3 Dfx PcieBr0D00F0 - Port 0, offset `0x11EA2`.

## Controls and information

### Socket 3 Dfx PcieBr0D00F0 - Port 0

Type: `Subtitle`. Offset: `0x1C981`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### Gen3 Override mode

Type: `OneOf`. Offset: `0x1C9A4`.

Firmware help: Set specific overrides in Gen3 features

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| UniPhy | 0 | standard, manufacturing | none |
| Manual | 1 | none | none |
| Test Card | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x658`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x11DC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Precursor

Type: `Numeric`. Offset: `0x1C9D8`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x659`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1284`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1C9CC`: Not((SocketIioConfig&#91;0x11DC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Cursor

Type: `Numeric`. Offset: `0x1C9F7`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 41; store 0x1: 41.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x65A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x12D8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1C9CC`: Not((SocketIioConfig&#91;0x11DC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Postcursor

Type: `Numeric`. Offset: `0x1CA16`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x65B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x132C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1C9CC`: Not((SocketIioConfig&#91;0x11DC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Postcursor

Type: `Numeric`. Offset: `0x1CA35`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x65C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1380`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1C9CC`: Not((SocketIioConfig&#91;0x11DC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Cursor

Type: `Numeric`. Offset: `0x1CA54`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 41; store 0x1: 41.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x65D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x13D4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1C9CC`: Not((SocketIioConfig&#91;0x11DC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Postcursor

Type: `Numeric`. Offset: `0x1CA73`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x65E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1428`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1C9CC`: Not((SocketIioConfig&#91;0x11DC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Gen3 NTB Test Card

Type: `OneOf`. Offset: `0x1CAA0`.

Firmware help: Execute Gen3 Phase2 for NTB PCIe Test Cards

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| LAGUNA | 0 | standard, manufacturing | none |
| NTB | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x65F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1230`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1CA94`: Not((SocketIioConfig&#91;0x11DC&#93; (Gen3 Override mode) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Preset Settings

Type: `Subtitle`. Offset: `0x1CACC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DN Tx Preset

Type: `OneOf`. Offset: `0x1CADE`.

Firmware help: PCIe Downstream Tx Preset

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 255 | standard, manufacturing | none |
| P0 (-6.0/0.0 dB) | 0 | none | none |
| P1 (-3.5/0.0 dB) | 1 | none | none |
| P2 (-4.5/0.0 dB) | 2 | none | none |
| P3 (-2.5/0.0 dB) | 3 | none | none |
| P4 ( 0.0/0.0 dB) | 4 | none | none |
| P5 ( 0.0/2.0 dB) | 5 | none | none |
| P6 ( 0.0/2.5 dB) | 6 | none | none |
| P7 (-6.0/3.5 dB) | 7 | none | none |
| P8 (-3.5/3.5 dB) | 8 | none | none |
| P9 ( 0.0/3.5 dB) | 9 | none | none |

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x660`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x147C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DN Rx Preset Hint

Type: `OneOf`. Offset: `0x1CB3E`.

Firmware help: PCIe Downstream Rx Preset Hint

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 255 | standard, manufacturing | none |
| P0 ( -6.0 dB) | 0 | none | none |
| P1 ( -7.0 dB) | 1 | none | none |
| P2 ( -8.0 dB) | 2 | none | none |
| P3 ( -9.0 dB) | 3 | none | none |
| P4 (-10.0 dB) | 4 | none | none |
| P5 (-11.0 dB) | 5 | none | none |
| P6 (-12.0 dB) | 6 | none | none |

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x661`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x14D0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### UP Rx Preset

Type: `OneOf`. Offset: `0x1CB89`.

Firmware help: PCIe Upstream Tx Preset

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 255 | standard, manufacturing | none |
| P0 (-6.0/0.0 dB) | 0 | none | none |
| P1 (-3.5/0.0 dB) | 1 | none | none |
| P2 (-4.5/0.0 dB) | 2 | none | none |
| P3 (-2.5/0.0 dB) | 3 | none | none |
| P4 ( 0.0/0.0 dB) | 4 | none | none |
| P5 ( 0.0/2.0 dB) | 5 | none | none |
| P6 ( 0.0/2.5 dB) | 6 | none | none |
| P7 (-6.0/3.5 dB) | 7 | none | none |
| P8 (-3.5/3.5 dB) | 8 | none | none |
| P9 ( 0.0/3.5 dB) | 9 | none | none |

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x662`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1524`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Miscellaneous Configuration

Type: `Subtitle`. Offset: `0x1CBF2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Inbound Configuration

Type: `OneOf`. Offset: `0x1CC04`.

Firmware help: Enable Inbound configuration

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x663`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1578`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x1C99C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
