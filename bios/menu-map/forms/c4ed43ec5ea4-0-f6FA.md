# Socket 2 Dfx PcieBr2D00F0 - Port 2A

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Socket 2 Dfx PcieBr2D00F0 - Port 2A**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6FA`, PE/section offset `0x19E9B`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Incoming references

- [Socket2 Configuration](c4ed43ec5ea4-0-f721.md) via Socket 2 Dfx PcieBr2D00F0 - Port 2A, offset `0x11D0A`.

## Controls and information

### Socket 2 Dfx PcieBr2D00F0 - Port 2A

Type: `Subtitle`. Offset: `0x19EA1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### Gen3 Override mode

Type: `OneOf`. Offset: `0x19EC4`.

Firmware help: Set specific overrides in Gen3 features

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| UniPhy | 0 | standard, manufacturing | none |
| Manual | 1 | none | none |
| Test Card | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x598`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x11CC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Precursor

Type: `Numeric`. Offset: `0x19EF8`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x599`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1274`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x19EEC`: Not((SocketIioConfig&#91;0x11CC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Cursor

Type: `Numeric`. Offset: `0x19F17`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 41; store 0x1: 41.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x59A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x12C8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x19EEC`: Not((SocketIioConfig&#91;0x11CC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Postcursor

Type: `Numeric`. Offset: `0x19F36`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x59B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x131C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x19EEC`: Not((SocketIioConfig&#91;0x11CC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Postcursor

Type: `Numeric`. Offset: `0x19F55`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x59C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1370`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x19EEC`: Not((SocketIioConfig&#91;0x11CC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Cursor

Type: `Numeric`. Offset: `0x19F74`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 41; store 0x1: 41.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x59D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x13C4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x19EEC`: Not((SocketIioConfig&#91;0x11CC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Postcursor

Type: `Numeric`. Offset: `0x19F93`.

Firmware help: Override GEN3PRIVTXEQ register

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x59E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1418`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x19EEC`: Not((SocketIioConfig&#91;0x11CC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Gen3 NTB Test Card

Type: `OneOf`. Offset: `0x19FC0`.

Firmware help: Execute Gen3 Phase2 for NTB PCIe Test Cards

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| LAGUNA | 0 | standard, manufacturing | none |
| NTB | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x59F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1220`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x19FB4`: Not((SocketIioConfig&#91;0x11CC&#93; (Gen3 Override mode) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Preset Settings

Type: `Subtitle`. Offset: `0x19FEC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DN Tx Preset

Type: `OneOf`. Offset: `0x19FFE`.

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

Question ID: `0x5A0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x146C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DN Rx Preset Hint

Type: `OneOf`. Offset: `0x1A05E`.

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

Question ID: `0x5A1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x14C0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### UP Rx Preset

Type: `OneOf`. Offset: `0x1A0A9`.

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

Question ID: `0x5A2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1514`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Miscellaneous Configuration

Type: `Subtitle`. Offset: `0x1A112`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Inbound Configuration

Type: `OneOf`. Offset: `0x1A124`.

Firmware help: Enable Inbound configuration

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x5A3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1568`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x19EBC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
