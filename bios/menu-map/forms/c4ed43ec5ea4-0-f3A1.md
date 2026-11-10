# Energy Perf BIAS

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; CPU - Advanced PM Tuning &gt; Energy Perf BIAS**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3A1`, PE/section offset `0x53C9E`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [CPU - Advanced PM Tuning](c4ed43ec5ea4-0-f3A0.md) via Energy Perf BIAS, offset `0x53C58`.

## Controls and information

### Energy Perf BIAS

Type: `Subtitle`. Offset: `0x53CA4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Power Performance Tuning

Type: `OneOf`. Offset: `0x53CC6`.

Firmware help: MSR 1FCh Bit&#91;25&#93; = PWR_PERF_TUNING_CFG_MODE. Enable - Use IA32_ENERGY_PERF_BIAS input from the core; Disable - Use alternate perf BIAS input from ENERGY_PERF_BIAS_CONFIG

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| OS Controls EPB | 0 | none | none |
| BIOS Controls EPB | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x149B`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x48`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CB6`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53CBE`: (SocketPowerManagementConfig&#91;0xA&#93; (Hardware P-States) == 0x2). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PECI PCS EPB

Type: `OneOf`. Offset: `0x53D03`.

Firmware help: Controls whether PECI has control over EPB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| OS controls EPB | 0 | standard, manufacturing | none |
| PECI controls EPB using PCS | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x149C`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x13`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CB6`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53CE9`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CF1`: ((SocketPowerManagementConfig&#91;0x48&#93; (Power Performance Tuning) == 0x1) or (SocketPowerManagementConfig&#91;0xA&#93; (Hardware P-States) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Energy Performance BIAS Setting

Type: `OneOf`. Offset: `0x53D30`.

Firmware help: Use input from ENERGY_PERF_BIAS_CONFIG mode selection. PERF/Balanced Perf/Balanced Power/Power

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Performance | 0 | none | none |
| Balanced Performance | 7 | standard, manufacturing | none |
| Balanced Power | 8 | none | none |
| Power | 15 | none | none |

Size: 8; Min: 0x0; Max: 0xF; Step: 0x0.

Question ID: `0x149D`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x49`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CB6`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x53D28`: (SocketPowerManagementConfig&#91;0x48&#93; (Power Performance Tuning) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Dynamic Loadline Switch

Type: `OneOf`. Offset: `0x53D69`.

Firmware help: Dynamic Loadline Switch control. MSR 0x1FC&#91;Bit24&#93;

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x149E`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x4A`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CB6`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53D61`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Workload Configuration

Type: `OneOf`. Offset: `0x53D8C`.

Firmware help: Optimization for the workload characterization. Balanced is recommended.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| UMA | 0 | standard, manufacturing | none |
| NUMA | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x149F`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x4B`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CB6`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Averaging Time Window

Type: `Numeric`. Offset: `0x53DB5`.

Firmware help: This is used to control the effective window of the average for C0 an P0 time

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 23; store 0x1: 23.

Size: 16; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x14A0`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x4C`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CB6`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53DAD`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P0 TotalTimeThreshold Low

Type: `Numeric`. Offset: `0x53DD9`.

Firmware help: The HW switching mechanism DISABLES the performance setting (0) when the total P0 time is less than this threshold

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 35; store 0x1: 35.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x0.

Question ID: `0x14A1`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x50`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CB6`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53DAD`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P0 TotalTimeThreshold High

Type: `Numeric`. Offset: `0x53DF8`.

Firmware help: The HW switching mechanism ENABLES the performance setting (0) when the total P0 time is greater than this threshold

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 58; store 0x1: 58.

Size: 8; Min: 0x0; Max: 0x3F; Step: 0x0.

Question ID: `0x14A2`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x51`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53CB6`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53DAD`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
