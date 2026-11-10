# IIO DFX Configuration

[Menu index](../README.md) | [Module index](../c4ed43ec5ea4-0.md)

Path: **Processor &gt; IIO Configuration &gt; IIO DFX Configuration**

Source: `SocketSetup`. Formset `516D5A04-C0D5-4657-B908-E4FB1D935EF0`, form `0x6C5`, PE/section offset `0xF3F0`.

Root evidence: AMITSE GUID/form entry candidates.

Paths come from static references and AMITSE candidates. Runtime menu selection, callbacks and installed hardware can change what is shown.

## Incoming references

- [IIO Configuration](c4ed43ec5ea4-0-f518.md) via IIO DFX Configuration, offset `0xAFC2`.

## Controls and information

### IIO DFX Configuration

Type: `Subtitle`. Offset: `0xF3F6`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: CMOS vendor gate; other conditions may apply.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### (internal CheckBox, Q0x241)

Type: `CheckBox`. Offset: `0xF40C`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path.

Default: Enabled; MfgDefault: Enabled.

Question ID: `0x241`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0x6`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF408`: 0x1. Expression result: stock true; CMOS unlock true.

### Socket0 Configuration

Type: `Ref`. Offset: `0xF426`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Opens: [Socket0 Configuration](c4ed43ec5ea4-0-f71F.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x242`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF41E`: (SocketIioConfig&#91;0x6&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### (internal CheckBox, Q0x243)

Type: `CheckBox`. Offset: `0xF43B`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Access: Hidden even with CMOS unlock on this path.

Default: Enabled; MfgDefault: Enabled.

Question ID: `0x243`. Question flags: `0x0` (none of the decoded flags).

Storage: `SocketIioConfig` at byte offset `0x7`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF437`: 0x1. Expression result: stock true; CMOS unlock true.

### Socket1 Configuration

Type: `Ref`. Offset: `0xF455`.

No explanatory firmware help is supplied. The label alone does not establish the control's full behavior.

Opens: [Socket1 Configuration](c4ed43ec5ea4-0-f720.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x244`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xF44D`: (SocketIioConfig&#91;0x7&#93; == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### EV DFX Features

Type: `OneOf`. Offset: `0xF46E`.

Firmware help: Expose IIO DFX devices and other CPU devices like PMON

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x245`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE43`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF466`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Ltssm Logger

Type: `OneOf`. Offset: `0xF48F`.

Firmware help: Enable/Disable Ltssm Logger for PCIE functionality

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x246`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE44`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF466`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Stop

Type: `Numeric`. Offset: `0xF4B8`.

Firmware help: Configure the Stop value for Ltssm Logger

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 153; store 0x1: 153.

Size: 8; Min: 0x0; Max: 0x99; Step: 0x0.

Question ID: `0x247`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE45`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF466`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF4B0`: (SocketIioConfig&#91;0xE44&#93; (Ltssm Logger) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Speed

Type: `OneOf`. Offset: `0xF4D7`.

Firmware help: Configure Speed value for Ltssm Logger

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Gen 1 (2.5 GT/s) | 1 | standard, manufacturing | none |
| Gen 2 (5 GT/s) | 2 | none | none |
| Gen 3 (8 GT/s) | 3 | none | none |

Size: 8; Min: 0x1; Max: 0x3; Step: 0x0.

Question ID: `0x248`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE46`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF466`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF4B0`: (SocketIioConfig&#91;0xE44&#93; (Ltssm Logger) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Mask

Type: `Numeric`. Offset: `0xF4FF`.

Firmware help: Configure Mask value for Ltssm Logger

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

Explicit static defaults: store 0x0: 255; store 0x1: 255.

Size: 8; Min: 0x0; Max: 0xFF; Step: 0x0.

Question ID: `0x249`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE47`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF466`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.
- `SuppressIf` at `0xF4B0`: (SocketIioConfig&#91;0xE44&#93; (Ltssm Logger) == 0x0). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Jitter Logger

Type: `OneOf`. Offset: `0xF520`.

Firmware help: Enable/Disable Jitter Logger for PCIE functionality

Access: CMOS vendor gate; other conditions may apply; disabled after unlock: conditional.

| Choice | Value | Static default flags | Additional conditions |
| --- | --- | --- | --- |
| Disabled | 0 | standard, manufacturing | none |
| Enabled | 1 | none | none |

Size: 8; Min: 0x0; Max: 0x1; Step: 0x0.

Question ID: `0x24A`. Question flags: `0x10` (reset required).

Storage: `SocketIioConfig` at byte offset `0xE48`, GUID `DD84017E-7F52-48F9-B16E-50ED9E0DBE27`. This is a variable offset, not a CMOS address.

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `GrayOutIf` at `0xF466`: (SocketSystemAccess&#91;0x0&#93; == 0x1). Expression result: stock runtime-dependent; CMOS unlock runtime-dependent.

### Socket 0, Device Hide Menu

Type: `Ref`. Offset: `0xF543`.

Firmware help: Socket 0, Device Hide Menu

Opens: [Socket 0, Device Hide Menu](c4ed43ec5ea4-0-f6C6.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x24B`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Socket 1, Device Hide Menu

Type: `Ref`. Offset: `0xF552`.

Firmware help: Socket 1, Device Hide Menu

Opens: [Socket 1, Device Hide Menu](c4ed43ec5ea4-0-f6C7.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x24C`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Socket 2, Device Hide Menu

Type: `Ref`. Offset: `0xF561`.

Firmware help: Socket 2, Device Hide Menu

Opens: [Socket 2, Device Hide Menu](c4ed43ec5ea4-0-f6C8.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x24D`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.

### Socket 3, Device Hide Menu

Type: `Ref`. Offset: `0xF570`.

Firmware help: Socket 3, Device Hide Menu

Opens: [Socket 3, Device Hide Menu](c4ed43ec5ea4-0-f6C9.md).

Access: CMOS vendor gate; other conditions may apply.

Question ID: `0x24E`. Question flags: `0x0` (none of the decoded flags).

Conditions on this path and item:

- `SuppressIf` at `0x9BBF`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
- `SuppressIf` at `0xAFBA`: (InspurSocketSetupFeatures&#91;0x1&#93; == 0x1). Expression result: stock true; CMOS unlock false.
