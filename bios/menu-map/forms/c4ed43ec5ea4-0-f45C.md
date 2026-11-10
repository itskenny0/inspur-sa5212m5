# Socket 0 PcieBr3D00F0 - Port 3A

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; Socket0 Configuration &gt; Socket 0 PcieBr3D00F0 - Port 3A**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x45C`, PE/section offset `0x254C1`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [Socket0 Configuration](c4ed43ec5ea4-0-f47A.md) via Socket 0 PcieBr3D00F0 - Port 3A, offset `0xB8D1`.

## Controls and information

### Socket 0 PcieBr3D00F0 - Port 3A

Type: `Subtitle`. Offset: `0x254C7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port

Type: `OneOf`. Offset: `0x254EA`.

Firmware help: In auto mode the BIOS will remove the EXP port if there is no device or errors on that device and the device is not HP capable. Disable is used to disable the port and hide its CFG space.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 2 | standard, manufacturing | none |
| Disabled | 0 | none | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x8A1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x47B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PXE Option ROM

Type: `OneOf`. Offset: `0x25512`.

Firmware help: This option controls the Option ROM's execution of network device if it exists on the slot.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | none | none |
| Enabled | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8A2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x187`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hot Plug Capable

Type: `OneOf`. Offset: `0x25543`.

Firmware help: This option specifies if the link is considered Hot Plug capable.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8A3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x12`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25533`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x2553B`: (SocketIioConfig&#91;0x47B&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Surprise Hot Plug Capable

Type: `OneOf`. Offset: `0x25564`.

Firmware help: This option specifies if the link is considered Suprise Hot Plug capable.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8A4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x66`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25533`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x2553B`: (SocketIioConfig&#91;0x47B&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link

Type: `OneOf`. Offset: `0x25585`.

Firmware help: This option disables the link so that the no training occurs but the CFG space is still active.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Enabled | 0 | standard, manufacturing | none |
| Disabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8A5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xDF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25533`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x2553B`: (SocketIioConfig&#91;0x47B&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Link Speed

Type: `OneOf`. Offset: `0x255B2`.

Firmware help: Choose Link Speed for this PCIe port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| Gen 1 (2.5 GT/s) | 1 | none | none |
| Gen 2 (5 GT/s) | 2 | none | none |
| Gen 3 (8 GT/s) | 3 | none | none |

Size: 8; Min: 0x0; Max: 0x3; Step: 0x0.

Question ID: `0x8A6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x577`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x255AA`: (SocketIioConfig&#91;0x47B&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Override Max Link Width

Type: `OneOf`. Offset: `0x255E9`.

Firmware help: Override the max link width that was set by bifurcation

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 0 | standard, manufacturing | none |
| x1 | 1 | none | none |
| x2 | 2 | none | none |
| x4 | 3 | none | none |
| x8 | 4 | none | none |
| x16 | 5 | none | none |

Size: 8; Min: 0x0; Max: 0x5; Step: 0x0.

Question ID: `0x8A7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x61F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x255AA`: (SocketIioConfig&#91;0x47B&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x255E1`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Port DeEmphasis

Type: `OneOf`. Offset: `0x25638`.

Firmware help: De-Emphais control (LNKCON2&#91;6&#93;) for this PCIe port.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| -6.0 dB | 0 | none | none |
| -3.5 dB | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8A8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x673`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x255AA`: (SocketIioConfig&#91;0x47B&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25628`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25630`: (SocketIioConfig&#91;0x577&#93; (Link Speed) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Status

Type: `Text`. Offset: `0x2565F`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Max

Type: `Text`. Offset: `0x25667`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Link Speed

Type: `Text`. Offset: `0x25677`.

Firmware provides this information field without explanatory help.

Static display text: Link Training Error. Runtime callbacks may replace this text.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x2566F`: (SocketIioConfig&#91;0x47B&#93; (PCI-E Port) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port Clocking

Type: `OneOf`. Offset: `0x25689`.

Firmware help: Configure port clocking via LNKCON&#91;6&#93;. This refers to this components and the down stream component.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Distinct | 0 | none | none |
| Common | 1 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8A9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x1DB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25681`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Port Max Payload Size

Type: `OneOf`. Offset: `0x256AC`.

Firmware help: Set Maxpayload size to 256B if possible

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| 128B | 0 | none | none |
| 256B | 1 | none | none |
| Auto | 2 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x8AA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x22F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port D-state

Type: `OneOf`. Offset: `0x256DC`.

Firmware help: Set to D0 for normal operation, D3Hot to be in low-power state

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| D0 | 0 | standard, manufacturing | none |
| D3Hot | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8AB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x283`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x256D4`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E ASPM Support

Type: `OneOf`. Offset: `0x256FF`.

Firmware help: This option enables / disables the ASPM (L1) support for the downstream devices.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Auto | 7 | none | none |
| L1 Only | 2 | none | none |
| Disabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x7; Step: 0x0.

Question ID: `0x8AC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x133`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port L0s Exit Latency

Type: `OneOf`. Offset: `0x25737`.

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

Question ID: `0x8AD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x2D7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x2572F`: (SocketIioConfig&#91;0x133&#93; (PCI-E ASPM Support) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PCI-E Port L1 Exit Latency

Type: `OneOf`. Offset: `0x2578C`.

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

Question ID: `0x8AE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x32B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25784`: (SocketIioConfig&#91;0x133&#93; (PCI-E ASPM Support) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### MSI

Type: `OneOf`. Offset: `0x257D9`.

Firmware help: BUS0 DEVx FUN0 OFF 0x5A bit 0, Where X is 0-3

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8AF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x37F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PCI-E Extended Sync

Type: `OneOf`. Offset: `0x257FA`.

Firmware help: Enable / disable the Extended Sync Mode (D:x F:0 O:7Ch B:7) where x is 0-9

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x3D3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Compliance Mode

Type: `OneOf`. Offset: `0x2581B`.

Firmware help: Disable/Enable Compliance Mode for this PCIe port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x5CB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### EOI

Type: `OneOf`. Offset: `0x2584E`.

Firmware help: Dev 0,2,3 MISCCTRLSTS (Reg 0x188)Bit 26

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | standard, manufacturing | none |
| Enabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x6C7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x2583C`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x1) or (SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Fatal Err Over

Type: `OneOf`. Offset: `0x25871`.

Firmware help: Enables forcing fatal error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x71B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Non-Fatal Err Over

Type: `OneOf`. Offset: `0x25892`.

Firmware help: Enables forcing non-fatal error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x76F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Corr Err Over

Type: `OneOf`. Offset: `0x258B3`.

Firmware help: Enables forcing correctable error propogation to the IIO core error logic for this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x7C3`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ACPI PME Interrupt

Type: `OneOf`. Offset: `0x258D4`.

Firmware help: When enabled, ACPI PME Interrupts are generated from this port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x817`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### L0s Support

Type: `OneOf`. Offset: `0x258F5`.

Firmware help: When disabled, IIO never puts its transmitter in L0s state

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | standard, manufacturing | none |
| Enabled | 0 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x86B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P2P Memory Write

Type: `OneOf`. Offset: `0x25916`.

Firmware help: Controls Peer2Peer Memory Write Decoding

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x8BF`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### P2P Memory Read

Type: `OneOf`. Offset: `0x25937`.

Firmware help: Controls Peer2Peer Memory Read Decoding

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8B9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x913`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### PME to ACK

Type: `OneOf`. Offset: `0x25958`.

Firmware help: Controls timeout usage for IIO waiting on PME_TO_ACK after a PME_TURN_OFF message

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 1 | none | none |
| Enabled | 0 | standard, manufacturing | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8BA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x967`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### HotPlug ACPI Mode

Type: `OneOf`. Offset: `0x25985`.

Firmware help: When Disabled, MSI is generated on HP event. When Enabled, _HPGPE message is generated

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8BB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x9BB`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25979`: Not((SocketIioConfig&#91;0xE33&#93; (PCIe ACPI Hot Plug) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### PM ACPI Mode

Type: `OneOf`. Offset: `0x259A8`.

Firmware help: When Disabled, MSI is generated on PM event. When Enabled, _HPGPE message is generated

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8BC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xA0F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Unsupported Request

Type: `OneOf`. Offset: `0x259C9`.

Firmware help: Controls the reporting of unsupported requests that IIO itself detects on requests its receives from a PCI Express/DMI port

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8BD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB5F`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Alternate TxEq

Type: `OneOf`. Offset: `0x259EA`.

Firmware help: Enable or Disable TxEq

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8BE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xAB7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### SRIS

Type: `OneOf`. Offset: `0x25A0B`.

Firmware help: Enable or Disable SRIS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8BF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xA63`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### ECRC

Type: `OneOf`. Offset: `0x25A2C`.

Firmware help: Enable or Disable ECRC (Error Capabilities and Control Register)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8C0`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xB0B`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A51`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A5A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A63`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A6C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A75`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A7E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A87`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A90`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25A99`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AA2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AAB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AB4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25ABD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AC6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25ACF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AD8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AE1`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AEA`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AF3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25AFC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B05`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B0E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B17`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B20`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B29`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B32`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B3B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B44`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B4D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B56`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B5F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B68`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B71`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B7A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B83`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B8C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B95`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25B9E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BA7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BB0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BB9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BC2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BCB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BD4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BDD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BE6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BEF`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25BF8`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C01`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C0A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C13`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C1C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C25`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C2E`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C37`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C40`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C49`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C52`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C5B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C64`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C6D`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C76`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C7F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C88`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C91`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25C9A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CA3`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CAC`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CB5`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CBE`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CC7`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CD0`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CD9`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CE2`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CEB`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CF4`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25CFD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25D06`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25D0F`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25D18`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25D21`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25D2A`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25D33`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `Subtitle`. Offset: `0x25D3C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25A4D`: 0x1. Expression result: stock true; CMOS unlock true.

### IODC Configuration

Type: `OneOf`. Offset: `0x25D47`.

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

Question ID: `0x8C1`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0x523`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Non-Transparent Bridge PCIe Port Definition

Type: `OneOf`. Offset: `0x25D84`.

Firmware help: &#91;EMBAR1XBASE, EMBAR2XBASE&#93; Configures port as TB, NTB-NTB, or NTB-RP (DON'T SELECT NTB-RP for legacy IIO on A0 Si!)

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Transparent Bridge | 0 | standard, manufacturing | none |
| NTB to NTB | 1 | none | none |
| NTB to RP | 2 | none | none |

Size: 8; Min: 0x0; Max: 0x2; Step: 0x0.

Question ID: `0x8C2`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xCBA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Enable NTB BARs

Type: `OneOf`. Offset: `0x25DB4`.

Firmware help: &#91;IMBAR1&#93; If disabled, BIOS will not program NTB BAR size registers

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8C3`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xCC6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DAC`: (SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Enable SPLIT BARs

Type: `OneOf`. Offset: `0x25DE9`.

Firmware help: &#91;IMBAR2, EMBAR2SZ&#93; If Enabled, will use two 32 bit BARs instead of 64 bit BAR

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8C4`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xCD2`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Primary BAR 23 Size

Type: `Numeric`. Offset: `0x25E0A`.

Firmware help: &#91;IMBAR1SZ&#93; Used to set the prefetchable BAR 23 size on primary side of NTB. Value &lt; than 12 or &gt; 29 (39 for BIOS supporting &gt; 4G PCI) disables BAR.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 22; store 0x1: 22.

Size: 8; Min: 0x0; Max: 0x30; Step: 0x1.

Question ID: `0x8C5`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xCDE`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Primary BAR 4 Size

Type: `Numeric`. Offset: `0x25E31`.

Firmware help: Used to set the prefetchable BAR 4 size on primary side of NTB. Value &lt; than 12 or &gt; 29 (39 for BIOS supporting &gt; 4G PCI) disables BAR.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 12; store 0x1: 12.

Size: 8; Min: 0x0; Max: 0x27; Step: 0x1.

Question ID: `0x8C6`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xCF6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25E29`: (SocketIioConfig&#91;0xCD2&#93; (Enable SPLIT BARs) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Primary BAR 5 Size

Type: `Numeric`. Offset: `0x25E50`.

Firmware help: Used to set the prefetchable BAR 5 size on primary side of NTB. Value &lt; than 12 or &gt; 29 (39 for BIOS supporting &gt; 4G PCI) disables BAR.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 12; store 0x1: 12.

Size: 8; Min: 0x0; Max: 0x27; Step: 0x1.

Question ID: `0x8C7`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD02`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25E29`: (SocketIioConfig&#91;0xCD2&#93; (Enable SPLIT BARs) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Primary BAR 45 Size

Type: `Numeric`. Offset: `0x25E79`.

Firmware help: &#91;IMBAR2SZ&#93; Used to set the prefetchable BAR 45 size on primary side of NTB. Value &lt; than 12 or &gt; 29 (39 for BIOS supporting &gt; 4G PCI) disables BAR.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 22; store 0x1: 22.

Size: 8; Min: 0x0; Max: 0x30; Step: 0x1.

Question ID: `0x8C8`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xCEA`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25E71`: (SocketIioConfig&#91;0xCD2&#93; (Enable SPLIT BARs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Secondary BAR 23 Size

Type: `Numeric`. Offset: `0x25E9A`.

Firmware help: &#91;EMBAR1SZ&#93; Used to set the prefetchable BAR 23 size on secondary side of NTB. Value &lt; than 12 or &gt; 39 disables BAR.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 22; store 0x1: 22.

Size: 8; Min: 0x0; Max: 0x30; Step: 0x1.

Question ID: `0x8C9`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD0E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Secondary BAR 4 Size

Type: `Numeric`. Offset: `0x25EC1`.

Firmware help: Used to set the prefetchable BAR 4 size on Secondary side of NTB. Value &lt; than 12 or &gt; 29 (39 for BIOS supporting &gt; 4G PCI) disables BAR.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 12; store 0x1: 12.

Size: 8; Min: 0x0; Max: 0x27; Step: 0x1.

Question ID: `0x8CA`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD26`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25EB9`: (SocketIioConfig&#91;0xCD2&#93; (Enable SPLIT BARs) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Secondary BAR 5 Size

Type: `Numeric`. Offset: `0x25EE0`.

Firmware help: Used to set the prefetchable BAR 5 size on Secondary side of NTB. Value &lt; than 12 or &gt; 29 (39 for BIOS supporting &gt; 4G PCI) disables BAR.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 12; store 0x1: 12.

Size: 8; Min: 0x0; Max: 0x27; Step: 0x1.

Question ID: `0x8CB`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD32`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25EB9`: (SocketIioConfig&#91;0xCD2&#93; (Enable SPLIT BARs) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Secondary BAR 45 Size

Type: `Numeric`. Offset: `0x25F09`.

Firmware help: Used to set the prefetchable BAR 45 size on secondary side of NTB. Value &lt; than 12 or &gt; 39 disables BAR.

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 22; store 0x1: 22.

Size: 8; Min: 0x0; Max: 0x30; Step: 0x1.

Question ID: `0x8CC`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD1A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25DD7`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCC6&#93; (Enable NTB BARs) == 0x0)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25F01`: (SocketIioConfig&#91;0xCD2&#93; (Enable SPLIT BARs) == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Secondary BAR 0/1 Prefetchable

Type: `OneOf`. Offset: `0x25F3E`.

Firmware help: Configures Secondary BAR 0/1 as Prefetchable/Non-Prefetchable

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8CD`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD3E`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25F2C`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x1)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Crosslink control Override

Type: `OneOf`. Offset: `0x25F73`.

Firmware help: Configure NTB port as DSP/USP, USD/DSP, or use external pin

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| DSD/USP | 3 | standard, manufacturing | none |
| USD/DSP | 2 | none | none |

Size: 8; Min: 0x2; Max: 0x3; Step: 0x0.

Question ID: `0x8CE`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xD4A`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0x25F61`: ((SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x0) or (SocketIioConfig&#91;0xCBA&#93; (Non-Transparent Bridge PCIe Port Definition) == 0x2)). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Hide Port?

Type: `OneOf`. Offset: `0x25F96`.

Firmware help: User can force to hide this root port from OS

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| No | 0 | standard, manufacturing | none |
| Yes | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x8CF`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xBF8`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25727`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### (internal CheckBox, Q0x8D0)

Type: `CheckBox`. Offset: `0x25FBD`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path; disabled after unlock: conditional.

Default: Enabled; MfgDefault: Enabled.

Question ID: `0x8D0`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xC6D`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAEE8`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xB8C9`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `GrayOutIf` at `0x254E2`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x25FB9`: 0x1. Expression result: stock true; CMOS unlock true.
