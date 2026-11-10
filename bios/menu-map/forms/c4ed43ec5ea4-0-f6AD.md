# Socket 2 PcieBr5D01F0 - MCP 1

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Socket 2 PcieBr5D01F0 - MCP 1**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6AD`, PE/section offset `0x4248C`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Incoming references

- [Socket2 Configuration](c4ed43ec5ea4-0-f519.md) via Socket 2 PcieBr5D01F0 - MCP 1, offset `0xC08A`.

## Controls and information

### Socket 2 PcieBr5D01F0 - MCP 1

Type: `Subtitle`. Offset: `0x42492`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### PCI-E Port

Type: `OneOf`. Offset: `0x424B5`.

Firmware help: In auto mode the BIOS will remove the EXP port if there is no device or errors on that device and the device is not HP capable. Disable is used to disable the port and hide its CFG space.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0xFD2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x4AE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0x424ED`.

Firmware help: This option specifies if the link is considered Hot Plug capable.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFD3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x45`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x424DD`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x424E5`: (SocketIioConfig&#91;0x4AE&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Surprise Hot Plug Capable

Type: `OneOf`. Offset: `0x4250E`.

Firmware help: This option specifies if the link is considered Suprise Hot Plug capable.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFD4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x99`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x424DD`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x424E5`: (SocketIioConfig&#91;0x4AE&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link

Type: `OneOf`. Offset: `0x4252F`.

Firmware help: This option disables the link so that the no training occurs but the CFG space is still active.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 0 | standard, manufacturing | none |
| Disabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFD5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x112`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x424DD`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x424E5`: (SocketIioConfig&#91;0x4AE&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Link Speed

Type: `OneOf`. Offset: `0x4255C`.

Firmware help: Choose Link Speed for this PCIe port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Gen 1 (2.5 GT/s) | 1 | none | none |
| Gen 2 (5 GT/s) | 2 | none | none |
| Gen 3 (8 GT/s) | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0xFD6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x5AA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x42554`: (SocketIioConfig&#91;0x4AE&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Override Max Link Width

Type: `OneOf`. Offset: `0x42593`.

Firmware help: Override the max link width that was set by bifurcation

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| x1 | 1 | none | none |
| x2 | 2 | none | none |
| x4 | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0xFD7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x652`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x42554`: (SocketIioConfig&#91;0x4AE&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4258B`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Port DeEmphasis

Type: `OneOf`. Offset: `0x425D4`.

Firmware help: De-Emphais control (LNKCON2&#91;6&#93;) for this PCIe port.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| -6.0 dB | 0 | none | none |
| -3.5 dB | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFD8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x6A6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x42554`: (SocketIioConfig&#91;0x4AE&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x425C4`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x425CC`: (SocketIioConfig&#91;0x5AA&#93; (Link Speed) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Status

Type: `Text`. Offset: `0x425FB`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Max

Type: `Text`. Offset: `0x42603`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Speed

Type: `Text`. Offset: `0x42613`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4260B`: (SocketIioConfig&#91;0x4AE&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Clocking

Type: `OneOf`. Offset: `0x42625`.

Firmware help: Configure port clocking via LNKCON&#91;6&#93;. This refers to this components and the down stream component.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Distinct | 0 | none | none |
| Common | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFD9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x20E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4261D`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Port Max Payload Size

Type: `OneOf`. Offset: `0x42648`.

Firmware help: Set Maxpayload size to 256B if possible

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 128B | 0 | none | none |
| 256B | 1 | none | none |
| Auto | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0xFDA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x262`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port D-state

Type: `OneOf`. Offset: `0x42678`.

Firmware help: Set to D0 for normal operation, D3Hot to be in low-power state

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| D0 | 0 | standard, manufacturing | none |
| D3Hot | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFDB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x2B6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x42670`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E ASPM Support

Type: `OneOf`. Offset: `0x4269B`.

Firmware help: This option enables / disables the ASPM (L1) support for the downstream devices.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 7 | none | none |
| L1 Only | 2 | none | none |
| Disabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x7; Step: 0x0.

Question ID: `0xFDC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x166`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port L0s Exit Latency

Type: `OneOf`. Offset: `0x426D3`.

Firmware help: The length of time this port requires to complete transition from L0s to L0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 4uS - 8uS | 3 | standard, manufacturing | none |
| &lt;1uS | 0 | none | none |
| 1uS - 2uS | 1 | none | none |
| 2uS - 4uS | 2 | none | none |
| 8uS - 16uS | 4 | none | none |
| 16uS - 32uS | 5 | none | none |
| 32uS - 64uS | 6 | none | none |
| &gt;64uS | 7 | none | none |

Size: 8; Min: 0x0; Max: 0x7; Step: 0x0.

Question ID: `0xFDD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x30A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x426CB`: (SocketIioConfig&#91;0x166&#93; (PCI-E ASPM Support) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port L1 Exit Latency

Type: `OneOf`. Offset: `0x42728`.

Firmware help: The length of time this port requires to complete transition from L1 to L0

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| &lt;1uS | 0 | none | none |
| 1uS - 2uS | 1 | none | none |
| 2uS - 4uS | 2 | none | none |
| 4uS - 8uS | 3 | none | none |
| 8uS - 16uS | 4 | standard, manufacturing | none |
| 16uS - 32uS | 5 | none | none |
| 32uS - 64uS | 6 | none | none |
| &gt;64uS | 7 | none | none |

Size: 8; Min: 0x0; Max: 0x7; Step: 0x0.

Question ID: `0xFDE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x35E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x42720`: (SocketIioConfig&#91;0x166&#93; (PCI-E ASPM Support) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MSI

Type: `OneOf`. Offset: `0x42775`.

Firmware help: BUS0 DEVx FUN0 OFF 0x5A bit 0, Where X is 0-3

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFDF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x3B2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Extended Sync

Type: `OneOf`. Offset: `0x42796`.

Firmware help: Enable / disable the Extended Sync Mode (D:x F:0 O:7Ch B:7) where x is 0-9

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x406`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Compliance Mode

Type: `OneOf`. Offset: `0x427B7`.

Firmware help: Disable/Enable Compliance Mode for this PCIe port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x5FE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### EOI

Type: `OneOf`. Offset: `0x427D8`.

Firmware help: Dev 0,2,3 MISCCTRLSTS (Reg 0x188)Bit 26

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | standard, manufacturing | none |
| Enabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x6FA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Fatal Err Over

Type: `OneOf`. Offset: `0x427F9`.

Firmware help: Enables forcing fatal error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x74E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Non-Fatal Err Over

Type: `OneOf`. Offset: `0x4281A`.

Firmware help: Enables forcing non-fatal error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x7A2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Corr Err Over

Type: `OneOf`. Offset: `0x4283B`.

Firmware help: Enables forcing correctable error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x7F6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ACPI PME Interrupt

Type: `OneOf`. Offset: `0x4285C`.

Firmware help: When enabled, ACPI PME Interrupts are generated from this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x84A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### L0s Support

Type: `OneOf`. Offset: `0x4287D`.

Firmware help: When disabled, IIO never puts its transmitter in L0s state

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | standard, manufacturing | none |
| Enabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x89E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P2P Memory Write

Type: `OneOf`. Offset: `0x4289E`.

Firmware help: Controls Peer2Peer Memory Write Decoding

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x8F2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P2P Memory Read

Type: `OneOf`. Offset: `0x428BF`.

Firmware help: Controls Peer2Peer Memory Read Decoding

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFE9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x946`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PME to ACK

Type: `OneOf`. Offset: `0x428E0`.

Firmware help: Controls timeout usage for IIO waiting on PME_TO_ACK after a PME_TURN_OFF message

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFEA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x99A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### HotPlug ACPI Mode

Type: `OneOf`. Offset: `0x4290D`.

Firmware help: When Disabled, MSI is generated on HP event. When Enabled, _HPGPE message is generated

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFEB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x9EE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x42901`: Not((SocketIioConfig&#91;0xE33&#93; (PCIe ACPI Hot Plug) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PM ACPI Mode

Type: `OneOf`. Offset: `0x42930`.

Firmware help: When Disabled, MSI is generated on PM event. When Enabled, _HPGPE message is generated

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFEC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xA42`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Unsupported Request

Type: `OneOf`. Offset: `0x42951`.

Firmware help: Controls the reporting of unsupported requests that IIO itself detects on requests its receives from a PCI Express/DMI port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFED`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB92`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Alternate TxEq

Type: `OneOf`. Offset: `0x42972`.

Firmware help: Enable or Disable TxEq

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFEE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xAEA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### SRIS

Type: `OneOf`. Offset: `0x42993`.

Firmware help: Enable or Disable SRIS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFEF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xA96`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ECRC

Type: `OneOf`. Offset: `0x429B4`.

Firmware help: Enable or Disable ECRC (Error Capabilities and Control Register)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFF0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB3E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### IODC Configuration

Type: `Subtitle`. Offset: `0x429D9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x429E2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x429EB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x429F4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x429FD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A06`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A0F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A18`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A21`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A2A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A33`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A3C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A45`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A4E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A57`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A60`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A69`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A72`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A7B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A84`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A8D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A96`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42A9F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42AA8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42AB1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42ABA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42AC3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42ACC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42AD5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42ADE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42AE7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42AF0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42AF9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B02`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B0B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B14`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B1D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B26`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B2F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B38`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B41`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B4A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B53`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B5C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B65`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B6E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B77`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B80`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B89`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B92`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42B9B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BA4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BAD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BB6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BBF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BC8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BD1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BDA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BE3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BEC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BF5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42BFE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C07`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C10`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C19`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C22`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C2B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C34`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C3D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C46`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C4F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C58`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C61`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C6A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C73`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C7C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C85`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C8E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42C97`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42CA0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42CA9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42CB2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42CBB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x42CC4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x429D5`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `OneOf`. Offset: `0x42CCF`.

Firmware help: Enable/Disable IODC (IO Direct Cache): Generate snoops instead of memory lookups, for remote InvItoM (IIO) and/or WCiLF (cores)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| KTI Option | 6 | standard, manufacturing | none |
| Auto | 1 | none | none |
| Enable for Remote InvItoM Hybrid Push | 2 | none | none |
| InvItoM AllocFlow | 3 | none | none |
| Enable for Remote InvItoM Hybrid AllocNonAlloc | 4 | none | none |
| Enable for Remote InvItoM and Remote WViLF | 5 | none | none |

Size: 8; Min: 0x1; Max: 0x6; Step: 0x0.

Question ID: `0xFF1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x556`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Hide Port?

Type: `OneOf`. Offset: `0x42D0C`.

Firmware help: User can force to hide this root port from OS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| No | 0 | standard, manufacturing | none |
| Yes | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xFF2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xC2B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x426C3`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### (internal CheckBox, Q0xFF3)

Type: `CheckBox`. Offset: `0x42D33`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Default: Enabled; MfgDefault: Enabled.

Question ID: `0xFF3`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xCA0`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x424AD`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x42D2F`: 0x1. Expression result: stock true; CMOS unlock true.
