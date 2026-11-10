# Socket1 Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; Socket1 Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x47B`, PE/section offset `0xBA01`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [IIO Configuration](c4ed43ec5ea4-0-f518.md) via Socket1 Configuration, offset `0xAF1F`.

## Controls and information

### IOU0 (IIO PCIe Br1)

Type: `OneOf`. Offset: `0xBA17`.

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

Question ID: `0xC4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBA0F`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOU1 (IIO PCIe Br2)

Type: `OneOf`. Offset: `0xBA54`.

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

Question ID: `0xC5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBA0F`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOU2 (IIO PCIe Br3)

Type: `OneOf`. Offset: `0xBA99`.

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

Question ID: `0xC6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBA0F`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBA91`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### MCP0 (IIO PCIe Br4)

Type: `OneOf`. Offset: `0xBAD6`.

Firmware help: Selects PCIe port Bifurcation for selected slot(s)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| x16 | 4 | standard, manufacturing | none |
| Auto | 255 | none | none |

Size: 8; Min: 0x4; Max: 0xFF; Step: 0x0.

Question ID: `0xC7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBA0F`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBA91`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### MCP1 (IIO PCIe Br5)

Type: `OneOf`. Offset: `0xBAF7`.

Firmware help: Selects PCIe port Bifurcation for selected slot(s)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| x16 | 4 | standard, manufacturing | none |
| Auto | 255 | none | none |

Size: 8; Min: 0x4; Max: 0xFF; Step: 0x0.

