# Network Configuration

[Menu index](../README.md) | [Module index](../f44ace4934bd-0.md)

Path: **Chipset &gt; Network Configuration**

Source: `Platform`. Formset `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9`, form `0xB`, PE/section offset `0xF367`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Controls and information

### Legacy Option ROMs support

Type: `OneOf`. Offset: `0xF36D`.

Firmware help: Enable/Disable Legacy PXE Option ROM execution for LANs.

Access: No active IFR hide condition on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 1 | none | none |
| Disabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x34`. Question flags: `0x10` (reset required).

Storage: `IntelSetup` at byte offset `0x104`, GUID `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9`. This is a variable offset, not a CMOS address.

### EFI Network

Type: `OneOf`. Offset: `0xF38E`.

Firmware help: Enable/Disable EFI Network support for LANs.

Access: No active IFR hide condition on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 1 | none | none |
| Disabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x35`. Question flags: `0x10` (reset required).

Storage: `IntelSetup` at byte offset `0x105`, GUID `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9`. This is a variable offset, not a CMOS address.

### LOM

Type: `OneOf`. Offset: `0xF3AF`.

Firmware help: Enable/Disable LAN on motherboard.

Access: No active IFR hide condition on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x36`. Question flags: `0x10` (reset required).

Storage: `IntelSetup` at byte offset `0x52`, GUID `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9`. This is a variable offset, not a CMOS address.

### FPK Port 1

Type: `OneOf`. Offset: `0xF3D8`.

Firmware help: Change mode of FPK Port 1

Access: Conditional; no CMOS vendor gate on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 1 | standard, manufacturing | none |
| Management | 2 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x37`. Question flags: `0x10` (reset required).

Storage: `IntelSetup` at byte offset `0x53`, GUID `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xF3D0`: (IntelSetup&#91;0x5B&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### FPK Port 2

Type: `OneOf`. Offset: `0xF40A`.

Firmware help: Change mode of FPK Port 2

Access: Conditional; no CMOS vendor gate on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 1 | standard, manufacturing | none |
| Management | 2 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x38`. Question flags: `0x10` (reset required).

Storage: `IntelSetup` at byte offset `0x54`, GUID `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xF402`: (IntelSetup&#91;0x5C&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### FPK Port 3

Type: `OneOf`. Offset: `0xF43C`.

Firmware help: Change mode of FPK Port 3

Access: Conditional; no CMOS vendor gate on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 1 | standard, manufacturing | none |
| Management | 2 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x39`. Question flags: `0x10` (reset required).

Storage: `IntelSetup` at byte offset `0x55`, GUID `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xF434`: (IntelSetup&#91;0x5D&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### FPK Port 4

Type: `OneOf`. Offset: `0xF46E`.

Firmware help: Change mode of FPK Port 4

Access: Conditional; no CMOS vendor gate on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 1 | standard, manufacturing | none |
| Management | 2 | none | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x3A`. Question flags: `0x10` (reset required).

Storage: `IntelSetup` at byte offset `0x56`, GUID `EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0xF466`: (IntelSetup&#91;0x5E&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
