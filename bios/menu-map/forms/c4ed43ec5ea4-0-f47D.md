# Sck0 IOAT Config

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; IOAT Configuration &gt; Sck0 IOAT Config**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x47D`, PE/section offset `0xEDAA`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [IOAT Configuration](c4ed43ec5ea4-0-f47C.md) via Sck0 IOAT Config, offset `0xED07`.

## Controls and information

### DCA

Type: `OneOf`. Offset: `0xEDB8`.

Firmware help: DCA Enable/Disable for this specific socket

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x21F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBAA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOAT Function 0 Items

Type: `Subtitle`. Offset: `0xEDE2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DMA

Type: `OneOf`. Offset: `0xEDF4`.

Firmware help: Select Dma Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x220`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBAC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No Snoop

Type: `OneOf`. Offset: `0xEE15`.

Firmware help: No Snoop Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x221`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBCC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOAT Function 1 Items

Type: `Subtitle`. Offset: `0xEE3F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DMA

Type: `OneOf`. Offset: `0xEE51`.

Firmware help: Select Dma Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x222`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBAD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No Snoop

Type: `OneOf`. Offset: `0xEE72`.

Firmware help: No Snoop Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x223`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBCD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOAT Function 2 Items

Type: `Subtitle`. Offset: `0xEE9C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DMA

Type: `OneOf`. Offset: `0xEEAE`.

Firmware help: Select Dma Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x224`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBAE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No Snoop

Type: `OneOf`. Offset: `0xEECF`.

Firmware help: No Snoop Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x225`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBCE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOAT Function 3 Items

Type: `Subtitle`. Offset: `0xEEF9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DMA

Type: `OneOf`. Offset: `0xEF0B`.

Firmware help: Select Dma Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x226`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBAF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No Snoop

Type: `OneOf`. Offset: `0xEF2C`.

Firmware help: No Snoop Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x227`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBCF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOAT Function 4 Items

Type: `Subtitle`. Offset: `0xEF56`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DMA

Type: `OneOf`. Offset: `0xEF68`.

Firmware help: Select Dma Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x228`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBB0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No Snoop

Type: `OneOf`. Offset: `0xEF89`.

Firmware help: No Snoop Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x229`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBD0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOAT Function 5 Items

Type: `Subtitle`. Offset: `0xEFB3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DMA

Type: `OneOf`. Offset: `0xEFC5`.

Firmware help: Select Dma Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x22A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBB1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No Snoop

Type: `OneOf`. Offset: `0xEFE6`.

Firmware help: No Snoop Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x22B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBD1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOAT Function 6 Items

Type: `Subtitle`. Offset: `0xF010`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DMA

Type: `OneOf`. Offset: `0xF022`.

Firmware help: Select Dma Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x22C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBB2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No Snoop

Type: `OneOf`. Offset: `0xF043`.

Firmware help: No Snoop Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x22D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBD2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOAT Function 7 Items

Type: `Subtitle`. Offset: `0xF06D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DMA

Type: `OneOf`. Offset: `0xF07F`.

Firmware help: Select Dma Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x22E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBB3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### No Snoop

Type: `OneOf`. Offset: `0xF0A0`.

Firmware help: No Snoop Enable/Disable for each CB device

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x22F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBD3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF30`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xECFF`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xEDB0`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
