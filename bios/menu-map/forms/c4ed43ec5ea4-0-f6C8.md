# Socket 2, Device Hide Menu

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; IIO DFX Configuration &gt; Socket 2, Device Hide Menu**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6C8`, PE/section offset `0x106E5`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [IIO DFX Configuration](c4ed43ec5ea4-0-f6C5.md) via Socket 2, Device Hide Menu, offset `0xF561`.

## Controls and information

### C-Stack Devhide0

Type: `Numeric`. Offset: `0x106F3`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2AF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFC9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide1

Type: `Numeric`. Offset: `0x10721`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFCD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide2

Type: `Numeric`. Offset: `0x1074F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFD1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide3

Type: `Numeric`. Offset: `0x1077D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFD5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide4

Type: `Numeric`. Offset: `0x107AB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFD9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide5

Type: `Numeric`. Offset: `0x107D9`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFDD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide6

Type: `Numeric`. Offset: `0x10807`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFE1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide7

Type: `Numeric`. Offset: `0x10835`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFE5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide0

Type: `Numeric`. Offset: `0x10863`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFE9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide1

Type: `Numeric`. Offset: `0x10891`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFED`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide2

Type: `Numeric`. Offset: `0x108BF`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2B9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFF1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide3

Type: `Numeric`. Offset: `0x108ED`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2BA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFF5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide4

Type: `Numeric`. Offset: `0x1091B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2BB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFF9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide5

Type: `Numeric`. Offset: `0x10949`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2BC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xFFD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide6

Type: `Numeric`. Offset: `0x10977`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2BD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1001`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide7

Type: `Numeric`. Offset: `0x109A5`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2BE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1005`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide0

Type: `Numeric`. Offset: `0x109D3`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2BF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1009`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide1

Type: `Numeric`. Offset: `0x10A01`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x100D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide2

Type: `Numeric`. Offset: `0x10A2F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1011`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide3

Type: `Numeric`. Offset: `0x10A5D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1015`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide4

Type: `Numeric`. Offset: `0x10A8B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1019`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide5

Type: `Numeric`. Offset: `0x10AB9`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x101D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide6

Type: `Numeric`. Offset: `0x10AE7`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1021`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide7

Type: `Numeric`. Offset: `0x10B15`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1025`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide0

Type: `Numeric`. Offset: `0x10B43`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1029`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide1

Type: `Numeric`. Offset: `0x10B71`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x102D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide2

Type: `Numeric`. Offset: `0x10B9F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2C9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1031`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide3

Type: `Numeric`. Offset: `0x10BCD`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2CA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1035`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide4

Type: `Numeric`. Offset: `0x10BFB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2CB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1039`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide5

Type: `Numeric`. Offset: `0x10C29`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2CC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x103D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide6

Type: `Numeric`. Offset: `0x10C57`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2CD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1041`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide7

Type: `Numeric`. Offset: `0x10C85`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2CE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1045`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide0

Type: `Numeric`. Offset: `0x10CB3`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2CF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1049`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide1

Type: `Numeric`. Offset: `0x10CE1`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x104D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide2

Type: `Numeric`. Offset: `0x10D0F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1051`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide3

Type: `Numeric`. Offset: `0x10D3D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1055`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide4

Type: `Numeric`. Offset: `0x10D6B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1059`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide5

Type: `Numeric`. Offset: `0x10D99`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x105D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide6

Type: `Numeric`. Offset: `0x10DC7`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1061`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide7

Type: `Numeric`. Offset: `0x10DF5`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1065`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide0

Type: `Numeric`. Offset: `0x10E23`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1069`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide1

Type: `Numeric`. Offset: `0x10E51`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x106D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide2

Type: `Numeric`. Offset: `0x10E7F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2D9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1071`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide3

Type: `Numeric`. Offset: `0x10EAD`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2DA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1075`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide4

Type: `Numeric`. Offset: `0x10EDB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2DB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1079`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide5

Type: `Numeric`. Offset: `0x10F09`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2DC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x107D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide6

Type: `Numeric`. Offset: `0x10F37`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2DD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1081`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide7

Type: `Numeric`. Offset: `0x10F65`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x2DE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1085`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0x106EB`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
