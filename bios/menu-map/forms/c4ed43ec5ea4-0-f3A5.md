# Program Pkg C-state Entry Criteria

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; Package C State Control &gt; Program Pkg C-state Entry Criteria**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3A5`, PE/section offset `0x53ECB`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Package C State Control](c4ed43ec5ea4-0-f394.md) via Program Pkg C-state Entry Criteria, offset `0x53873`.

## Controls and information

### Program Pkg C-state Entry Criteria

Type: `Subtitle`. Offset: `0x53ED1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.

### PKGC_ENTRY_CRITERIA OVRD

Type: `OneOf`. Offset: `0x53EEB`.

Firmware help: Allows manual overrides for PKG_CST_ENTRY_CRITERIA_MASK

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| SKIP | 0 | manufacturing | none |
| Manual | 1 | standard | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14A6`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x5F`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CPU0 PgkC ENTRY CRITERIA

Type: `Ref`. Offset: `0x53F14`.

Firmware help: Socket Specific PgkC ENTRY CRITERIA

Opens: [CPU0 PgkC ENTRY CRITERIA](c4ed43ec5ea4-0-f3F0.md).

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Question ID: `0x14A7`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CPU1 PgkC ENTRY CRITERIA

Type: `Ref`. Offset: `0x53F23`.

Firmware help: Socket Specific PgkC ENTRY CRITERIA

Opens: [CPU1 PgkC ENTRY CRITERIA](c4ed43ec5ea4-0-f3F1.md).

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Question ID: `0x14A8`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x5386F`: 0x1. Expression result: stock true; CMOS unlock true.
- `GrayOutIf` at `0x53EE3`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53F0C`: (SocketPowerManagementConfig&#91;0x5F&#93; (PKGC_ENTRY_CRITERIA OVRD) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
