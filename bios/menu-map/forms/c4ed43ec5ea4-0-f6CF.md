# Socket 0 Dfx PcieBr1D03F0 - Port 1D

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; IIO DFX Configuration &gt; Socket0 Configuration &gt; Socket 0 Dfx PcieBr1D03F0 - Port 1D**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6CF`, PE/section offset `0x12B61`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Socket0 Configuration](c4ed43ec5ea4-0-f71F.md) via Socket 0 Dfx PcieBr1D03F0 - Port 1D, offset `0x118C7`.

## Controls and information

### Socket 0 Dfx PcieBr1D03F0 - Port 1D

Type: `Subtitle`. Offset: `0x12B67`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Gen3 Override mode

Type: `OneOf`. Offset: `0x12B8A`.

Firmware help: Set specific overrides in Gen3 features

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| UniPhy | 0 | standard, manufacturing | none |
| Manual | 1 | none | none |
| Test Card | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x394`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x11A1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Precursor

Type: `Numeric`. Offset: `0x12BBE`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x395`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1249`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x12BB2`: Not((SocketIioConfig&#91;0x11A1&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Cursor

Type: `Numeric`. Offset: `0x12BDD`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 41; store 0x1: 41.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x396`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x129D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x12BB2`: Not((SocketIioConfig&#91;0x11A1&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph2 TxEq Postcursor

Type: `Numeric`. Offset: `0x12BFC`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x397`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x12F1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x12BB2`: Not((SocketIioConfig&#91;0x11A1&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Postcursor

Type: `Numeric`. Offset: `0x12C1B`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x398`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1345`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x12BB2`: Not((SocketIioConfig&#91;0x11A1&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Cursor

Type: `Numeric`. Offset: `0x12C3A`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 41; store 0x1: 41.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x399`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1399`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x12BB2`: Not((SocketIioConfig&#91;0x11A1&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ph3 TxEq Postcursor

Type: `Numeric`. Offset: `0x12C59`.

Firmware help: Override GEN3PRIVTXEQ register

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 11; store 0x1: 11.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x1.

Question ID: `0x39A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x13ED`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x12BB2`: Not((SocketIioConfig&#91;0x11A1&#93; (Gen3 Override mode) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Gen3 NTB Test Card

Type: `OneOf`. Offset: `0x12C86`.

Firmware help: Execute Gen3 Phase2 for NTB PCIe Test Cards

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| LAGUNA | 0 | standard, manufacturing | none |
| NTB | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x39B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x11F5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x12C7A`: Not((SocketIioConfig&#91;0x11A1&#93; (Gen3 Override mode) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Preset Settings

Type: `Subtitle`. Offset: `0x12CB2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DN Tx Preset

Type: `OneOf`. Offset: `0x12CC4`.

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

Question ID: `0x39C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1441`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DN Rx Preset Hint

Type: `OneOf`. Offset: `0x12D24`.

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

Question ID: `0x39D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1495`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### UP Rx Preset

Type: `OneOf`. Offset: `0x12D6F`.

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

Question ID: `0x39E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x14E9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Miscellaneous Configuration

Type: `Subtitle`. Offset: `0x12DD8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Inbound Configuration

Type: `OneOf`. Offset: `0x12DEA`.

Firmware help: Enable Inbound configuration

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x39F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x153D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x12B82`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
