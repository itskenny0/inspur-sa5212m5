# Package Current Config

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; Package Current Config**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3A3`, PE/section offset `0x53E1D`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Advanced Power Management Configuration](c4ed43ec5ea4-0-f51C.md) via Package Current Config, offset `0x52EAF`.

## Controls and information

### Package Current Config

Type: `Subtitle`. Offset: `0x53E23`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Current Limit Override

Type: `OneOf`. Offset: `0x53E3D`.

Firmware help: 0 - Default, do nothing; 1 - Manual, override Current limitation in 1/8 A increments.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14A3`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x55`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53E35`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Current Limitation

Type: `Numeric`. Offset: `0x53E66`.

Firmware help: Current limitation in 1/8 A increments. This field is locked by VR_CURRENT_CONFIG&#91;LOCK&#93; Value &lt;= CURRENT_LIMIT

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 1080; store 0x1: 1080.

Size: 16; Min: 0x0; Max: 0x7F8; Step: 0x0.

Question ID: `0x14A4`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x58`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53E35`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53E5E`: (SocketPowerManagementConfig&#91;0x55&#93; (Current Limit Override) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Lock Indication

Type: `OneOf`. Offset: `0x53E8C`.

Firmware help: Lock for CURRENT_LIMIT settings Move this into the Config Above

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14A5`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x60`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53E35`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
