# Intel(R) VMD for Volume Management Device on Socket 3

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Intel(R) VMD for Volume Management Device on Socket 3**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6C4`, PE/section offset `0xDA51`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Controls and information

### VMD Config for PStack0

Type: `Subtitle`. Offset: `0xDA5F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack0

Type: `OneOf`. Offset: `0xDA71`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x19E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD5D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1A

Type: `OneOf`. Offset: `0xDA9A`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x19F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD84`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1B

Type: `OneOf`. Offset: `0xDABB`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1A0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD85`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1C

Type: `OneOf`. Offset: `0xDADC`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1A1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD86`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1D

Type: `OneOf`. Offset: `0xDAFD`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1A2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD87`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xDB1E`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 1A-1D

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1A3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD99`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xDB3F`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x1A4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xDB6B`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x1A5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDB5E`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xDB94`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1A6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDB87`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xDBBE`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x1A7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDBD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xDBDD`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1A8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xDC05`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x1A9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xDC31`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1AA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDE1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDC24`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xDC68`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x1AB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDE1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDA57`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA92`: (SocketIioConfig&#91;0xD5D&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDC5B`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD Config for PStack1

Type: `Subtitle`. Offset: `0xDCA0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack1

Type: `OneOf`. Offset: `0xDCB2`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1AC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD5E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2A

Type: `OneOf`. Offset: `0xDCDB`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1AD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD88`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2B

Type: `OneOf`. Offset: `0xDCFC`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1AE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD89`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2C

Type: `OneOf`. Offset: `0xDD1D`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1AF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD8A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2D

Type: `OneOf`. Offset: `0xDD3E`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1B0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD8B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xDD5F`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 2A-2D

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1B1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD9A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xDD80`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x1B2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xDDAC`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x1B3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDD9F`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xDDD5`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1B4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDDC8`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xDDFF`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x1B5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDBE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xDE1E`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1B6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDCA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xDE46`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x1B7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xDE72`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1B8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDE2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDE65`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xDEA9`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x1B9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDE2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDC98`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDCD3`: (SocketIioConfig&#91;0xD5E&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDE9C`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD Config for PStack2

Type: `Subtitle`. Offset: `0xDEE1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack2

Type: `OneOf`. Offset: `0xDEF3`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1BA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD5F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3A

Type: `OneOf`. Offset: `0xDF1C`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1BB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD8C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3B

Type: `OneOf`. Offset: `0xDF3D`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1BC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD8D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3C

Type: `OneOf`. Offset: `0xDF5E`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1BD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD8E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3D

Type: `OneOf`. Offset: `0xDF7F`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1BE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD8F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xDFA0`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 3A-3D

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1BF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD9B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xDFC1`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x1C0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xDFED`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x1C1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDFE0`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xE016`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1C2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE009`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xE040`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x1C3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDBF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xE05F`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1C4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDCB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xE087`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x1C5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xE0B3`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x1C6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDE3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE0A6`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xE0EA`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x1C7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDE3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xDED9`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDF14`: (SocketIioConfig&#91;0xD5F&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xE0DD`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
