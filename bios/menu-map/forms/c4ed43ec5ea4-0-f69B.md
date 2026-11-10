# Socket 2 PcieBr3D02F0 - Port 3C

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; Socket 2 PcieBr3D02F0 - Port 3C**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x69B`, PE/section offset `0x3E737`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

No reference path from a candidate root was found. This may be an internal or runtime-linked form.

## Incoming references

- [Socket2 Configuration](c4ed43ec5ea4-0-f519.md) via Socket 2 PcieBr3D02F0 - Port 3C, offset `0xBFDB`.

## Controls and information

### Socket 2 PcieBr3D02F0 - Port 3C

Type: `Subtitle`. Offset: `0x3E73D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: No active IFR hide condition on this path.

### PCI-E Port

Type: `OneOf`. Offset: `0x3E760`.

Firmware help: In auto mode the BIOS will remove the EXP port if there is no device or errors on that device and the device is not HP capable. Disable is used to disable the port and hide its CFG space.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0xEE4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x4A7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0x3E798`.

Firmware help: This option specifies if the link is considered Hot Plug capable.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEE5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x3E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E788`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3E790`: (SocketIioConfig&#91;0x4A7&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Surprise Hot Plug Capable

Type: `OneOf`. Offset: `0x3E7B9`.

Firmware help: This option specifies if the link is considered Suprise Hot Plug capable.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEE6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x92`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E788`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3E790`: (SocketIioConfig&#91;0x4A7&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link

Type: `OneOf`. Offset: `0x3E7DA`.

Firmware help: This option disables the link so that the no training occurs but the CFG space is still active.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 0 | standard, manufacturing | none |
| Disabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEE7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x10B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E788`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3E790`: (SocketIioConfig&#91;0x4A7&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Link Speed

Type: `OneOf`. Offset: `0x3E807`.

Firmware help: Choose Link Speed for this PCIe port

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Gen 1 (2.5 GT/s) | 1 | none | none |
| Gen 2 (5 GT/s) | 2 | none | none |
| Gen 3 (8 GT/s) | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0xEE8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x5A3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E7FF`: (SocketIioConfig&#91;0x4A7&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Override Max Link Width

Type: `OneOf`. Offset: `0x3E83E`.

Firmware help: Override the max link width that was set by bifurcation

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| x1 | 1 | none | none |
| x2 | 2 | none | none |
| x4 | 3 | none | none |
| x8 | 4 | none | none |

Size: 8; Min: 0x0; Max: 0x4; Step: 0x0.

Question ID: `0xEE9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x64B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E7FF`: (SocketIioConfig&#91;0x4A7&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E836`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Port DeEmphasis

Type: `OneOf`. Offset: `0x3E886`.

Firmware help: De-Emphais control (LNKCON2&#91;6&#93;) for this PCIe port.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| -6.0 dB | 0 | none | none |
| -3.5 dB | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEEA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x69F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E7FF`: (SocketIioConfig&#91;0x4A7&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E876`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3E87E`: (SocketIioConfig&#91;0x5A3&#93; (Link Speed) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Status

Type: `Text`. Offset: `0x3E8AD`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Max

Type: `Text`. Offset: `0x3E8B5`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Speed

Type: `Text`. Offset: `0x3E8C5`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: Conditional; no CMOS vendor gate on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E8BD`: (SocketIioConfig&#91;0x4A7&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Clocking

Type: `OneOf`. Offset: `0x3E8D7`.

Firmware help: Configure port clocking via LNKCON&#91;6&#93;. This refers to this components and the down stream component.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Distinct | 0 | none | none |
| Common | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEEB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x207`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E8CF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Port Max Payload Size

Type: `OneOf`. Offset: `0x3E8FA`.

Firmware help: Set Maxpayload size to 256B if possible

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 128B | 0 | none | none |
| 256B | 1 | none | none |
| Auto | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0xEEC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x25B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port D-state

Type: `OneOf`. Offset: `0x3E92A`.

Firmware help: Set to D0 for normal operation, D3Hot to be in low-power state

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| D0 | 0 | standard, manufacturing | none |
| D3Hot | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEED`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x2AF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E922`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E ASPM Support

Type: `OneOf`. Offset: `0x3E94D`.

Firmware help: This option enables / disables the ASPM (L1) support for the downstream devices.

Access: No active IFR hide condition on this path; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 7 | none | none |
| L1 Only | 2 | none | none |
| Disabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x7; Step: 0x0.

Question ID: `0xEEE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x15F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port L0s Exit Latency

Type: `OneOf`. Offset: `0x3E985`.

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

Question ID: `0xEEF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x303`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3E97D`: (SocketIioConfig&#91;0x15F&#93; (PCI-E ASPM Support) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port L1 Exit Latency

Type: `OneOf`. Offset: `0x3E9DA`.

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

Question ID: `0xEF0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x357`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3E9D2`: (SocketIioConfig&#91;0x15F&#93; (PCI-E ASPM Support) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MSI

Type: `OneOf`. Offset: `0x3EA27`.

Firmware help: BUS0 DEVx FUN0 OFF 0x5A bit 0, Where X is 0-3

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x3AB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Extended Sync

Type: `OneOf`. Offset: `0x3EA48`.

Firmware help: Enable / disable the Extended Sync Mode (D:x F:0 O:7Ch B:7) where x is 0-9

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x3FF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Compliance Mode

Type: `OneOf`. Offset: `0x3EA69`.

Firmware help: Disable/Enable Compliance Mode for this PCIe port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x5F7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### EOI

Type: `OneOf`. Offset: `0x3EA8A`.

Firmware help: Dev 0,2,3 MISCCTRLSTS (Reg 0x188)Bit 26

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | standard, manufacturing | none |
| Enabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x6F3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Fatal Err Over

Type: `OneOf`. Offset: `0x3EAAB`.

Firmware help: Enables forcing fatal error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x747`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Non-Fatal Err Over

Type: `OneOf`. Offset: `0x3EACC`.

Firmware help: Enables forcing non-fatal error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x79B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Corr Err Over

Type: `OneOf`. Offset: `0x3EAED`.

Firmware help: Enables forcing correctable error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x7EF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ACPI PME Interrupt

Type: `OneOf`. Offset: `0x3EB0E`.

Firmware help: When enabled, ACPI PME Interrupts are generated from this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x843`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### L0s Support

Type: `OneOf`. Offset: `0x3EB2F`.

Firmware help: When disabled, IIO never puts its transmitter in L0s state

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | standard, manufacturing | none |
| Enabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEF9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x897`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P2P Memory Write

Type: `OneOf`. Offset: `0x3EB50`.

Firmware help: Controls Peer2Peer Memory Write Decoding

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEFA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x8EB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P2P Memory Read

Type: `OneOf`. Offset: `0x3EB71`.

Firmware help: Controls Peer2Peer Memory Read Decoding

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEFB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x93F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PME to ACK

Type: `OneOf`. Offset: `0x3EB92`.

Firmware help: Controls timeout usage for IIO waiting on PME_TO_ACK after a PME_TURN_OFF message

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEFC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x993`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### HotPlug ACPI Mode

Type: `OneOf`. Offset: `0x3EBBF`.

Firmware help: When Disabled, MSI is generated on HP event. When Enabled, _HPGPE message is generated

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEFD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x9E7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EBB3`: Not((SocketIioConfig&#91;0xE33&#93; (PCIe ACPI Hot Plug) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PM ACPI Mode

Type: `OneOf`. Offset: `0x3EBE2`.

Firmware help: When Disabled, MSI is generated on PM event. When Enabled, _HPGPE message is generated

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEFE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xA3B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Unsupported Request

Type: `OneOf`. Offset: `0x3EC03`.

Firmware help: Controls the reporting of unsupported requests that IIO itself detects on requests its receives from a PCI Express/DMI port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xEFF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB8B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Alternate TxEq

Type: `OneOf`. Offset: `0x3EC24`.

Firmware help: Enable or Disable TxEq

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xF00`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xAE3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### SRIS

Type: `OneOf`. Offset: `0x3EC45`.

Firmware help: Enable or Disable SRIS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xF01`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xA8F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ECRC

Type: `OneOf`. Offset: `0x3EC66`.

Firmware help: Enable or Disable ECRC (Error Capabilities and Control Register)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xF02`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB37`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EC8B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EC94`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EC9D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECA6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECAF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECB8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECC1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECCA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECD3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECDC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECE5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECEE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ECF7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED00`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED09`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED12`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED1B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED24`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED2D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED36`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED3F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED48`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED51`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED5A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED63`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED6C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED75`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED7E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED87`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED90`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3ED99`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDA2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDAB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDB4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDBD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDC6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDCF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDD8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDE1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDEA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDF3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EDFC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE05`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE0E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE17`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE20`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE29`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE32`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE3B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE44`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE4D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE56`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE5F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE68`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE71`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE7A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE83`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE8C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE95`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EE9E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EEA7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EEB0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EEB9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EEC2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EECB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EED4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EEDD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EEE6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EEEF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EEF8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF01`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF0A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF13`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF1C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF25`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF2E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF37`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF40`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF49`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF52`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF5B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF64`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF6D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x3EF76`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x3EC87`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `OneOf`. Offset: `0x3EF81`.

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

Question ID: `0xF03`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x54F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Hide Port?

Type: `OneOf`. Offset: `0x3EFBE`.

Firmware help: User can force to hide this root port from OS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| No | 0 | standard, manufacturing | none |
| Yes | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0xF04`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xC24`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3E975`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### (internal CheckBox, Q0xF05)

Type: `CheckBox`. Offset: `0x3EFE5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Default: Enabled; MfgDefault: Enabled.

Question ID: `0xF05`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xC99`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `GrayOutIf` at `0x3E758`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x3EFE1`: 0x1. Expression result: stock true; CMOS unlock true.
