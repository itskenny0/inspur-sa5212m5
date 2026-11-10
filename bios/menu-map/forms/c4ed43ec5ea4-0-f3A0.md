# CPU - Advanced PM Tuning

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; CPU - Advanced PM Tuning**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3A0`, PE/section offset `0x53C40`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Advanced Power Management Configuration](c4ed43ec5ea4-0-f51C.md) via CPU - Advanced PM Tuning, offset `0x52E96`.

## Controls and information

### CPU - Advanced PM Tuning

Type: `Subtitle`. Offset: `0x53C46`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Energy Perf BIAS

Type: `Ref`. Offset: `0x53C58`.

Firmware help: Energy Perf BIAS Sub Menu

Opens: [Energy Perf BIAS](c4ed43ec5ea4-0-f3A1.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1499`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### SAPM Control

Type: `OneOf`. Offset: `0x53C77`.

Firmware help: MSR 1FCh Bit&#91;22&#93; = PWR_PERF_TUNING_DISABLE_SAPM_CTRL

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 0 | standard, manufacturing | none |
| Disabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x149A`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x54`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53C67`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53C6F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
