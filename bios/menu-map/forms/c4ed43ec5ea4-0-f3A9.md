# Perf P-Limit

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; CPU P State Control &gt; Perf P-Limit**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3A9`, PE/section offset `0x5416C`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [CPU P State Control](c4ed43ec5ea4-0-f380.md) via Perf P-Limit, offset `0x5337B`.

## Controls and information

### Perf P-Limit

Type: `Subtitle`. Offset: `0x54172`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x53114`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5331F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Perf P-Limit Differential

Type: `Numeric`. Offset: `0x5418C`.

Firmware help: Parameter used to tune how far below local socket frequency remote socket frequency is allowed to be. Also impacts rate at which frequency drops when feature disengages.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 1; store 0x1: 1.

Size: 8; Min: 0x0; Max: 0x7; Step: 0x0.

Question ID: `0x14B8`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x9A`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x53114`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5331F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54184`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Perf P-Limit Clip

Type: `Numeric`. Offset: `0x541AB`.

Firmware help: Maximum value the floor is allowed to be set to for perf P-limit.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 31; store 0x1: 31.

Size: 8; Min: 0x0; Max: 0x1F; Step: 0x0.

Question ID: `0x14B9`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x9B`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x53114`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5331F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54184`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Perf P-Limit Threshold

Type: `Numeric`. Offset: `0x541CA`.

Firmware help: Uncore frequency threshold above which this socket will trigger the feature and start trying to raise frequency of other sockets.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 15; store 0x1: 15.

Size: 8; Min: 0x0; Max: 0x1F; Step: 0x0.

Question ID: `0x14BA`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x77`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x53114`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5331F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54184`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Perf P Limit

Type: `OneOf`. Offset: `0x541E9`.

Firmware help: Enable/Disable Performance P-Limit

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14BB`. Question flags: `0x10` (reset required).

Storage: `SocketPowerManagementConfig` at byte offset `0x99`, GUID `A1047342-BDBA-4DAE-A67A-40979B65C7F8`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x53114`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x5331F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x54184`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
