# Socket 0 Dfx PcieBr4D02F0 - MCP 0

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; IIO DFX Configuration &gt; Socket0 Configuration &gt; Socket 0 Dfx PcieBr4D01F0 - MCP 0**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6DA`, PE/section offset `0x148DB`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Socket0 Configuration](c4ed43ec5ea4-0-f71F.md) via Socket 0 Dfx PcieBr4D01F0 - MCP 0, offset `0x119DA`.

## Controls and information

### Socket 0 Dfx PcieBr4D02F0 - MCP 0

Type: `Subtitle`. Offset: `0x148E1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Gen3 Override mode

Type: `OneOf`. Offset: `0x14904`.

Firmware help: Set specific overrides in Gen3 features

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| UniPhy | 0 | standard, manufacturing | none |
| Manual | 1 | none | none |
| Test Card | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x418`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x11AC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Precursor

Type: `Numeric`. Offset: `0x14938`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x419`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1254`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1492C`: Not((SocketIioConfig&#91;0x11AC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Cursor

Type: `Numeric`. Offset: `0x14957`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 41; store 0x1: 41.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x41A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x12A8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1492C`: Not((SocketIioConfig&#91;0x11AC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Postcursor

Type: `Numeric`. Offset: `0x14976`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x41B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x12FC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1492C`: Not((SocketIioConfig&#91;0x11AC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Postcursor

Type: `Numeric`. Offset: `0x14995`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x41C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1350`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1492C`: Not((SocketIioConfig&#91;0x11AC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Cursor

Type: `Numeric`. Offset: `0x149B4`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 41; store 0x1: 41.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x41D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x13A4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1492C`: Not((SocketIioConfig&#91;0x11AC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Postcursor

Type: `Numeric`. Offset: `0x149D3`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x41E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x13F8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1492C`: Not((SocketIioConfig&#91;0x11AC&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Gen3 NTB Test Card

Type: `OneOf`. Offset: `0x14A00`.

Firmware help: Execute Gen3 Phase2 for NTB PCIe Test Cards

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| LAGUNA | 0 | standard, manufacturing | none |
| NTB | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x41F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1200`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x149F4`: Not((SocketIioConfig&#91;0x11AC&#93; (Gen3 Override mode) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Preset Settings

Type: `Subtitle`. Offset: `0x14A2C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DN Tx Preset

Type: `OneOf`. Offset: `0x14A3E`.

Firmware help: PCIe Downstream Tx Preset

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

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

Question ID: `0x420`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x144C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DN Rx Preset Hint

Type: `OneOf`. Offset: `0x14A9E`.

Firmware help: PCIe Downstream Rx Preset Hint

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

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

Question ID: `0x421`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x14A0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### UP Rx Preset

Type: `OneOf`. Offset: `0x14AE9`.

Firmware help: PCIe Upstream Tx Preset

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

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

Question ID: `0x422`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x14F4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Miscellaneous Configuration

Type: `Subtitle`. Offset: `0x14B52`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Inbound Configuration

Type: `OneOf`. Offset: `0x14B64`.

Firmware help: Enable Inbound configuration

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x423`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1548`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x148FC`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
