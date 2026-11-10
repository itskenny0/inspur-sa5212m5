# BSSA Configuration Menu

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Memory Configuration &gt; BSSA Configuration Menu**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x58F`, PE/section offset `0x517E5`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Memory Configuration](c4ed43ec5ea4-0-f540.md) via BSSA Configuration Menu, offset `0x50AD2`.

## Controls and information

### BSSA Module Loader

Type: `OneOf`. Offset: `0x517F3`.

Firmware help: Enables loading the BSSA test module

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13CE`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xB6`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### BSSA Rank Margin Tool

Type: `OneOf`. Offset: `0x5181B`.

Firmware help: Enables the BSSA Rank Margin Tool

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13CF`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xB7`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### BSSA RMT on Fast Cold Boot

Type: `OneOf`. Offset: `0x51843`.

Firmware help: Enable/Disable the BSSA Rank Margin Tool on a Fast Cold Boot

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13D0`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xB8`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Per Bit Margining

Type: `OneOf`. Offset: `0x51877`.

Firmware help: Enable Per Bit Margining

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13D1`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xB9`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Display Tables

Type: `OneOf`. Offset: `0x5189F`.

Firmware help: Enable displaying results as tables

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13D2`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xBA`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Display Plots

Type: `OneOf`. Offset: `0x518C7`.

Firmware help: Enable the display of per-bit results as plots

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13D3`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xBB`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Loop Count

Type: `Numeric`. Offset: `0x518EF`.

Firmware help: Exponential loop count for single rank test

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 16; store 0x1: 16.

Size: 8; Min: 0x0; Max: 0x1F; Step: 0x0.

Question ID: `0x13D4`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xBC`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Backside Margining

Type: `OneOf`. Offset: `0x5190E`.

Firmware help: Enable margin test on the register or buffer backside

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13D5`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xBD`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Early Read ID Margining

Type: `OneOf`. Offset: `0x51936`.

Firmware help: Enable NVMDIMM Early Read ID test

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13D6`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xBE`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Step Size Override

Type: `OneOf`. Offset: `0x5195E`.

Firmware help: Enable overriding the default step sizes

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Enabled | 1 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13D7`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xBF`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### RxDqs

Type: `OneOf`. Offset: `0x5198E`.

Firmware help: Step size of RxDqs. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13D8`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC0`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### RxVref

Type: `OneOf`. Offset: `0x519C4`.

Firmware help: Step size of RxVref. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13D9`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC1`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### TxDq

Type: `OneOf`. Offset: `0x519FA`.

Firmware help: Step size of TxDq. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13DA`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC2`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### TxVref

Type: `OneOf`. Offset: `0x51A30`.

Firmware help: Step size of TxVref. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13DB`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC3`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CmdAll

Type: `OneOf`. Offset: `0x51A66`.

Firmware help: Step size of CmdAll. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13DC`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC4`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CmdVref

Type: `OneOf`. Offset: `0x51A9C`.

Firmware help: Step size of CmdVref. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13DD`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC5`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CtlAll

Type: `OneOf`. Offset: `0x51AD2`.

Firmware help: Step size of CtlAll. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13DE`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC6`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### EridDelay

Type: `OneOf`. Offset: `0x51B08`.

Firmware help: Step size of EridDelay. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13DF`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC7`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### EridVref

Type: `OneOf`. Offset: `0x51B3E`.

Firmware help: Step size of EridVref. Auto: 1. Supported values: 1,2,4,8

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| 1 | 1 | none | none |
| 2 | 2 | none | none |
| 4 | 4 | none | none |
| 8 | 8 | none | none |

Size: 8; Min: 0x1; Max: 0x8; Step: 0x0.

Question ID: `0x13E0`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC8`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51986`: (SocketMemoryConfig&#91;0xBF&#93; (Step Size Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### RMT Debug Messages

Type: `OneOf`. Offset: `0x51B76`.

Firmware help: Enables the BSSA RMT debug messages

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 9 | standard, manufacturing | none |
| Enabled | 5 | none | none |
| Disabled | 2 | none | none |

Size: 8; Min: 0x2; Max: 0x9; Step: 0x0.

Question ID: `0x13E1`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xC9`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50ABB`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x517EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5186B`: SocketMemoryConfig&#91;0xB7&#93; (BSSA Rank Margin Tool) in &#91;0, 2&#93;. Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
