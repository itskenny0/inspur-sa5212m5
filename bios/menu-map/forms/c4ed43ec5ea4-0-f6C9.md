# Socket 3, Device Hide Menu

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; IIO DFX Configuration &gt; Socket 3, Device Hide Menu**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6C9`, PE/section offset `0x10F97`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [IIO DFX Configuration](c4ed43ec5ea4-0-f6C5.md) via Socket 3, Device Hide Menu, offset `0xF570`.

## Controls and information

### C-Stack Devhide0

Type: `Numeric`. Offset: `0x10FA5`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2DF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1089`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide1

Type: `Numeric`. Offset: `0x10FD3`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x108D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide2

Type: `Numeric`. Offset: `0x11001`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1091`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide3

Type: `Numeric`. Offset: `0x1102F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1095`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide4

Type: `Numeric`. Offset: `0x1105D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1099`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide5

Type: `Numeric`. Offset: `0x1108B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x109D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide6

Type: `Numeric`. Offset: `0x110B9`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10A1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide7

Type: `Numeric`. Offset: `0x110E7`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10A5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide0

Type: `Numeric`. Offset: `0x11115`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10A9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide1

Type: `Numeric`. Offset: `0x11143`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10AD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide2

Type: `Numeric`. Offset: `0x11171`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2E9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10B1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide3

Type: `Numeric`. Offset: `0x1119F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2EA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10B5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide4

Type: `Numeric`. Offset: `0x111CD`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2EB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10B9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide5

Type: `Numeric`. Offset: `0x111FB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2EC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10BD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide6

Type: `Numeric`. Offset: `0x11229`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2ED`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10C1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide7

Type: `Numeric`. Offset: `0x11257`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2EE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10C5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide0

Type: `Numeric`. Offset: `0x11285`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2EF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10C9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide1

Type: `Numeric`. Offset: `0x112B3`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10CD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide2

Type: `Numeric`. Offset: `0x112E1`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10D1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide3

Type: `Numeric`. Offset: `0x1130F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10D5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide4

Type: `Numeric`. Offset: `0x1133D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10D9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide5

Type: `Numeric`. Offset: `0x1136B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10DD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide6

Type: `Numeric`. Offset: `0x11399`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10E1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide7

Type: `Numeric`. Offset: `0x113C7`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10E5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide0

Type: `Numeric`. Offset: `0x113F5`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10E9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide1

Type: `Numeric`. Offset: `0x11423`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10ED`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide2

Type: `Numeric`. Offset: `0x11451`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2F9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10F1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide3

Type: `Numeric`. Offset: `0x1147F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2FA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10F5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide4

Type: `Numeric`. Offset: `0x114AD`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2FB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10F9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide5

Type: `Numeric`. Offset: `0x114DB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2FC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10FD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide6

Type: `Numeric`. Offset: `0x11509`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2FD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1101`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide7

Type: `Numeric`. Offset: `0x11537`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2FE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1105`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide0

Type: `Numeric`. Offset: `0x11565`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2FF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1109`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide1

Type: `Numeric`. Offset: `0x11593`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x300`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x110D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide2

Type: `Numeric`. Offset: `0x115C1`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x301`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1111`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide3

Type: `Numeric`. Offset: `0x115EF`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x302`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1115`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide4

Type: `Numeric`. Offset: `0x1161D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x303`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1119`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide5

Type: `Numeric`. Offset: `0x1164B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x304`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x111D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide6

Type: `Numeric`. Offset: `0x11679`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x305`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1121`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide7

Type: `Numeric`. Offset: `0x116A7`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x306`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1125`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide0

Type: `Numeric`. Offset: `0x116D5`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x307`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1129`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide1

Type: `Numeric`. Offset: `0x11703`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x308`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x112D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide2

Type: `Numeric`. Offset: `0x11731`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x309`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1131`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide3

Type: `Numeric`. Offset: `0x1175F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x30A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1135`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide4

Type: `Numeric`. Offset: `0x1178D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x30B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1139`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide5

Type: `Numeric`. Offset: `0x117BB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x30C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x113D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide6

Type: `Numeric`. Offset: `0x117E9`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x30D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1141`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide7

Type: `Numeric`. Offset: `0x11817`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x30E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1145`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x10F9D`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
