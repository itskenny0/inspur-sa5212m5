# Flashing...

[Menu index](../README.md) | [Module index](../bdc5290bdcb5-0.md)

Path: **Recovery &gt; Proceed with flash update**

Source: `ReFlash`. Formset `80E1202E-2697-4264-9CC9-80762C3E5863`, form `0x2`, PE/section offset `0x8C57`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Recovery](bdc5290bdcb5-0-f1.md) via Proceed with flash update, offset `0x8C42`.

## Controls and information

### WARNING! System firmware is being updated.

Type: `Subtitle`. Offset: `0x8C69`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C5D`: Not((Setup&#91;0x1&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Keyboard is locked.

Type: `Subtitle`. Offset: `0x8C72`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C5D`: Not((Setup&#91;0x1&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### DO NOT TURN THE POWER OFF !!!

Type: `Subtitle`. Offset: `0x8C7B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C5D`: Not((Setup&#91;0x1&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Once firmware update is completed

Type: `Subtitle`. Offset: `0x8C84`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C5D`: Not((Setup&#91;0x1&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### press any key to reboot the system

Type: `Subtitle`. Offset: `0x8C8D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C5D`: Not((Setup&#91;0x1&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Flash update failed

Type: `Subtitle`. Offset: `0x8CA0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C98`: (Setup&#91;0x1&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Flash image invalid or not found

Type: `Subtitle`. Offset: `0x8CA9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C98`: (Setup&#91;0x1&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### System will reset in 5 seconds

Type: `Subtitle`. Offset: `0x8CB2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C98`: (Setup&#91;0x1&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Action, Q0x64)

Type: `Action`. Offset: `0x8CDA`.

Firmware help: Flash update status

Access: Hidden even with CMOS unlock on this path.

Question ID: `0x64`. Question flags: `0x4` (callback).

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8CCE`: 0x1. Expression result: stock true; CMOS unlock true.
- `SuppressIf` at `0x8CD2`: (AMICallback&#91;0x0&#93; == 0xB). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal Numeric, Q0x3)

Type: `Numeric`. Offset: `0x8CF3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 16; Min: 0x0; Max: 0xFFFF; Step: 0x0.

Question ID: `0x3`. Question flags: `0x0` (none of the decoded flags).

Storage: `AMICallback` at byte offset `0x0`, GUID `9CF0F18E-7C7D-49DE-B5AA-BBBAD6B21007`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x8CEF`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x4)

Type: `Numeric`. Offset: `0x8D09`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x4`. Question flags: `0x0` (none of the decoded flags).

Storage: `Setup` at byte offset `0x1`, GUID `80E1202E-2697-4264-9CC9-80762C3E5863`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x8CEF`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x5)

Type: `Numeric`. Offset: `0x8D1C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x5`. Question flags: `0x0` (none of the decoded flags).

Storage: `SystemAccess` at byte offset `0x0`, GUID `E770BB69-BCB4-4D04-9E97-23FF9456FEAC`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x8CEF`: 0x1. Expression result: stock true; CMOS unlock true.

### (internal Numeric, Q0x6)

Type: `Numeric`. Offset: `0x8D2F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: yes.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x6`. Question flags: `0x0` (none of the decoded flags).

Storage: `Setup` at byte offset `0x0`, GUID `80E1202E-2697-4264-9CC9-80762C3E5863`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x8BB5`: Not((Setup&#91;0x0&#93; == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x8C2E`: (Not((Setup&#91;0x1&#93; == 0x0)) or (SystemAccess&#91;0x0&#93; == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `DisableIf` at `0x8CEF`: 0x1. Expression result: stock true; CMOS unlock true.
