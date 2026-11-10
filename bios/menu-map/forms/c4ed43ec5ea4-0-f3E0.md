# PMAX CONFIG Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; PMAX CONFIG Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3E0`, PE/section offset `0x5444A`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Advanced Power Management Configuration](c4ed43ec5ea4-0-f51C.md) via PMAX CONFIG Configuration, offset `0x52EE6`.

## Controls and information

### PMAX CONFIG Configuration

Type: `Subtitle`. Offset: `0x54450`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PMAX Config Sign

Type: `OneOf`. Offset: `0x5446A`.

Firmware help: Controls whether PMAX Config offset is a positive or negative value.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Positive | 0 | standard, manufacturing | none |
| Negative | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14C8`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xC0`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54462`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PMAX Config Offset

Type: `Numeric`. Offset: `0x5448B`.

Firmware help: Input decimal correction factor to program. Valid input values are 0 to 15. Will be positive or negative based on PMAX Config Sign value.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 8; Min: 0x0; Max: 0xF; Step: 0x1.

Question ID: `0x14C9`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xC1`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54462`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
