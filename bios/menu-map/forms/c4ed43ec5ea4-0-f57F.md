# Memory Power Savings Advanced Options

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Advanced Power Management Configuration &gt; Memory Power &amp; Thermal Configuration &gt; Memory Power Savings Advanced Options**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x57F`, PE/section offset `0x50E4E`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Memory Power &amp; Thermal Configuration](c4ed43ec5ea4-0-f582.md) via Memory Power Savings Advanced Options, offset `0x50E3B`.

## Controls and information

### CKE Throttling

Type: `OneOf`. Offset: `0x50E5C`.

Firmware help: Configures CKE Throttling

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Manual | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1394`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x44`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x50DD5`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x50E54`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CKE Feature

Type: `Ref`. Offset: `0x50E85`.

Firmware help: CKE Feature

Opens: [CKE Feature](c4ed43ec5ea4-0-f59F.md).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Question ID: `0x1395`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x50DD5`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x50E54`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x50E7D`: (SocketMemoryConfig&#91;0x44&#93; (CKE Throttling) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### SREF Feature

Type: `OneOf`. Offset: `0x50E96`.

Firmware help: SREF Feature

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Manual | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1396`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x45`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x50DD5`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x50E54`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Self Refresh Feature

Type: `Ref`. Offset: `0x50EBF`.

Firmware help: Self Refresh Feature

Opens: [Self Refresh Feature](c4ed43ec5ea4-0-f5A0.md).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Question ID: `0x1397`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x50DD5`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x50E54`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x50EB7`: (SocketMemoryConfig&#91;0x45&#93; (SREF Feature) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PKGC SREF EN

Type: `OneOf`. Offset: `0x50ED0`.

Firmware help: PKGC SREF EN

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 1 | standard, manufacturing | none |
| Disabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1398`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x46`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x52EDE`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x50DD5`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x50E54`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
