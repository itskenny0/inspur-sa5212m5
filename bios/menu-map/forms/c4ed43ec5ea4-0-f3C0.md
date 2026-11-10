# SOCKET RAPL Config

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; SOCKET RAPL Config**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3C0`, PE/section offset `0x54293`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Advanced Power Management Configuration](c4ed43ec5ea4-0-f51C.md) via SOCKET RAPL Config, offset `0x52ECD`.

## Controls and information

### SOCKET RAPL Config

Type: `Subtitle`. Offset: `0x54299`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### FAST_RAPL_NSTRIKE_PL2_DUTY_CYCLE

Type: `Numeric`. Offset: `0x542BB`.

Firmware help: FAST_RAPL_NSTRIKE_PL2_DUTY_CYCLE value between 25 (10%) - 64 (25%)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 64; store 0x1: 64.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x1.

Question ID: `0x14BF`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xAE`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x542B3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Package RAPL Limit MSR Lock

Type: `OneOf`. Offset: `0x542EC`.

Firmware help: Enable/Disable locking of Package RAPL Limit MSR and a reset will be required to unlock the register.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14C0`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xAF`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x542B3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x542DA`: ((SocketPowerManagementConfig&#91;0x5&#93; (Enhanced Intel SpeedStep(R) Tech) == 0x0) or (SocketPowerManagementConfig&#91;0x19&#93; (Intel(R) Turbo Boost Technology) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Package RAPL Limit CSR Lock

Type: `OneOf`. Offset: `0x5430D`.

Firmware help: Enable/Disable locking of Package RAPL Limit CSR and a reset will be required to unlock the register.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14C1`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xB0`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x542B3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x542DA`: ((SocketPowerManagementConfig&#91;0x5&#93; (Enhanced Intel SpeedStep(R) Tech) == 0x0) or (SocketPowerManagementConfig&#91;0x19&#93; (Intel(R) Turbo Boost Technology) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PL1 Limit

Type: `OneOf`. Offset: `0x54330`.

Firmware help: Enable/Disable PL1. If this option is disabled, BIOS will program the deafult values for PL1 Power Limit and PL1 Time Window.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14C2`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xB1`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x542B3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PL1 Power Limit

Type: `Numeric`. Offset: `0x5436D`.

Firmware help: PL1 Power Limit in Watts. The value may vary from 0 to Fused Value. If the value is 0, the fused value will be programmed. A value greater than fused TDP value will not be programmed.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0x7FFF; Step: 0x1.

Question ID: `0x14C3`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xB2`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x54353`: (((SocketPowerManagementConfig&#91;0x5&#93; (Enhanced Intel SpeedStep(R) Tech) == 0x0) or (SocketPowerManagementConfig&#91;0x19&#93; (Intel(R) Turbo Boost Technology) == 0x0)) or (SocketPowerManagementConfig&#91;0xB1&#93; (PL1 Limit) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PL1 Time Window

Type: `Numeric`. Offset: `0x5439B`.

Firmware help: PL1 value in seconds. The value may vary from 0 to 56. Indicates the time window over which TDP value should be maintained. If the value is 0, the fused value will be programmed.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 1; store 0x1: 1.

Size: 8; Min: 0x0; Max: 0x38; Step: 0x1.

Question ID: `0x14C4`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xB6`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x54353`: (((SocketPowerManagementConfig&#91;0x5&#93; (Enhanced Intel SpeedStep(R) Tech) == 0x0) or (SocketPowerManagementConfig&#91;0x19&#93; (Intel(R) Turbo Boost Technology) == 0x0)) or (SocketPowerManagementConfig&#91;0xB1&#93; (PL1 Limit) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PL2 Limit

Type: `OneOf`. Offset: `0x543BA`.

Firmware help: Enable/Disable PL2. If this option is disabled, BIOS will program the deafult values for PL2 Power Limit and PL2 Time Window.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14C5`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xB8`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x54353`: (((SocketPowerManagementConfig&#91;0x5&#93; (Enhanced Intel SpeedStep(R) Tech) == 0x0) or (SocketPowerManagementConfig&#91;0x19&#93; (Intel(R) Turbo Boost Technology) == 0x0)) or (SocketPowerManagementConfig&#91;0xB1&#93; (PL1 Limit) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PL2 Power Limit

Type: `Numeric`. Offset: `0x543F7`.

Firmware help: PL2 Power Limit in Watts. The value may vary from 0 to Fused Value. If the value is 0, BIOS programs 125% * TDP

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0x7FFF; Step: 0x1.

Question ID: `0x14C6`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xB9`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x543DD`: (((SocketPowerManagementConfig&#91;0x5&#93; (Enhanced Intel SpeedStep(R) Tech) == 0x0) or (SocketPowerManagementConfig&#91;0x19&#93; (Intel(R) Turbo Boost Technology) == 0x0)) or (SocketPowerManagementConfig&#91;0xB8&#93; (PL2 Limit) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PL2 Time Window

Type: `Numeric`. Offset: `0x54425`.

Firmware help: PL2 value in seconds. The value may vary from 0 to 56. Indicates the time window over which TDP value should be maintained. If the value is 0, the fused value will be programmed.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 1; store 0x1: 1.

Size: 8; Min: 0x0; Max: 0x38; Step: 0x1.

Question ID: `0x14C7`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xBE`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x542AB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x543DD`: (((SocketPowerManagementConfig&#91;0x5&#93; (Enhanced Intel SpeedStep(R) Tech) == 0x0) or (SocketPowerManagementConfig&#91;0x19&#93; (Intel(R) Turbo Boost Technology) == 0x0)) or (SocketPowerManagementConfig&#91;0xB8&#93; (PL2 Limit) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
