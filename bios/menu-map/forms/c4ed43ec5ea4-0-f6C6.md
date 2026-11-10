# Socket 0, Device Hide Menu

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; IIO DFX Configuration &gt; Socket 0, Device Hide Menu**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6C6`, PE/section offset `0xF581`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [IIO DFX Configuration](c4ed43ec5ea4-0-f6C5.md) via Socket 0, Device Hide Menu, offset `0xF543`.

## Controls and information

### C-Stack Devhide0

Type: `Numeric`. Offset: `0xF58F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x24F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE49`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide1

Type: `Numeric`. Offset: `0xF5BD`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x250`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE4D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide2

Type: `Numeric`. Offset: `0xF5EB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x251`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE51`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide3

Type: `Numeric`. Offset: `0xF619`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x252`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE55`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide4

Type: `Numeric`. Offset: `0xF647`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x253`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE59`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide5

Type: `Numeric`. Offset: `0xF675`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x254`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE5D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide6

Type: `Numeric`. Offset: `0xF6A3`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x255`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE61`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### C-Stack Devhide7

Type: `Numeric`. Offset: `0xF6D1`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x256`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE65`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide0

Type: `Numeric`. Offset: `0xF6FF`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x257`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE69`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide1

Type: `Numeric`. Offset: `0xF72D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x258`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE6D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide2

Type: `Numeric`. Offset: `0xF75B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x259`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE71`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide3

Type: `Numeric`. Offset: `0xF789`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x25A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE75`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide4

Type: `Numeric`. Offset: `0xF7B7`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x25B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE79`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide5

Type: `Numeric`. Offset: `0xF7E5`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x25C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE7D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide6

Type: `Numeric`. Offset: `0xF813`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x25D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE81`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack0 Devhide7

Type: `Numeric`. Offset: `0xF841`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x25E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE85`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide0

Type: `Numeric`. Offset: `0xF86F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x25F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE89`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide1

Type: `Numeric`. Offset: `0xF89D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x260`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE8D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide2

Type: `Numeric`. Offset: `0xF8CB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x261`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE91`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide3

Type: `Numeric`. Offset: `0xF8F9`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x262`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE95`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide4

Type: `Numeric`. Offset: `0xF927`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x263`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE99`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide5

Type: `Numeric`. Offset: `0xF955`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x264`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE9D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack1 Devhide6

Type: `Numeric`. Offset: `0xF983`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x265`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEA1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide7

Type: `Numeric`. Offset: `0xF9B1`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x266`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEA5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide0

Type: `Numeric`. Offset: `0xF9DF`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x267`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEA9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide1

Type: `Numeric`. Offset: `0xFA0D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x268`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEAD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide2

Type: `Numeric`. Offset: `0xFA3B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x269`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEB1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide3

Type: `Numeric`. Offset: `0xFA69`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x26A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEB5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide4

Type: `Numeric`. Offset: `0xFA97`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x26B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEB9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide5

Type: `Numeric`. Offset: `0xFAC5`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x26C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEBD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide6

Type: `Numeric`. Offset: `0xFAF3`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x26D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEC1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### P-Stack2 Devhide7

Type: `Numeric`. Offset: `0xFB21`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x26E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEC5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide0

Type: `Numeric`. Offset: `0xFB4F`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x26F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEC9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide1

Type: `Numeric`. Offset: `0xFB7D`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x270`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xECD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide2

Type: `Numeric`. Offset: `0xFBAB`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x271`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xED1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide3

Type: `Numeric`. Offset: `0xFBD9`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x272`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xED5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide4

Type: `Numeric`. Offset: `0xFC07`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x273`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xED9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide5

Type: `Numeric`. Offset: `0xFC35`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x274`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEDD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide6

Type: `Numeric`. Offset: `0xFC63`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x275`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEE1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP0-Stack Devhide7

Type: `Numeric`. Offset: `0xFC91`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x276`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEE5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide0

Type: `Numeric`. Offset: `0xFCBF`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x277`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEE9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide1

Type: `Numeric`. Offset: `0xFCED`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x278`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEED`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide2

Type: `Numeric`. Offset: `0xFD1B`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x279`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEF1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide3

Type: `Numeric`. Offset: `0xFD49`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x27A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEF5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide4

Type: `Numeric`. Offset: `0xFD77`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x27B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEF9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide5

Type: `Numeric`. Offset: `0xFDA5`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x27C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xEFD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide6

Type: `Numeric`. Offset: `0xFDD3`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x27D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xF01`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MCP1-Stack Devhide7

Type: `Numeric`. Offset: `0xFE01`.

Firmware help: If entire DEVHIDEx is 0, then register will not be modified. If any byte is non-zero, then the entire DEVHIDE register will be overridden with these values (thus overriding any other HIDE option in setup such as PCIe port hide questions).

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 0; store 0x1: 0.

Size: 32; Min: 0x0; Max: 0xFFFFFFFF; Step: 0x0.

Question ID: `0x27E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xF05`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF587`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
