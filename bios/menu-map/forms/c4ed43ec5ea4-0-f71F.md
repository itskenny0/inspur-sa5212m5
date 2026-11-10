# Socket0 Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; IIO DFX Configuration &gt; Socket0 Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x71F`, PE/section offset `0x11849`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [IIO DFX Configuration](c4ed43ec5ea4-0-f6C5.md) via Socket0 Configuration, offset `0xF426`.

## Controls and information

### (internal CheckBox, Q0x30F)

Type: `CheckBox`. Offset: `0x11853`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path.

Default: Disabled; MfgDefault: Disabled.

Question ID: `0x30F`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0xC64`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1184F`: 0x1. Expression result: stock true; CMOS unlock true.

### Socket 0 Dfx PcieBr0D00F0 - Port 0/DMI

Type: `Ref`. Offset: `0x11865`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr0D00F0 - Port 0/DMI](c4ed43ec5ea4-0-f6CA.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x310`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr1D00F0 - Port 1A

Type: `Ref`. Offset: `0x1187C`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr1D00F0 - Port 1A](c4ed43ec5ea4-0-f6CB.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x311`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11874`: (SocketIioConfig&#91;0xC65&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr1D01F0 - Port 1B

Type: `Ref`. Offset: `0x11895`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr1D01F0 - Port 1B](c4ed43ec5ea4-0-f6CD.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x312`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1188D`: (SocketIioConfig&#91;0xC66&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr1D02F0 - Port 1C

Type: `Ref`. Offset: `0x118AE`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr1D02F0 - Port 1C](c4ed43ec5ea4-0-f6CE.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x313`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118A6`: (SocketIioConfig&#91;0xC67&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr1D03F0 - Port 1D

Type: `Ref`. Offset: `0x118C7`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr1D03F0 - Port 1D](c4ed43ec5ea4-0-f6CF.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x314`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118BF`: (SocketIioConfig&#91;0xC68&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr2D00F0 - Port 2A

Type: `Ref`. Offset: `0x118E0`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr2D00F0 - Port 2A](c4ed43ec5ea4-0-f6D0.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x315`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118D8`: (SocketIioConfig&#91;0xC69&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr2D01F0 - Port 2B

Type: `Ref`. Offset: `0x118F9`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr2D01F0 - Port 2B](c4ed43ec5ea4-0-f6D1.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x316`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x118F1`: (SocketIioConfig&#91;0xC6A&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr2D02F0 - Port 2C

Type: `Ref`. Offset: `0x11912`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr2D02F0 - Port 2C](c4ed43ec5ea4-0-f6D2.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x317`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1190A`: (SocketIioConfig&#91;0xC6B&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr2D03F0 - Port 2D

Type: `Ref`. Offset: `0x1192B`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr2D03F0 - Port 2D](c4ed43ec5ea4-0-f6D3.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x318`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11923`: (SocketIioConfig&#91;0xC6C&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr3D00F0 - Port 3A

Type: `Ref`. Offset: `0x11944`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr3D00F0 - Port 3A](c4ed43ec5ea4-0-f6D4.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x319`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1193C`: (SocketIioConfig&#91;0xC6D&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr3D01F0 - Port 3B

Type: `Ref`. Offset: `0x1195D`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr3D01F0 - Port 3B](c4ed43ec5ea4-0-f6D5.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x31A`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11955`: (SocketIioConfig&#91;0xC6E&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr3D02F0 - Port 3C

Type: `Ref`. Offset: `0x11976`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr3D02F0 - Port 3C](c4ed43ec5ea4-0-f6D6.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x31B`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x1196E`: (SocketIioConfig&#91;0xC6F&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr3D03F0 - Port 3D

Type: `Ref`. Offset: `0x1198F`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr3D03F0 - Port 3D](c4ed43ec5ea4-0-f6D7.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x31C`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11987`: (SocketIioConfig&#91;0xC70&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr4D00F0 - MCP 0

Type: `Ref`. Offset: `0x119A8`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr4D00F0 - MCP 0](c4ed43ec5ea4-0-f6D8.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x31D`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119A0`: (SocketIioConfig&#91;0xC71&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr4D01F0 - MCP 0

Type: `Ref`. Offset: `0x119C1`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr4D01F0 - MCP 0](c4ed43ec5ea4-0-f6D9.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x31E`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119B9`: (SocketIioConfig&#91;0xC72&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr4D01F0 - MCP 0

Type: `Ref`. Offset: `0x119DA`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr4D02F0 - MCP 0](c4ed43ec5ea4-0-f6DA.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x31F`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119D2`: (SocketIioConfig&#91;0xC73&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr4D03F0 - MCP 0

Type: `Ref`. Offset: `0x119F3`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr4D03F0 - MCP 0](c4ed43ec5ea4-0-f6DB.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x320`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x119EB`: (SocketIioConfig&#91;0xC74&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr5D00F0 - MCP 1

Type: `Ref`. Offset: `0x11A0C`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr5D00F0 - MCP 1](c4ed43ec5ea4-0-f6DC.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x321`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11A04`: (SocketIioConfig&#91;0xC75&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr5D01F0 - MCP 1

Type: `Ref`. Offset: `0x11A25`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr5D01F0 - MCP 1](c4ed43ec5ea4-0-f6DD.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x322`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11A1D`: (SocketIioConfig&#91;0xC76&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr5D02F0 - MCP 1

Type: `Ref`. Offset: `0x11A3E`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr5D02F0 - MCP 1](c4ed43ec5ea4-0-f6DE.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x323`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11A36`: (SocketIioConfig&#91;0xC77&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0 Dfx PcieBr5D03F0 - MCP 1

Type: `Ref`. Offset: `0x11A57`.

Firmware help: Settings related to PCI Express PortS (0/1A/1B/1C/1D/2A/2B/2C/2D/3A/3B/3C/3D/4A/5A)

Opens: [Socket 0 Dfx PcieBr5D03F0 - MCP 1](c4ed43ec5ea4-0-f6DF.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x324`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0x11A4F`: (SocketIioConfig&#91;0xC78&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
