# Pkg C-state SA Power Management Control

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; Package C State Control &gt; Pkg C-state SA Power Management Control**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x3A8`, PE/section offset `0x54134`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Package C State Control](c4ed43ec5ea4-0-f394.md) via Pkg C-state SA Power Management Control, offset `0x538B4`.

## Controls and information

### Pkg C-state SA Power Management Control

Type: `Subtitle`. Offset: `0x5413A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### CPU0 SAPMCTL_CFG

Type: `Ref`. Offset: `0x5414C`.

Firmware help: Socket Specific SAPMCTL_CFG

Opens: [CPU0 SAPMCTL_CFG](c4ed43ec5ea4-0-f3F8.md).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Question ID: `0x14B6`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### CPU1 SAPMCTL_CFG

Type: `Ref`. Offset: `0x5415B`.

Firmware help: Socket Specific SAPMCTL_CFG

Opens: [CPU1 SAPMCTL_CFG](c4ed43ec5ea4-0-f3F9.md).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Question ID: `0x14B7`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52E48`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x53790`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x53806`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
