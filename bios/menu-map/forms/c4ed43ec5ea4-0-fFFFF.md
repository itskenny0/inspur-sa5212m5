# (untitled form)

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; **

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0xFFFF`, PE/section offset `0x54BD4`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Controls and information

### (internal OneOf, Q0xDFF1)

Type: `OneOf`. Offset: `0x54BDE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
|  | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x0; Step: 0x0.

Question ID: `0xDFF1`. Question flags: `0x4` (callback).

Storage: `SocketCommonRcConfig` at byte offset `0xD`, GUID `4402CA38-808F-4279-BCEC-5BAF8D59092F`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x54BDA`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal OneOf, Q0xDFF2)

Type: `OneOf`. Offset: `0x54BF8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
|  | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x0; Step: 0x0.

Question ID: `0xDFF2`. Question flags: `0x4` (callback).

Storage: `SocketCommonRcConfig` at byte offset `0xC`, GUID `4402CA38-808F-4279-BCEC-5BAF8D59092F`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x54BDA`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal OneOf, Q0xDFF3)

Type: `OneOf`. Offset: `0x54C12`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
|  | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x0; Step: 0x0.

Question ID: `0xDFF3`. Question flags: `0x4` (callback).

Storage: `SocketIioConfig` at byte offset `0xE40`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x54BDA`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal OneOf, Q0xDFF4)

Type: `OneOf`. Offset: `0x54C2C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
|  | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x0; Step: 0x0.

Question ID: `0xDFF4`. Question flags: `0x4` (callback).

Storage: `SocketMemoryConfig` at byte offset `0x63`, GUID `98CF19ED-4109-4681-B79D-9196757C7824`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x54BDA`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal OneOf, Q0xDFF5)

Type: `OneOf`. Offset: `0x54C46`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
|  | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x0; Step: 0x0.

Question ID: `0xDFF5`. Question flags: `0x4` (callback).

Storage: `SocketProcessorCoreConfig` at byte offset `0x26`, GUID `07013588-C789-4E12-A7C3-88FAFAE79F7C`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x54BDA`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x14FC)

Type: `Numeric`. Offset: `0x54C66`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x14FC`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketSystemAccess` at byte offset `0x0`, GUID `07013588-C789-4E12-A7C3-88FAFAE79F7C`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `DisableIf` at `0x54C62`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x14FD)

Type: `Numeric`. Offset: `0x54C79`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x14FD`. Question flags: `0x0` (none of the decoded flags).

Storage: `InspurSocketSetupFeatures` at byte offset `0x1`, GUID `07013588-C789-4E12-A7C3-88FAFAE79F7C`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `DisableIf` at `0x54C62`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x14FE)

Type: `Numeric`. Offset: `0x54C8C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x14FE`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xB6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `DisableIf` at `0x54C62`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x14FF)

Type: `Numeric`. Offset: `0x54C9F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x14FF`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xB5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `DisableIf` at `0x54C62`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x1500)

Type: `Numeric`. Offset: `0x54CB2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x1500`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xB4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `DisableIf` at `0x54C62`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x1501)

Type: `Numeric`. Offset: `0x54CC5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x1501`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xB3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `DisableIf` at `0x54C62`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x1502)

Type: `Numeric`. Offset: `0x54CD8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x1502`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xB2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `DisableIf` at `0x54C62`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x1503)

Type: `Numeric`. Offset: `0x54CEB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x1503`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xB1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `DisableIf` at `0x54C62`: 0x1. Expression result: stock true; CMOS unlock true.
