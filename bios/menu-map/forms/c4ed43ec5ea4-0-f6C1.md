# Intel(R) VMD for Volume Management Device on Socket 0

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; Intel(R) VMD technology &gt; Intel(R) VMD for Volume Management Device on Socket 0**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6C1`, PE/section offset `0xC628`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Intel(R) VMD technology](c4ed43ec5ea4-0-f6C0.md) via Intel(R) VMD for Volume Management Device on Socket 0, offset `0xC5FC`.

## Controls and information

### VMD Config for PStack0

Type: `Subtitle`. Offset: `0xC636`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack0

Type: `OneOf`. Offset: `0xC648`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x121`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD54`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1A

Type: `OneOf`. Offset: `0xC671`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x122`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD60`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1B

Type: `OneOf`. Offset: `0xC692`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x123`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD61`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1C

Type: `OneOf`. Offset: `0xC6B3`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x124`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD62`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1D

Type: `OneOf`. Offset: `0xC6D4`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x125`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD63`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xC6F5`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 1A-1D

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x126`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD90`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xC716`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x127`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD9C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xC742`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x128`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC735`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xC76B`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x129`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC75E`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xC795`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x12A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xC7B4`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x12B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xC7DC`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x12C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDCC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xC7FB`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x12D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC62E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC669`: (SocketIioConfig&#91;0xD54&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD Config for PStack1

Type: `Subtitle`. Offset: `0xC838`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack1

Type: `OneOf`. Offset: `0xC84A`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x12E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD55`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2A

Type: `OneOf`. Offset: `0xC873`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x12F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD64`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2B

Type: `OneOf`. Offset: `0xC894`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x130`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD65`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2C

Type: `OneOf`. Offset: `0xC8B5`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x131`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD66`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2D

Type: `OneOf`. Offset: `0xC8D6`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x132`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD67`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xC8F7`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 2A-2D

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x133`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD91`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xC918`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x134`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD9D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xC944`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x135`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC937`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xC96D`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x136`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC960`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xC997`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x137`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xC9B6`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x138`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xC9DE`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x139`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDCD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xCA0A`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x13A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC9FD`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xCA41`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x13B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xC830`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xC86B`: (SocketIioConfig&#91;0xD55&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCA34`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD Config for PStack2

Type: `Subtitle`. Offset: `0xCA79`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack2

Type: `OneOf`. Offset: `0xCA8B`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD56`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3A

Type: `OneOf`. Offset: `0xCAB4`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD68`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3B

Type: `OneOf`. Offset: `0xCAD5`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD69`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3C

Type: `OneOf`. Offset: `0xCAF6`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x13F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD6A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3D

Type: `OneOf`. Offset: `0xCB17`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x140`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD6B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xCB38`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 3A-3D

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x141`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD92`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xCB59`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x142`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD9E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xCB85`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x143`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCB78`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xCBBC`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x144`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCBAF`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xCBDF`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x145`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xCBFE`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x146`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xCC26`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x147`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDCE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xCC52`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x148`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCC45`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xCC89`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x149`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC5F4`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCA71`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCAAC`: (SocketIioConfig&#91;0xD56&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCC7C`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
