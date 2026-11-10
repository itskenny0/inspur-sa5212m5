# NGNVM DIMM Secure Erase Unit

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Memory Configuration &gt; NGN Configuration &gt; NGNVM DIMM Secure Erase Unit**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x58E`, PE/section offset `0x515AE`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [NGN Configuration](c4ed43ec5ea4-0-f58C.md) via NGNVM DIMM Secure Erase Unit, offset `0x5140F`.

## Controls and information

### Erase All DIMMs

Type: `OneOf`. Offset: `0x515BC`.

Firmware help: Erases the persistent memory region of all NVMDIMMs in the system

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C1`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xEC`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S0 CH0

Type: `OneOf`. Offset: `0x515E5`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 0, Memory controller 0, Socket 0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C2`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xED`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x515DD`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S0 CH1

Type: `OneOf`. Offset: `0x51610`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 1, Memory controller 0, Socket 0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C3`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xEE`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51608`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S0 CH2

Type: `OneOf`. Offset: `0x5163B`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 2, Memory controller 0, Socket 0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C4`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xEF`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51633`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S0 CH3

Type: `OneOf`. Offset: `0x51666`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 0, Memory controller 1, Socket 0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C5`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF0`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5165E`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S0 CH4

Type: `OneOf`. Offset: `0x51691`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 1, Memory controller 1, Socket 0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C6`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF1`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51689`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S0 CH5

Type: `OneOf`. Offset: `0x516BC`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 2, Memory controller 1, Socket 0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C7`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF2`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x516B4`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S1 CH0

Type: `OneOf`. Offset: `0x516E7`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 0, Memory controller 0, Socket 1

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C8`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF3`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x516DF`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S1 CH1

Type: `OneOf`. Offset: `0x51712`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 1, Memory controller 0, Socket 1

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C9`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF4`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5170A`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S1 CH2

Type: `OneOf`. Offset: `0x5173D`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 2, Memory controller 0, Socket 1

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13CA`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF5`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51735`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S1 CH3

Type: `OneOf`. Offset: `0x51768`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 0, Memory controller 1, Socket 1

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13CB`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF6`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x51760`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S1 CH4

Type: `OneOf`. Offset: `0x51793`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 1, Memory controller 1, Socket 1

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13CC`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF7`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5178B`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### S1 CH5

Type: `OneOf`. Offset: `0x517BE`.

Firmware help: Erases the persistent memory region of NVMDIMM in Channel 2, Memory controller 1, Socket 1

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13CD`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xF8`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x515B4`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x517B6`: (SocketMemoryConfig&#91;0xEC&#93; (Erase All DIMMs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
