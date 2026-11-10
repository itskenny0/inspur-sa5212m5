# Intel(R) VMD for Volume Management Device on Socket 1

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; Intel(R) VMD technology &gt; Intel(R) VMD for Volume Management Device on Socket 1**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6C2`, PE/section offset `0xCCBB`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Intel(R) VMD technology](c4ed43ec5ea4-0-f6C0.md) via Intel(R) VMD for Volume Management Device on Socket 1, offset `0xC615`.

## Controls and information

### VMD Config for PStack0

Type: `Subtitle`. Offset: `0xCCC9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack0

Type: `OneOf`. Offset: `0xCCDB`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD57`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1A

Type: `OneOf`. Offset: `0xCD04`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD6C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1B

Type: `OneOf`. Offset: `0xCD25`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD6D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1C

Type: `OneOf`. Offset: `0xCD46`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD6E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1D

Type: `OneOf`. Offset: `0xCD67`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD6F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xCD88`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 1A-1D

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x14F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD93`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xCDA9`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x150`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD9F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xCDD5`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x151`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCDC8`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xCDFE`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x152`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCDF1`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xCE28`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x153`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xCE47`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x154`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xCE6F`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x155`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDCF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xCE9B`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x156`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCE8E`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xCED2`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x157`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCCC1`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCCFC`: (SocketIioConfig&#91;0xD57&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCEC5`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD Config for PStack1

Type: `Subtitle`. Offset: `0xCF0A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for Pstack1

Type: `OneOf`. Offset: `0xCF1C`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x158`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD58`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2A

Type: `OneOf`. Offset: `0xCF45`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x159`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD70`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2B

Type: `OneOf`. Offset: `0xCF66`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x15A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD71`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2C

Type: `OneOf`. Offset: `0xCF87`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x15B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD72`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2D

Type: `OneOf`. Offset: `0xCFA8`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x15C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD73`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xCFC9`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 2A-2D

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x15D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD94`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xCFEA`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x15E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD016`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x15F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD009`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD03F`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x160`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD032`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xD069`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x161`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xD088`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x162`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xD0B0`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x163`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD0DC`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x164`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD0CF`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD113`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x165`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xCF02`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xCF3D`: (SocketIioConfig&#91;0xD58&#93; (Intel(R) VMD for Volume Management Device for Pstack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD106`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD Config for PStack2

Type: `Subtitle`. Offset: `0xD14B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack2

Type: `OneOf`. Offset: `0xD15D`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x166`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD59`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3A

Type: `OneOf`. Offset: `0xD186`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x167`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD74`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3B

Type: `OneOf`. Offset: `0xD1A7`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x168`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD75`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3C

Type: `OneOf`. Offset: `0xD1C8`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x169`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD76`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3D

Type: `OneOf`. Offset: `0xD1E9`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x16A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD77`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xD20A`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 3A-3D

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x16B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD95`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xD22B`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x16C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD257`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x16D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD24A`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD280`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x16E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD273`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xD2AA`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x16F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xD2C9`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x170`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xD2F1`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x171`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD31D`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x172`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD310`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD354`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x173`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xC60D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0xD143`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD17E`: (SocketIioConfig&#91;0xD59&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD347`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