Question ID: `0xC8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xC0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBA0F`: (SocketIioConfig&#91;0xC5F&#93; (PCIe Train by BIOS) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBA91`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Completion Timeout Disable

Type: `OneOf`. Offset: `0xBB24`.

Firmware help: Enable / disable the Completion Timeout (D:x F:0 O:B8h B:4) where x is 0-3

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 0 | standard, manufacturing | none |
| Disabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xC9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xC4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBB1C`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Completion Timeout Value

Type: `OneOf`. Offset: `0xBB4D`.

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

Question ID: `0xCA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xC6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBB1C`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBB45`: (SocketIioConfig&#91;0xC4&#93; (PCI-E Completion Timeout Disable) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Sck1 RP Correctable Err

Type: `OneOf`. Offset: `0xBB93`.

Firmware help: Applies to root ports only. Enable interrupt on correctable errors

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xCB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBB1C`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Sck1 RP NonFatal Uncorrectable Err

Type: `OneOf`. Offset: `0xBBB4`.

Firmware help: Applies to root ports only. Enable interrupt on a non-fatal error

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xCC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBB1C`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Sck1 RP Fatal Uncorrectable Err

Type: `OneOf`. Offset: `0xBBD5`.

Firmware help: Applies to root ports only. Enable MSI/INTx interrupt on fatal errors

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xCD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBB1C`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Not Any Riser Card Plugged

Type: `Subtitle`. Offset: `0xBC1A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBBF8`: ((((SocketIioConfig&#91;0xB3&#93; == 0x1) or (SocketIioConfig&#91;0xB4&#93; == 0x1)) or (SocketIioConfig&#91;0xB5&#93; == 0x1)) or (SocketIioConfig&#91;0xB6&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser1 (3* x8) Card Plugged on PCIE1_CPU0/1

Type: `Subtitle`. Offset: `0xBC2D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC25`: (SocketIioConfig&#91;0xB3&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser1: Up-&gt;Port 2C(CPU1);Middle-&gt;Port 2A(CPU1);Down-&gt;Port 3A (CPU0)

Type: `Subtitle`. Offset: `0xBC36`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC25`: (SocketIioConfig&#91;0xB3&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser2 (1* x16+ 1* x8) Card Plugged on PCIE1_CPU0/1

Type: `Subtitle`. Offset: `0xBC49`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC41`: (SocketIioConfig&#91;0xB4&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser2: Up(x16)-&gt;Port 2A(CPU1);Down(x8)-&gt;Port 3A(CPU0)

Type: `Subtitle`. Offset: `0xBC52`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC41`: (SocketIioConfig&#91;0xB4&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser3 (2* x8) Card Plugged on PCIE2_CPU1

Type: `Subtitle`. Offset: `0xBC65`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC5D`: (SocketIioConfig&#91;0xB5&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser3: Up-&gt;Port 1C; Down-&gt;Port 1A

Type: `Subtitle`. Offset: `0xBC6E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC5D`: (SocketIioConfig&#91;0xB5&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser4 (1* x16) Card Plugged on PCIE2_CPU1

Type: `Subtitle`. Offset: `0xBC81`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC79`: (SocketIioConfig&#91;0xB6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Riser4: Port1A(x16)

Type: `Subtitle`. Offset: `0xBC8A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xBA07`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC79`: (SocketIioConfig&#91;0xB6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr0D00F0 - Port 0

Type: `Ref`. Offset: `0xBCA7`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr0D00F0 - Port 0](c4ed43ec5ea4-0-f462.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xCE`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBC97`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBC9F`: (SocketIioConfig&#91;0xC79&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr1D00F0 - Port 1A

Type: `Ref`. Offset: `0xBCC2`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr1D00F0 - Port 1A](c4ed43ec5ea4-0-f463.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xCF`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBCBA`: (SocketIioConfig&#91;0xC7A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr1D01F0 - Port 1B

Type: `Ref`. Offset: `0xBCDB`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr1D01F0 - Port 1B](c4ed43ec5ea4-0-f469.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD0`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBCD3`: (SocketIioConfig&#91;0xC7B&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr1D02F0 - Port 1C

Type: `Ref`. Offset: `0xBCF4`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr1D02F0 - Port 1C](c4ed43ec5ea4-0-f46A.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD1`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBCEC`: (SocketIioConfig&#91;0xC7C&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr1D03F0 - Port 1D

Type: `Ref`. Offset: `0xBD0D`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr1D03F0 - Port 1D](c4ed43ec5ea4-0-f46B.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD2`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBD05`: (SocketIioConfig&#91;0xC7D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr2D00F0 - Port 2A

Type: `Ref`. Offset: `0xBD26`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr2D00F0 - Port 2A](c4ed43ec5ea4-0-f46C.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD3`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBD1E`: (SocketIioConfig&#91;0xC7E&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr2D01F0 - Port 2B

Type: `Ref`. Offset: `0xBD3F`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr2D01F0 - Port 2B](c4ed43ec5ea4-0-f46D.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD4`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBD37`: (SocketIioConfig&#91;0xC7F&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr2D02F0 - Port 2C

Type: `Ref`. Offset: `0xBD58`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr2D02F0 - Port 2C](c4ed43ec5ea4-0-f46E.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD5`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBD50`: (SocketIioConfig&#91;0xC80&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr2D03F0 - Port 2D

Type: `Ref`. Offset: `0xBD71`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr2D03F0 - Port 2D](c4ed43ec5ea4-0-f46F.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD6`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBD69`: (SocketIioConfig&#91;0xC81&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr3D00F0 - Port 3A

Type: `Ref`. Offset: `0xBD8A`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr3D00F0 - Port 3A](c4ed43ec5ea4-0-f470.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD7`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBD82`: (SocketIioConfig&#91;0xC82&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr3D01F0 - Port 3B

Type: `Ref`. Offset: `0xBDA3`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr3D01F0 - Port 3B](c4ed43ec5ea4-0-f475.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD8`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBD9B`: (SocketIioConfig&#91;0xC83&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr3D02F0 - Port 3C

Type: `Ref`. Offset: `0xBDBC`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr3D02F0 - Port 3C](c4ed43ec5ea4-0-f476.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xD9`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDB4`: (SocketIioConfig&#91;0xC84&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr3D03F0 - Port 3D

Type: `Ref`. Offset: `0xBDD5`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr3D03F0 - Port 3D](c4ed43ec5ea4-0-f477.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xDA`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDCD`: (SocketIioConfig&#91;0xC85&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr4D00F0 - MCP 0

Type: `Ref`. Offset: `0xBDF6`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr4D00F0 - MCP 0](c4ed43ec5ea4-0-f478.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xDB`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDE6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBDEE`: (SocketIioConfig&#91;0xC86&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr4D01F0 - MCP 0

Type: `Ref`. Offset: `0xBE0F`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr4D01F0 - MCP 0](c4ed43ec5ea4-0-f479.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xDC`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDE6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBE07`: (SocketIioConfig&#91;0xC87&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr4D02F0 - MCP 0

Type: `Ref`. Offset: `0xBE28`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr4D02F0 - MCP 0](c4ed43ec5ea4-0-f48E.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xDD`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDE6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBE20`: (SocketIioConfig&#91;0xC88&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr4D03F0 - MCP 0

Type: `Ref`. Offset: `0xBE41`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr4D03F0 - MCP 0](c4ed43ec5ea4-0-f48F.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xDE`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDE6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBE39`: (SocketIioConfig&#91;0xC89&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr5D00F0 - MCP 1

Type: `Ref`. Offset: `0xBE5A`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr5D00F0 - MCP 1](c4ed43ec5ea4-0-f490.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xDF`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDE6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBE52`: (SocketIioConfig&#91;0xC8A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr5D01F0 - MCP 1

Type: `Ref`. Offset: `0xBE73`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr5D01F0 - MCP 1](c4ed43ec5ea4-0-f491.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xE0`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDE6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBE6B`: (SocketIioConfig&#91;0xC8B&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr5D02F0 - MCP 1

Type: `Ref`. Offset: `0xBE8C`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr5D02F0 - MCP 1](c4ed43ec5ea4-0-f492.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xE1`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDE6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBE84`: (SocketIioConfig&#91;0xC8C&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 1 PcieBr5D03F0 - MCP 1

Type: `Ref`. Offset: `0xBEA5`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 1 PcieBr5D03F0 - MCP 1](c4ed43ec5ea4-0-f493.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0xE2`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAF17`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xBDE6`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xBE9D`: (SocketIioConfig&#91;0xC8D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
