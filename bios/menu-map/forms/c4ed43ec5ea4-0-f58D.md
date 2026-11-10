# Memory Dfx Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Memory Configuration &gt; Memory Dfx Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x58D`, PE/section offset `0x5207F`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Memory Configuration](c4ed43ec5ea4-0-f540.md) via Memory Dfx Configuration, offset `0x50AC3`.

## Controls and information

### Memory Dfx Configuration

Type: `Subtitle`. Offset: `0x52085`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### DIMM Management

Type: `OneOf`. Offset: `0x5209F`.

Firmware help: Selects whether BIOS Setup or the NGN DIMM Management Driver will control the NVMDIMMs.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| BIOS Setup | 0 | none | none |
| NGN DIMM Management Driver | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13FB`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x2A`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Load NGN DIMM Management Drivers

Type: `OneOf`. Offset: `0x520C7`.

Firmware help: Enable/Disable to load the NGN DIMM Management Drivers for NVMDIMMs(install the gNfitBindingProtocolGuid).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13FC`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x120`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Persistent Memory Mode

Type: `OneOf`. Offset: `0x520F7`.

Firmware help: Selects whether Persistent memory mode should be enabled.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13FD`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x3D`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x520EF`: (SocketMemoryConfig&#91;0x2A&#93; (DIMM Management) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Memory Interleaving

Type: `OneOf`. Offset: `0x52129`.

Firmware help: Maximum Node Interleave (1,2,4-way)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| NUMA (1-way) Node Interleave | 1 | none | none |
| 2-way Node Interleave | 2 | none | none |
| 4-way Node Interleave | 4 | none | none |

Size: 8; Min: 0x1; Max: 0x4; Step: 0x0.

Question ID: `0x13FE`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x0`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x52121`: (SocketCommonRcConfig&#91;0x9&#93; (NUMA Optimized) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### NVMDIMM Partitioning

Type: `OneOf`. Offset: `0x52162`.

Firmware help: Enable NVMDIMM partitioning.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13FF`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x2B`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5215A`: (SocketMemoryConfig&#91;0x2A&#93; (DIMM Management) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S0 MC0 Partition Ratio

Type: `OneOf`. Offset: `0x52195`.

Firmware help: Partition ratios of VOL, PMEM and BLK region for NVMDIMMs in Socket0 MC0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| VOL:20% PMEM:80% BLK:0% | 0 | none | none |
| VOL:80% PMEM:20% BLK:0% | 1 | none | none |
| VOL:50% PMEM:50% BLK:0% | 2 | none | none |
| VOL:60% PMEM:0% BLK:40% | 3 | none | none |
| VOL:40% PMEM:10% BLK:50% | 4 | standard, manufacturing | none |
| VOL:0% PMEM:40% BLK:60% | 5 | none | none |
| VOL:0% PMEM:30% BLK:70% | 6 | none | none |
| VOL:100% PMEM:0% BLK:0% | 7 | none | none |
| VOL:0% PMEM:100% BLK:0% | 8 | none | none |
| VOL:0% PMEM:0% BLK:100% | 9 | none | none |
| VOL:30% PMEM:60% BLK:10% | 10 | none | none |
| VOL:70% PMEM:0% BLK:30% | 11 | none | none |

Size: 8; Min: 0x0; Max: 0xB; Step: 0x0.

Question ID: `0x1400`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x2C`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x52185`: (SocketMemoryConfig&#91;0x2A&#93; (DIMM Management) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x5218D`: (SocketMemoryConfig&#91;0x2B&#93; (NVMDIMM Partitioning) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S0 MC1 Partition Ratio

Type: `OneOf`. Offset: `0x52210`.

Firmware help: Partition ratios of VOL, PMEM and BLK region for NVMDIMMs in Socket0 MC1

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| VOL:20% PMEM:80% BLK:0% | 0 | none | none |
| VOL:80% PMEM:20% BLK:0% | 1 | none | none |
| VOL:50% PMEM:50% BLK:0% | 2 | none | none |
| VOL:60% PMEM:0% BLK:40% | 3 | none | none |
| VOL:40% PMEM:10% BLK:50% | 4 | standard, manufacturing | none |
| VOL:0% PMEM:40% BLK:60% | 5 | none | none |
| VOL:0% PMEM:30% BLK:70% | 6 | none | none |
| VOL:100% PMEM:0% BLK:0% | 7 | none | none |
| VOL:0% PMEM:100% BLK:0% | 8 | none | none |
| VOL:0% PMEM:0% BLK:100% | 9 | none | none |
| VOL:30% PMEM:60% BLK:10% | 10 | none | none |
| VOL:70% PMEM:0% BLK:30% | 11 | none | none |

Size: 8; Min: 0x0; Max: 0xB; Step: 0x0.

Question ID: `0x1401`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x2D`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x52200`: (SocketMemoryConfig&#91;0x2A&#93; (DIMM Management) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x52208`: (SocketMemoryConfig&#91;0x2B&#93; (NVMDIMM Partitioning) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S1 MC0 Partition Ratio

Type: `OneOf`. Offset: `0x5228B`.

Firmware help: Partition ratios of VOL, PMEM and BLK region for NVMDIMMs in Socket1 MC0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| VOL:20% PMEM:80% BLK:0% | 0 | none | none |
| VOL:80% PMEM:20% BLK:0% | 1 | none | none |
| VOL:50% PMEM:50% BLK:0% | 2 | none | none |
| VOL:60% PMEM:0% BLK:40% | 3 | none | none |
| VOL:40% PMEM:10% BLK:50% | 4 | standard, manufacturing | none |
| VOL:0% PMEM:40% BLK:60% | 5 | none | none |
| VOL:0% PMEM:30% BLK:70% | 6 | none | none |
| VOL:100% PMEM:0% BLK:0% | 7 | none | none |
| VOL:0% PMEM:100% BLK:0% | 8 | none | none |
| VOL:0% PMEM:0% BLK:100% | 9 | none | none |
| VOL:30% PMEM:60% BLK:10% | 10 | none | none |
| VOL:70% PMEM:0% BLK:30% | 11 | none | none |

Size: 8; Min: 0x0; Max: 0xB; Step: 0x0.

Question ID: `0x1402`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x2E`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5227B`: (SocketMemoryConfig&#91;0x2A&#93; (DIMM Management) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x52283`: (SocketMemoryConfig&#91;0x2B&#93; (NVMDIMM Partitioning) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S1 MC1 Partition Ratio

Type: `OneOf`. Offset: `0x52306`.

Firmware help: Partition ratios of VOL, PMEM and BLK region for NVMDIMMs in Socket1 MC1

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| VOL:20% PMEM:80% BLK:0% | 0 | none | none |
| VOL:80% PMEM:20% BLK:0% | 1 | none | none |
| VOL:50% PMEM:50% BLK:0% | 2 | none | none |
| VOL:60% PMEM:0% BLK:40% | 3 | none | none |
| VOL:40% PMEM:10% BLK:50% | 4 | standard, manufacturing | none |
| VOL:0% PMEM:40% BLK:60% | 5 | none | none |
| VOL:0% PMEM:30% BLK:70% | 6 | none | none |
| VOL:100% PMEM:0% BLK:0% | 7 | none | none |
| VOL:0% PMEM:100% BLK:0% | 8 | none | none |
| VOL:0% PMEM:0% BLK:100% | 9 | none | none |
| VOL:30% PMEM:60% BLK:10% | 10 | none | none |
| VOL:70% PMEM:0% BLK:30% | 11 | none | none |

Size: 8; Min: 0x0; Max: 0xB; Step: 0x0.

Question ID: `0x1403`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x2F`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x522F6`: (SocketMemoryConfig&#91;0x2A&#93; (DIMM Management) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x522FE`: (SocketMemoryConfig&#91;0x2B&#93; (NVMDIMM Partitioning) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### High Address Region

Type: `OneOf`. Offset: `0x52371`.

Firmware help: High Address Region starting bit position. Auto - 0 (not enabled). Note that the actual start of the region is 2**N - 64MB, where N is the selected bit position.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Bit Position 33 | 33 | none | none |
| Bit Position 34 | 34 | none | none |
| Bit Position 35 | 35 | none | none |
| Bit Position 36 | 36 | none | none |
| Bit Position 37 | 37 | none | none |
| Bit Position 38 | 38 | none | none |
| Bit Position 39 | 39 | none | none |
| Bit Position 40 | 40 | none | none |
| Bit Position 41 | 41 | none | none |
| Bit Position 42 | 42 | none | none |
| Bit Position 43 | 43 | none | none |
| Bit Position 44 | 44 | none | none |
| Bit Position 45 | 45 | none | none |

Size: 8; Min: 0x0; Max: 0x2D; Step: 0x0.

Question ID: `0x1404`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xDE`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Low Mem Channel Config

Type: `OneOf`. Offset: `0x523E6`.

Firmware help: Select Channel for low memory, Auto - 0 (BIOS select)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Channel 0 | 1 | none | none |
| Channel 1 | 2 | none | none |
| Channel 2 | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0x1405`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xDD`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Configuration Mask for 2LM

Type: `OneOf`. Offset: `0x5241D`.

Firmware help: Selects the mask type to use for 2LM configurations

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Normal | 0 | standard, manufacturing | none |
| Aggressive | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1406`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x40`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x52415`: (SocketMemoryConfig&#91;0x3C&#93; (Volatile Memory Mode) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CR Halt/Warn Mixed SKU

Type: `OneOf`. Offset: `0x52440`.

Firmware help: Enable will raise Fatal error and halt the system; Disable will log warning and continue booting to shell/OS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1407`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x122`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### ECC Support

Type: `OneOf`. Offset: `0x52468`.

Firmware help: Enable - Enables DDR ECC Support. Disable - Disables this feature.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1408`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x28`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x52097`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
