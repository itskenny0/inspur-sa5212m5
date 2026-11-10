# Intel(R) VMD for Volume Management Device on Socket 2

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Intel(R) VMD for Volume Management Device on Socket 2**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6C3`, PE/section offset `0xD386`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Controls and information

### VMD Config for PStack0

Type: `Subtitle`. Offset: `0xD394`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack0

Type: `OneOf`. Offset: `0xD3A6`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x174`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD5A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1A

Type: `OneOf`. Offset: `0xD3CF`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x175`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD78`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1B

Type: `OneOf`. Offset: `0xD3F0`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x176`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD79`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1C

Type: `OneOf`. Offset: `0xD411`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x177`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD7A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 1D

Type: `OneOf`. Offset: `0xD432`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x178`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD7B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xD453`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 1A-1D

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x179`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD96`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xD474`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x17A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD4A0`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x17B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD493`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD4C9`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x17C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD4BC`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xD4F3`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x17D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDBA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xD512`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x17E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xD53A`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x17F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD566`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x180`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD559`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD59D`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x181`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD38C`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD3C7`: (SocketIioConfig&#91;0xD5A&#93; (Intel(R) VMD for Volume Management Device for PStack0) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD590`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD Config for PStack1

Type: `Subtitle`. Offset: `0xD5D5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack1

Type: `OneOf`. Offset: `0xD5E7`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x182`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD5B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2A

Type: `OneOf`. Offset: `0xD610`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x183`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD7C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2B

Type: `OneOf`. Offset: `0xD631`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x184`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD7D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2C

Type: `OneOf`. Offset: `0xD652`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x185`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD7E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 2D

Type: `OneOf`. Offset: `0xD673`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x186`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD7F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xD694`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 2A-2D

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x187`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD97`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xD6B5`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x188`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD6E1`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x189`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD6D4`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD70A`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x18A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDAF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD6FD`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xD734`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x18B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDBB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xD753`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x18C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xD77B`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x18D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD7A7`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x18E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD79A`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD7DE`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x18F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDDF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD5CD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD608`: (SocketIioConfig&#91;0xD5B&#93; (Intel(R) VMD for Volume Management Device for PStack1) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD7D1`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD Config for PStack2

Type: `Subtitle`. Offset: `0xD816`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Intel(R) VMD for Volume Management Device for PStack2

Type: `OneOf`. Offset: `0xD828`.

Firmware help: Enable/Disable Intel(R) Volume Management Device Technology in this Stack.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x190`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD5C`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3A

Type: `OneOf`. Offset: `0xD851`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x191`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD80`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3B

Type: `OneOf`. Offset: `0xD872`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x192`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD81`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3C

Type: `OneOf`. Offset: `0xD893`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x193`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD82`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### VMD port 3D

Type: `OneOf`. Offset: `0xD8B4`.

Firmware help: Enable/Disable Intel® Volume Management Device Technology on specific root port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x194`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD83`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0xD8D5`.

Firmware help: Enable/Disable Hot Plug for PCIe Root Ports 3A-3D

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x195`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD98`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar size

Type: `Numeric`. Offset: `0xD8F6`.

Firmware help: Setup VMD Config BAR size (in bits Min=20, Max=27), ex: 20bits=1MB, 27bits=128MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x1B; Step: 0x1.

Question ID: `0x196`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDA4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD922`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x2; Max: 0x2; Step: 0x0.

Question ID: `0x197`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD915`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### CfgBar attribute

Type: `OneOf`. Offset: `0xD94B`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x198`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDB0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD93E`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 size

Type: `Numeric`. Offset: `0xD975`.

Firmware help: Setup VMD Memory BAR1 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 25; store 0x1: 25.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x199`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDBC`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar1 attribute

Type: `OneOf`. Offset: `0xD994`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | standard, manufacturing | none |
| 64-bit non-prefetchable | 1 | none | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x19A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDC8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 size

Type: `Numeric`. Offset: `0xD9BC`.

Firmware help: Setup VMD Memory BAR2 size (in bits Min=20), ex: 20bits=1MB, 22bits=4MB, 26bits=64MB

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 20; store 0x1: 20.

Size: 8; Min: 0x14; Max: 0x27; Step: 0x1.

Question ID: `0x19B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDD4`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xD9E8`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 32-bit non-prefetchable | 0 | none | none |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x19C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDE0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD9DB`: (SocketCommonRcConfig&#91;0xC&#93; &gt;= 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MemBar2 attribute

Type: `OneOf`. Offset: `0xDA1F`.

Firmware help: Set up VMD Config BAR attribute, like 64-bit or prefetchable

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 64-bit non-prefetchable | 1 | standard, manufacturing | none |
| 64-bit prefetchable | 2 | none | none |

Size: 8; Min: 0x1; Max: 0x2; Step: 0x0.

Question ID: `0x19D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDE0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0xD80E`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xD849`: (SocketIioConfig&#91;0xD5C&#93; (Intel(R) VMD for Volume Management Device for PStack2) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xDA12`: (SocketCommonRcConfig&#91;0xC&#93; &lt; 0x3). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
