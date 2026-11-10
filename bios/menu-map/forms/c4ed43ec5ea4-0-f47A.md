# Socket0 Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; Socket0 Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x47A`, PE/section offset `0xB53C`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [IIO Configuration](c4ed43ec5ea4-0-f518.md) via Socket0 Configuration, offset `0xAEF0`.

## Controls and information

### IOU0 (IIO PCIe Br1)

Type: `OneOf`. Offset: `0xB55A`.

Firmware help: Selects PCIe port Bifurcation for selected slot(s)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| x4x4x4x4 | 0 | none | none |
| x4x4x8 | 1 | none | none |
| x8x4x4 | 2 | none | none |
| x8x8 | 3 | standard, manufacturing | none |
| x16 | 4 | none | none |
| Auto | 255 | none | none |

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0xA4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB54A`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB552`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### IOU1 (IIO PCIe Br2)

Type: `OneOf`. Offset: `0xB599`.

Firmware help: Selects PCIe port Bifurcation for selected slot(s)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| x4x4x4x4 | 0 | none | none |
| x4x4x8 | 1 | none | none |
| x8x4x4 | 2 | none | none |
| x8x8 | 3 | standard, manufacturing | none |
| x16 | 4 | none | none |
| Auto | 255 | none | none |

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0xA5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB54A`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOU2 (IIO PCIe Br3)

Type: `OneOf`. Offset: `0xB5DE`.

Firmware help: Selects PCIe port Bifurcation for selected slot(s)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| x4x4x4x4 | 0 | none | none |
| x4x4x8 | 1 | none | none |
| x8x4x4 | 2 | none | none |
| x8x8 | 3 | none | none |
| x16 | 4 | none | none |
| Auto | 255 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0xA6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB54A`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB5D6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### MCP0 (IIO PCIe Br4)

Type: `OneOf`. Offset: `0xB61B`.

Firmware help: Selects PCIe port Bifurcation for selected slot(s)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| x16 | 4 | standard, manufacturing | none |
| Auto | 255 | none | none |

Size: 8; Min: 0x4; Max: 0xFF; Step: 0x0.

Question ID: `0xA7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB54A`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB5D6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### MCP1 (IIO PCIe Br5)

Type: `OneOf`. Offset: `0xB63C`.

Firmware help: Selects PCIe port Bifurcation for selected slot(s)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| x16 | 4 | standard, manufacturing | none |
| Auto | 255 | none | none |

Size: 8; Min: 0x4; Max: 0xFF; Step: 0x0.

Question ID: `0xA8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB54A`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB5D6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Completion Timeout Disable

Type: `OneOf`. Offset: `0xB669`.

