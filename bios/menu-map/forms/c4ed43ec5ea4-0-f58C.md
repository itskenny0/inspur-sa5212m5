# NGN Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Memory Configuration &gt; NGN Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x58C`, PE/section offset `0x51409`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Memory Configuration](c4ed43ec5ea4-0-f540.md) via NGN Configuration, offset `0x50AAA`.

## Controls and information

### NGNVM DIMM Secure Erase Unit

Type: `Ref`. Offset: `0x5140F`.

Firmware help: Erases the persistent memory region of the selected DIMMs

Opens: [NGNVM DIMM Secure Erase Unit](c4ed43ec5ea4-0-f58E.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x13B7`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Set TDP DIMM power limit

Type: `OneOf`. Offset: `0x51426`.

Firmware help: Sets the current total dissipated DIMM power limit

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 10W | 10 | none | none |
| 12W | 12 | standard, manufacturing | none |
| 15W | 15 | none | none |
| 18W | 18 | none | none |

Size: 8; Min: 0xA; Max: 0x12; Step: 0x0.

Question ID: `0x13B8`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xEB`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### ARS on Boot

Type: `OneOf`. Offset: `0x51455`.

Firmware help: Enable\Disable Address Range Scrub during boot time

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13B9`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xDA`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Lock NGN CSRs

Type: `OneOf`. Offset: `0x5147D`.

Firmware help: Enable\Disable Lock NGN CSRs

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13BA`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xD3`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Debug lock for NGN

Type: `OneOf`. Offset: `0x514A5`.

Firmware help: Enable\Disable Debug lock for NGN

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13BB`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xD9`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### NGN CMD Time

Type: `OneOf`. Offset: `0x514CD`.

Firmware help: Select 1N\2N NGN Command tme

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| 1N | 0 | none | none |
| 2N | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13BC`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xD4`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### NGN ECC Correctable error

Type: `OneOf`. Offset: `0x514F5`.

Firmware help: Enable\Disable NGN ECC Correctable error

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13BD`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xD5`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### NGN ECC Write Check

Type: `OneOf`. Offset: `0x5151D`.

Firmware help: Enable\Disable NGN ECC Write Check

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13BE`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xD6`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### NGN ECC Read Check

Type: `OneOf`. Offset: `0x51545`.

Firmware help: Enable\Disable NGN ECC Read Check

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13BF`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xD7`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CR QoS Configuration

Type: `OneOf`. Offset: `0x5156D`.

Firmware help: Select CR QoS Configuration Profiles

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Default (no QoS optimization) | 0 | standard, manufacturing | none |
| Option 1 | 1 | none | none |
| Option 2 | 2 | none | none |
| Option 3 | 3 | none | none |
| Option 4 | 4 | none | none |
| Option 5 | 5 | none | none |

Size: 8; Min: 0x0; Max: 0x5; Step: 0x0.

Question ID: `0x13C0`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x11F`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A84`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x5141E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
