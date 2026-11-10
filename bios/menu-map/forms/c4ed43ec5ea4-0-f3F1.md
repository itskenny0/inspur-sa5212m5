# CPU1 PgkC ENTRY CRITERIA

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; Package C State Control &gt; Program Pkg C-state Entry Criteria &gt; CPU1 PgkC ENTRY CRITERIA**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3F1`, PE/section offset `0x54604`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Program Pkg C-state Entry Criteria](c4ed43ec5ea4-0-f3A5.md) via CPU1 PgkC ENTRY CRITERIA, offset `0x53F23`.

## Controls and information

### CPU1 PgkC ENTRY CRITERIA

Type: `Subtitle`. Offset: `0x5460A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### UPI_0_IN_L1

Type: `OneOf`. Offset: `0x5462D`.

Firmware help: UPI_0 is selected either Disable or IN_L1

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14D3`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x9D`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### UPI_1_IN_L1

Type: `OneOf`. Offset: `0x5464E`.

Firmware help: UPI_1 is selected either Disable or IN_L1

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14D4`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x9F`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### UPI_2_IN_L1

Type: `OneOf`. Offset: `0x5466F`.

Firmware help: UPI_2 is selected either Disable or IN_L1

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14D5`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xA1`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCIE Port0 PCIE_IN

Type: `OneOf`. Offset: `0x54690`.

Firmware help: If IN_L1, set PCIE port in L1.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14D6`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xA3`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCIE Port1 PCIE_IN

Type: `OneOf`. Offset: `0x546B1`.

Firmware help: If IN_L1, set PCIE port in L1.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14D7`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xA5`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCIE Port2 PCIE_IN

Type: `OneOf`. Offset: `0x546D2`.

Firmware help: If IN_L1, set PCIE port in L1.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14D8`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xA7`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCIE Port3 PCIE_IN

Type: `OneOf`. Offset: `0x546F3`.

Firmware help: If IN_L1, set PCIE port in L1.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14D9`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xA9`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCIE Port4 PCIE_IN

Type: `OneOf`. Offset: `0x54714`.

Firmware help: If IN_L1, set PCIE port in L1.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14DA`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xAB`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCIE Port5 PCIE_IN

Type: `OneOf`. Offset: `0x54735`.

Firmware help: If IN_L1, set PCIE port in L1.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| IN_L1 | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14DB`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xAD`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x54625`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