Firmware help: Enable / disable the Completion Timeout (D:x F:0 O:B8h B:4) where x is 0-3

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| No | 0 | standard, manufacturing | none |
| Yes | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xA9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xC3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB661`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Completion Timeout Value

Type: `OneOf`. Offset: `0xB692`.

Firmware help: Program the Completion Timeout Value (D:x F:0 O:B8h B:3-0) where x is 0-3

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 50µs to 10ms | 0 | none | none |
| 16ms to 55ms | 5 | none | none |
| 65ms to 210ms | 6 | none | none |
| 260ms to 900ms | 9 | standard, manufacturing | none |
| 1s to 3.5s | 10 | none | none |
| 4s to 13s | 13 | none | none |
| 17s to 64s | 14 | none | none |

Size: 8; Min: 0x0; Max: 0xE; Step: 0x0.

Question ID: `0xAA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xC5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB661`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB68A`: (SocketIioConfig&#91;0xC3&#93; (PCI-E Completion Timeout Disable) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Sck0 RP Correctable Err

Type: `OneOf`. Offset: `0xB6D8`.

Firmware help: Applies to root ports only. Enable interrupt on correctable errors

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xAB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB661`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Sck0 RP NonFatal Uncorrectable Err

Type: `OneOf`. Offset: `0xB6F9`.

Firmware help: Applies to root ports only. Enable interrupt on a non-fatal error

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xAC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB661`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Sck0 RP Fatal Uncorrectable Err

Type: `OneOf`. Offset: `0xB71A`.

Firmware help: Applies to root ports only. Enable MSI/INTx interrupt on fatal errors

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xAD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB661`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### (internal CheckBox, Q0xAE)

Type: `CheckBox`. Offset: `0xB741`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0xAE`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xC64`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB73D`: 0x1. Expression result: stock true; CMOS unlock true.

### Not Any Riser Card Plugged

Type: `Subtitle`. Offset: `0xB775`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB753`: ((((SocketIioConfig&#91;0xB1&#93; == 0x1) or (SocketIioConfig&#91;0xB2&#93; == 0x1)) or (SocketIioConfig&#91;0xB3&#93; == 0x1)) or (SocketIioConfig&#91;0xB4&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser1 Card (3* x8) Plugged on PCIE0_CPU0

Type: `Subtitle`. Offset: `0xB788`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB780`: (SocketIioConfig&#91;0xB1&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser1: Up-&gt;Port 2C;Middle-&gt;Port 2A;Down-&gt;Port 3C

Type: `Subtitle`. Offset: `0xB791`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB780`: (SocketIioConfig&#91;0xB1&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser2 Card (1* x16+ 1* x8) Plugged on PCIE0_CPU0

Type: `Subtitle`. Offset: `0xB7A4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB79C`: (SocketIioConfig&#91;0xB2&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser2: Up(x16)-&gt;Port 2A;Down(x8)-&gt;Port 3C

Type: `Subtitle`. Offset: `0xB7AD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB79C`: (SocketIioConfig&#91;0xB2&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser1 (3* x8) Card Plugged on PCIE1_CPU0/1

Type: `Subtitle`. Offset: `0xB7C0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB7B8`: (SocketIioConfig&#91;0xB3&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser1: Up-&gt;Port 2C(CPU1);Middle-&gt;Port 2A(CPU1);Down-&gt;Port 3A (CPU0)

Type: `Subtitle`. Offset: `0xB7C9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB7B8`: (SocketIioConfig&#91;0xB3&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser2 (1* x16+ 1* x8) Card Plugged on PCIE1_CPU0/1

Type: `Subtitle`. Offset: `0xB7DC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB7D4`: (SocketIioConfig&#91;0xB4&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser2: Up(x16)-&gt;Port 2A(CPU1);Down(x8)-&gt;Port 3A(CPU0)

Type: `Subtitle`. Offset: `0xB7E5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xB542`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB7D4`: (SocketIioConfig&#91;0xB4&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr0D00F0 - Port 0/DMI

Type: `Ref`. Offset: `0xB7F2`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr0D00F0 - Port 0/DMI](c4ed43ec5ea4-0-f453.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xAF`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Port 1A - 10GBE Uplink x8

Type: `Ref`. Offset: `0xB809`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Port 1A - 10GBE Uplink x8](c4ed43ec5ea4-0-f454.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB0`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB801`: (SocketIioConfig&#91;0xC65&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr1D01F0 - Port 1B

Type: `Ref`. Offset: `0xB822`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr1D01F0 - Port 1B](c4ed43ec5ea4-0-f455.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB1`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB81A`: (SocketIioConfig&#91;0xC66&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Port 1C - OCP_A

Type: `Ref`. Offset: `0xB83B`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Port 1C - OCP_A](c4ed43ec5ea4-0-f456.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB2`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB833`: (SocketIioConfig&#91;0xC67&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr1D03F0 - Port 1D

Type: `Ref`. Offset: `0xB854`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr1D03F0 - Port 1D](c4ed43ec5ea4-0-f457.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB3`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB84C`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr2D00F0 - Port 2A

Type: `Ref`. Offset: `0xB86D`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr2D00F0 - Port 2A](c4ed43ec5ea4-0-f458.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB4`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB865`: (SocketIioConfig&#91;0xC69&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr2D01F0 - Port 2B

Type: `Ref`. Offset: `0xB886`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr2D01F0 - Port 2B](c4ed43ec5ea4-0-f459.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB5`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB87E`: (SocketIioConfig&#91;0xC6A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr2D02F0 - Port 2C

Type: `Ref`. Offset: `0xB89F`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr2D02F0 - Port 2C](c4ed43ec5ea4-0-f45A.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB6`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB897`: (SocketIioConfig&#91;0xC6B&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr2D03F0 - Port 2D

Type: `Ref`. Offset: `0xB8B8`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr2D03F0 - Port 2D](c4ed43ec5ea4-0-f45B.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB7`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8B0`: (SocketIioConfig&#91;0xC6C&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr3D00F0 - Port 3A

Type: `Ref`. Offset: `0xB8D1`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr3D00F0 - Port 3A](c4ed43ec5ea4-0-f45C.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB8`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr3D01F0 - Port 3B

Type: `Ref`. Offset: `0xB8EA`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr3D01F0 - Port 3B](c4ed43ec5ea4-0-f45D.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xB9`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8E2`: (SocketIioConfig&#91;0xC6E&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr3D02F0 - Port 3C

Type: `Ref`. Offset: `0xB903`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr3D02F0 - Port 3C](c4ed43ec5ea4-0-f45E.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xBA`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8FB`: (SocketIioConfig&#91;0xC6F&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr3D03F0 - Port 3D

Type: `Ref`. Offset: `0xB91C`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr3D03F0 - Port 3D](c4ed43ec5ea4-0-f45F.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xBB`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB914`: (SocketIioConfig&#91;0xC70&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr4D00F0 - MCP 0

Type: `Ref`. Offset: `0xB93D`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr4D00F0 - MCP 0](c4ed43ec5ea4-0-f460.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xBC`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB92D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB935`: (SocketIioConfig&#91;0xC71&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr4D01F0 - MCP 0

Type: `Ref`. Offset: `0xB956`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr4D01F0 - MCP 0](c4ed43ec5ea4-0-f461.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xBD`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB92D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB94E`: (SocketIioConfig&#91;0xC72&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr4D01F0 - MCP 0

Type: `Ref`. Offset: `0xB96F`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr4D02F0 - MCP 0](c4ed43ec5ea4-0-f488.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xBE`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB92D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB967`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr4D03F0 - MCP 0

Type: `Ref`. Offset: `0xB988`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr4D03F0 - MCP 0](c4ed43ec5ea4-0-f489.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xBF`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB92D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB980`: (SocketIioConfig&#91;0xC74&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr5D00F0 - MCP 1

Type: `Ref`. Offset: `0xB9A1`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr5D00F0 - MCP 1](c4ed43ec5ea4-0-f48A.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xC0`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB92D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB999`: (SocketIioConfig&#91;0xC75&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr5D01F0 - MCP 1

Type: `Ref`. Offset: `0xB9BA`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr5D01F0 - MCP 1](c4ed43ec5ea4-0-f48B.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xC1`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB92D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB9B2`: (SocketIioConfig&#91;0xC76&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr5D02F0 - MCP 1

Type: `Ref`. Offset: `0xB9D3`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr5D02F0 - MCP 1](c4ed43ec5ea4-0-f48C.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xC2`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB92D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB9CB`: (SocketIioConfig&#91;0xC77&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 PcieBr5D03F0 - MCP 1

Type: `Ref`. Offset: `0xB9EC`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 PcieBr5D03F0 - MCP 1](c4ed43ec5ea4-0-f48D.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xC3`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB92D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xB9E4`: (SocketIioConfig&#91;0xC78&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
