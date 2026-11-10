# Advanced Power Management Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x51C`, PE/section offset `0x52DDD`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Processor](c4ed43ec5ea4-0-f510.md) via Advanced Power Management Configuration, offset `0x9BD8`.

## Controls and information

### Advanced Power Management Configuration

Type: `Subtitle`. Offset: `0x52DE3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### use SPT workarounds

Type: `OneOf`. Offset: `0x52E05`.

Firmware help: Enabled: use SPT workarounds - B2P cmd MISC_WORKAROUND_ENABLE

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x143F`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0xC6`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x52DF5`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x52DFD`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### CPU P State Control

Type: `Ref`. Offset: `0x52E2A`.

Firmware help: P State Control Configuration Sub Menu, include Turbo, XE and etc.

Opens: [CPU P State Control](c4ed43ec5ea4-0-f380.md).

Access: No active IFR hide condition on this path.

Question ID: `0x1440`. Question flags: `0x0` (none of the decoded flags).

### Hardware PM State Control

Type: `Ref`. Offset: `0x52E39`.

Firmware help: Hardware P-State setting

Opens: [Hardware PM State Control](c4ed43ec5ea4-0-f385.md).

Access: No active IFR hide condition on this path.

Question ID: `0x1441`. Question flags: `0x0` (none of the decoded flags).

### Overclocking

Type: `Ref`. Offset: `0x52E50`.

Firmware help: Provide manual XE Ratio Limit setting

Opens: [Overclocking](c4ed43ec5ea4-0-f381.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1442`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### CPU C State Control

Type: `Ref`. Offset: `0x52E5F`.

Firmware help: CPU C State setting

Opens: [CPU C State Control](c4ed43ec5ea4-0-f390.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1443`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Package C State Control

Type: `Ref`. Offset: `0x52E6E`.

Firmware help: Package C State setting

Opens: [Package C State Control](c4ed43ec5ea4-0-f394.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1444`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### CPU Thermal Management

Type: `Ref`. Offset: `0x52E87`.

Firmware help: CPU Thermal Related setting

Opens: [CPU Thermal Management](c4ed43ec5ea4-0-f393.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1445`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### CPU - Advanced PM Tuning

Type: `Ref`. Offset: `0x52E96`.

Firmware help: Setting Energy Per Bias, Pwr_Ctl, PP0 Current SWLTD, SAPM etc

Opens: [CPU - Advanced PM Tuning](c4ed43ec5ea4-0-f3A0.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1446`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E7F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Package Current Config

Type: `Ref`. Offset: `0x52EAF`.

Firmware help: Program PRI_PLANE_CURT_CFG_CTRL_MSR 0x601 Sub Menu

Opens: [Package Current Config](c4ed43ec5ea4-0-f3A3.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1447`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### EPB Override Control

Type: `Ref`. Offset: `0x52EBE`.

Firmware help: Program CSR_DYNAMIC_PERF_POWER_CTL 1:10:2:0x64 Sub Menu

Opens: [EPB Override Control](c4ed43ec5ea4-0-f3A7.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1448`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### SOCKET RAPL Config

Type: `Ref`. Offset: `0x52ECD`.

Firmware help: SOCKET RAPL Configuration Sub Menu - TURBO_POWER_LIMIT CSR &amp; MSR

Opens: [SOCKET RAPL Config](c4ed43ec5ea4-0-f3C0.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x1449`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52EA7`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PMAX CONFIG Configuration

Type: `Ref`. Offset: `0x52EE6`.

Firmware help: PMAX CONFIG Control Sub Menu

Opens: [PMAX CONFIG Configuration](c4ed43ec5ea4-0-f3E0.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x144A`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ACPI Sx State Control

Type: `Ref`. Offset: `0x52EF5`.

Firmware help: ACPI Sx State Control individually

Opens: [ACPI Sx State Control](c4ed43ec5ea4-0-f3D0.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x144B`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Memory Power &amp; Thermal Configuration

Type: `Ref`. Offset: `0x52F04`.

Firmware help: Displays and provides option to change the Memory Settings

Opens: [Memory Power &amp; Thermal Configuration](c4ed43ec5ea4-0-f582.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x144C`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
