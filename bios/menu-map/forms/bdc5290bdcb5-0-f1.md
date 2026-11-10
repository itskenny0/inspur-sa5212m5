# Recovery

[Menu index](../README.md) | [Module index](../bdc5290bdcb5-0.md)

Path: **Recovery**

Source: `ReFlash`. Formset `80E1202E-2697-4264-9CC9-80762C3E5863`, form `0x1`, PE/section offset `0x8B76`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Recovery](bdc5290bdcb5-0-f1.md) via Yes, I'm sure, offset `0x8BA2`.

## Controls and information

### Yes, I'm sure

Type: `Ref`. Offset: `0x8BA2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Opens: [Recovery](bdc5290bdcb5-0-f1.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0x66`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0x8B7C`: (Setup&#91;0x0&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8B96`: Not((Setup&#91;0x1&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Flash update is

Type: `Text`. Offset: `0x8BC9`.

Firmware provides this information field without explanatory help.

Static display text: disabled. Runtime callbacks may replace this text.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8BC1`: (SystemAccess&#91;0x0&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Reason

Type: `Text`. Offset: `0x8BD1`.

Firmware provides this information field without explanatory help.

Static display text: USER access level. Runtime callbacks may replace this text.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8BC1`: (SystemAccess&#91;0x0&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Please select blocks you want to update

Type: `Subtitle`. Offset: `0x8BDB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Reset NVRAM

Type: `CheckBox`. Offset: `0x8BF8`.

Firmware help: Set this option to reset NVRAM to default values

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 1.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0x1`. Question flags: `0x0` (none of the decoded flags).

Storage: `Setup` at byte offset `0x3`, GUID `80E1202E-2697-4264-9CC9-80762C3E5863`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x8BE4`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Boot Block Update

Type: `CheckBox`. Offset: `0x8C0E`.

Firmware help: Set this option to update boot block area of the firmware

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 1.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0x2`. Question flags: `0x0` (none of the decoded flags).

Storage: `Setup` at byte offset `0x4`, GUID `80E1202E-2697-4264-9CC9-80762C3E5863`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x8BE4`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Proceed with flash update

Type: `Ref`. Offset: `0x8C42`.

Firmware help: Select this to start flash update

Opens: [Flashing...](bdc5290bdcb5-0-f2.md).

Access: Conditional; no CMOS vendor gate on this path.

Question ID: `0x65`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
