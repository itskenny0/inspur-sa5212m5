# Memory Map

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Memory Configuration &gt; Memory Map**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x58A`, PE/section offset `0x512E1`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Memory Configuration](c4ed43ec5ea4-0-f540.md) via Memory Map, offset `0x50A8C`.

## Controls and information

### Volatile Memory Mode

Type: `OneOf`. Offset: `0x512EF`.

Firmware help: Selects whether 1LM or 2LM memory mode should be enabled

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 1LM | 0 | standard, manufacturing | none |
| 2LM | 1 | none | none |
| Auto | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13B1`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x3C`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x512E7`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### 1LM Memory Interleave Granularity

Type: `OneOf`. Offset: `0x5131F`.

Firmware help: Selects the 1LM memory interleave granularity

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| 256B Target, 256B Channel | 1 | none | none |
| 64B Target, 64B Channel | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13B2`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x3E`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x512E7`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51317`: (SocketMemoryConfig&#91;0x3C&#93; (Volatile Memory Mode) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IMC Interleaving

Type: `OneOf`. Offset: `0x51355`.

Firmware help: Select IMC Interleaving setting

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| 1-way Interleave | 1 | none | none |
| 2-way Interleave | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13B3`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x41`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x512E7`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51349`: Not((SocketCommonRcConfig&#91;0x9&#93; (NUMA Optimized) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Channel Interleaving

Type: `OneOf`. Offset: `0x5137F`.

Firmware help: Select Channel Interleaving setting

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| 1-way Interleave | 1 | none | none |
| 2-way Interleave | 2 | none | none |
| 3-way Interleave | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0x13B4`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x42`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x512E7`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Rank Interleaving

Type: `OneOf`. Offset: `0x513AE`.

Firmware help: Select Rank Interleaving setting

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| 1-way Interleave | 1 | none | none |
| 2-way Interleave | 2 | none | none |
| 4-way Interleave | 4 | none | none |
| 8-way Interleave | 8 | none | none |

Size: 8; Min: 0x0; Max: 0x8; Step: 0x0.

Question ID: `0x13B5`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x43`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x512E7`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket Interleave Below 4GB

Type: `OneOf`. Offset: `0x513E4`.

Firmware help: Splits the 0-4GB address space between two sockets, so that both sockets get a chunk of local memory below 4GB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13B6`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x29`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x512E7`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
