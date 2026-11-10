# Socket 3 PcieBr3D03F0 - Port 3D

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Socket 3 PcieBr3D03F0 - Port 3D**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6A7`, PE/section offset `0x4AE57`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Incoming references

- [Socket3 Configuration](c4ed43ec5ea4-0-f51A.md) via Socket 3 PcieBr3D03F0 - Port 3D, offset `0xC209`.

## Controls and information

### Socket 3 PcieBr3D03F0 - Port 3D

Type: `Subtitle`. Offset: `0x4AE5D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### PCI-E Port

Type: `OneOf`. Offset: `0x4AE80`.

Firmware help: In auto mode the BIOS will remove the EXP port if there is no device or errors on that device and the device is not HP capable. Disable is used to disable the port and hide its CFG space.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x11F7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x4BD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0x4AEB8`.

Firmware help: This option specifies if the link is considered Hot Plug capable.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x11F8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x54`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AEA8`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4AEB0`: (SocketIioConfig&#91;0x4BD&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Surprise Hot Plug Capable

Type: `OneOf`. Offset: `0x4AED9`.

Firmware help: This option specifies if the link is considered Suprise Hot Plug capable.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x11F9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xA8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AEA8`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4AEB0`: (SocketIioConfig&#91;0x4BD&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link

Type: `OneOf`. Offset: `0x4AEFA`.

Firmware help: This option disables the link so that the no training occurs but the CFG space is still active.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 0 | standard, manufacturing | none |
| Disabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x11FA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x121`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AEA8`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4AEB0`: (SocketIioConfig&#91;0x4BD&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Link Speed

Type: `OneOf`. Offset: `0x4AF27`.

Firmware help: Choose Link Speed for this PCIe port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Gen 1 (2.5 GT/s) | 1 | none | none |
| Gen 2 (5 GT/s) | 2 | none | none |
| Gen 3 (8 GT/s) | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0x11FB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x5B9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AF1F`: (SocketIioConfig&#91;0x4BD&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Override Max Link Width

Type: `OneOf`. Offset: `0x4AF5E`.

Firmware help: Override the max link width that was set by bifurcation

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| x1 | 1 | none | none |
| x2 | 2 | none | none |
| x4 | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0x11FC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x661`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AF1F`: (SocketIioConfig&#91;0x4BD&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AF56`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Port DeEmphasis

Type: `OneOf`. Offset: `0x4AF9F`.

Firmware help: De-Emphais control (LNKCON2&#91;6&#93;) for this PCIe port.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| -6.0 dB | 0 | none | none |
| -3.5 dB | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x11FD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x6B5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AF1F`: (SocketIioConfig&#91;0x4BD&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AF8F`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4AF97`: (SocketIioConfig&#91;0x5B9&#93; (Link Speed) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Status

Type: `Text`. Offset: `0x4AFC6`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Max

Type: `Text`. Offset: `0x4AFCE`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Speed

Type: `Text`. Offset: `0x4AFDE`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AFD6`: (SocketIioConfig&#91;0x4BD&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Clocking

Type: `OneOf`. Offset: `0x4AFF0`.

Firmware help: Configure port clocking via LNKCON&#91;6&#93;. This refers to this components and the down stream component.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Distinct | 0 | none | none |
| Common | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x11FE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x21D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4AFE8`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Port Max Payload Size

Type: `OneOf`. Offset: `0x4B013`.

Firmware help: Set Maxpayload size to 256B if possible

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 128B | 0 | none | none |
| 256B | 1 | none | none |
| Auto | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x11FF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x271`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port D-state

Type: `OneOf`. Offset: `0x4B043`.

Firmware help: Set to D0 for normal operation, D3Hot to be in low-power state

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| D0 | 0 | standard, manufacturing | none |
| D3Hot | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1200`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x2C5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B03B`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E ASPM Support

Type: `OneOf`. Offset: `0x4B066`.

Firmware help: This option enables / disables the ASPM (L1) support for the downstream devices.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 7 | none | none |
| L1 Only | 2 | none | none |
| Disabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x7; Step: 0x0.

Question ID: `0x1201`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x175`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port L0s Exit Latency

Type: `OneOf`. Offset: `0x4B09E`.

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

Question ID: `0x1202`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x319`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B096`: (SocketIioConfig&#91;0x175&#93; (PCI-E ASPM Support) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port L1 Exit Latency

Type: `OneOf`. Offset: `0x4B0F3`.

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

Question ID: `0x1203`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x36D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B0EB`: (SocketIioConfig&#91;0x175&#93; (PCI-E ASPM Support) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MSI

Type: `OneOf`. Offset: `0x4B140`.

Firmware help: BUS0 DEVx FUN0 OFF 0x5A bit 0, Where X is 0-3

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1204`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x3C1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Extended Sync

Type: `OneOf`. Offset: `0x4B161`.

Firmware help: Enable / disable the Extended Sync Mode (D:x F:0 O:7Ch B:7) where x is 0-9

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1205`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x415`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Compliance Mode

Type: `OneOf`. Offset: `0x4B182`.

Firmware help: Disable/Enable Compliance Mode for this PCIe port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1206`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x60D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### EOI

Type: `OneOf`. Offset: `0x4B1A3`.

Firmware help: Dev 0,2,3 MISCCTRLSTS (Reg 0x188)Bit 26

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | standard, manufacturing | none |
| Enabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1207`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x709`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Fatal Err Over

Type: `OneOf`. Offset: `0x4B1C4`.

Firmware help: Enables forcing fatal error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1208`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x75D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Non-Fatal Err Over

Type: `OneOf`. Offset: `0x4B1E5`.

Firmware help: Enables forcing non-fatal error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1209`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x7B1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Corr Err Over

Type: `OneOf`. Offset: `0x4B206`.

Firmware help: Enables forcing correctable error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x120A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x805`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ACPI PME Interrupt

Type: `OneOf`. Offset: `0x4B227`.

Firmware help: When enabled, ACPI PME Interrupts are generated from this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x120B`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x859`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### L0s Support

Type: `OneOf`. Offset: `0x4B248`.

Firmware help: When disabled, IIO never puts its transmitter in L0s state

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | standard, manufacturing | none |
| Enabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x120C`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x8AD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P2P Memory Write

Type: `OneOf`. Offset: `0x4B269`.

Firmware help: Controls Peer2Peer Memory Write Decoding

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x120D`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x901`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P2P Memory Read

Type: `OneOf`. Offset: `0x4B28A`.

Firmware help: Controls Peer2Peer Memory Read Decoding

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x120E`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x955`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PME to ACK

Type: `OneOf`. Offset: `0x4B2AB`.

Firmware help: Controls timeout usage for IIO waiting on PME_TO_ACK after a PME_TURN_OFF message

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x120F`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x9A9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### HotPlug ACPI Mode

Type: `OneOf`. Offset: `0x4B2D8`.

Firmware help: When Disabled, MSI is generated on HP event. When Enabled, _HPGPE message is generated

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1210`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x9FD`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B2CC`: Not((SocketIioConfig&#91;0xE33&#93; (PCIe ACPI Hot Plug) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PM ACPI Mode

Type: `OneOf`. Offset: `0x4B2FB`.

Firmware help: When Disabled, MSI is generated on PM event. When Enabled, _HPGPE message is generated

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1211`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xA51`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Unsupported Request

Type: `OneOf`. Offset: `0x4B31C`.

Firmware help: Controls the reporting of unsupported requests that IIO itself detects on requests its receives from a PCI Express/DMI port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1212`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBA1`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Alternate TxEq

Type: `OneOf`. Offset: `0x4B33D`.

Firmware help: Enable or Disable TxEq

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1213`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xAF9`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### SRIS

Type: `OneOf`. Offset: `0x4B35E`.

Firmware help: Enable or Disable SRIS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1214`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xAA5`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ECRC

Type: `OneOf`. Offset: `0x4B37F`.

Firmware help: Enable or Disable ECRC (Error Capabilities and Control Register)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1215`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB4D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3A4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3AD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3B6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3BF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3C8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3D1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3DA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3E3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3EC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3F5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B3FE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B407`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B410`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B419`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B422`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B42B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B434`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B43D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B446`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B44F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B458`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B461`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B46A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B473`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B47C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B485`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B48E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B497`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4A0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4A9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4B2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4BB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4C4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4CD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4D6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4DF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4E8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4F1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B4FA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B503`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B50C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B515`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B51E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B527`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B530`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B539`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B542`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B54B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B554`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B55D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B566`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B56F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B578`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B581`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B58A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B593`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B59C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5A5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5AE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5B7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5C0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5C9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5D2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5DB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5E4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5ED`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5F6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B5FF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B608`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B611`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B61A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B623`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B62C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B635`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B63E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B647`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B650`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B659`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B662`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B66B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B674`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B67D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B686`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x4B68F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x4B3A0`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `OneOf`. Offset: `0x4B69A`.

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

Question ID: `0x1216`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x565`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Hide Port?

Type: `OneOf`. Offset: `0x4B6D7`.

Firmware help: User can force to hide this root port from OS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| No | 0 | standard, manufacturing | none |
| Yes | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x1217`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xC3A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B08E`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### (internal CheckBox, Q0x1218)

Type: `CheckBox`. Offset: `0x4B6FE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Default: Enabled; MfgDefault: Enabled.

Question ID: `0x1218`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xCAF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x4AE78`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x4B6FA`: 0x1. Expression result: stock true; CMOS unlock true.
