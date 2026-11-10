# DRAM RAPL Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; Memory Power &amp; Thermal Configuration &gt; DRAM RAPL Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3B0`, PE/section offset `0x5420E`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Memory Power &amp; Thermal Configuration](c4ed43ec5ea4-0-f582.md) via DRAM RAPL Configuration, offset `0x50DB7`.

## Controls and information

### DRAM RAPL Configuration

Type: `Subtitle`. Offset: `0x54214`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Override BW_LIMIT_TF

Type: `Numeric`. Offset: `0x5422E`.

Firmware help: Allows custom tuning of BW_LIMIT_TF when DRAM RAPL is enabled

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 8; Min: 0x0; Max: 0x10; Step: 0x1.

Question ID: `0x14BC`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xCB`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54226`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DRAM RAPL Extended Range

Type: `OneOf`. Offset: `0x5424D`.

Firmware help: Select DRAM RAPL Extended Range

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14BD`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xCD`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54226`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CMS ENABLE DRAM PM

Type: `OneOf`. Offset: `0x5426E`.

Firmware help: CMS ENABLE DRAM PM

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14BE`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0xCE`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54226`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
