# EPB Override Control

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; EPB Override Control**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3A7`, PE/section offset `0x5406B`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Advanced Power Management Configuration](c4ed43ec5ea4-0-f51C.md) via EPB Override Control, offset `0x52EBE`.

## Controls and information

### EPB Override Control

Type: `Subtitle`. Offset: `0x54071`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### UNCORE_PERF_PLIMIT_OVRD_EN

Type: `OneOf`. Offset: `0x5408B`.

Firmware help: Uncore Perf PLimit Override

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14B1`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x71`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54083`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### EET_OVERRIDE_ENABLE

Type: `OneOf`. Offset: `0x540AC`.

Firmware help: EET override

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14B2`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x72`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54083`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IO_BW_PLIMIT_OVRD_EN

Type: `OneOf`. Offset: `0x540CD`.

Firmware help: IO BW PLimit Override

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14B3`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x73`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54083`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### IOM_APM_OVERRIDE_ENABLE

Type: `OneOf`. Offset: `0x540EE`.

Firmware help: IOM APM Override

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14B4`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x75`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54083`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### UPI_APM_OVERRIDE_ENABLE

Type: `OneOf`. Offset: `0x5410F`.

Firmware help: UPI APM Override

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14B5`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x76`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54083`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
