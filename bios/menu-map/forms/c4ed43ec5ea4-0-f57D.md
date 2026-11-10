# Page Policy

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Memory Configuration &gt; Page Policy**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x57D`, PE/section offset `0x50BC5`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Memory Configuration](c4ed43ec5ea4-0-f540.md) via Page Policy, offset `0x50A55`.

## Controls and information

### Page Policy

Type: `OneOf`. Offset: `0x50BD3`.

Firmware help: Select Page Policy

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 3 | standard, manufacturing | none |
| Closed | 1 | none | none |
| Adaptive | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x3; Step: 0x0.

Question ID: `0x1385`. Question flags: `0x10` (reset required).

Storage: `SocketMemoryConfig` at byte offset `0x6`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x50A4D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x50BCB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
