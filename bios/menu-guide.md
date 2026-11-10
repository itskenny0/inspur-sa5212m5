# Reading the BIOS menu map

The [full catalogue](menu-map/README.md) is organized by firmware formset, then by form. Each setting page gives the path, vendor help, choices, defaults and access conditions. This guide explains the main areas and some terminology that the help assumes you already know. It describes the intended function of the controls, not a recommended configuration.

The map contains repeated port, socket, channel and device templates. Their presence does not mean the corresponding hardware is installed. It also includes blank internal questions that other expressions use, and controls that remain hidden even after the CMOS switch is selected.

## Main setup

[Setup forms](menu-map/53022c42f931-0.md) contain the familiar Main, Advanced, Security, Boot and Save & Exit pages.

| Area | What it controls |
| --- | --- |
| Main | Firmware, CPU and memory information, access level, date and time. Information fields can be filled in by callbacks during boot. |
| Trusted Computing | Firmware support for TPM/TCG services and related operations. This is separate from the Secure Boot key database. |
| ACPI Settings | Interfaces and states exposed to the OS, including hibernation-related settings. OS support also determines whether a state is usable. |
| Super IO Configuration | Low-speed peripheral functions such as the board's serial port and its resource assignments. |
| Serial Port Console Redirection | Sending the firmware text console over a serial connection, including baud rate and terminal parameters. This is separate from the BMC's graphical remote console. |
| PCI Subsystem Settings | PCI resource allocation and PCIe behavior. These general settings coexist with more detailed CPU IIO and PCH port controls. |
| Network Stack Configuration | Firmware network protocols and network boot support. These settings do not replace the NIC driver's OS configuration. |
| CSM Configuration | Legacy BIOS compatibility and option ROM policies. Boot Option Filter controls which boot types are offered; per-device policies choose which kind of adapter ROM is used. Disabling CSM is a separate change from showing this page. |
| Security | Setup passwords and references to Secure Boot configuration. Access restrictions and security state can still disable controls after the menu unlock. |
| Boot | Boot order and startup behavior. Device lists can be populated dynamically. |
| Save & Exit | Commit, discard and default-loading actions. A destructive driver callback or storage action is not necessarily undone by discarding normal setup edits. |

## Processor

[SocketSetup](menu-map/c4ed43ec5ea4-0.md) is the largest group. It includes CPU, memory, interconnect, PCIe and power-management controls for the processor sockets.

| Area | What it controls |
| --- | --- |
| Processor Configuration | Core-related and processor feature controls. Active Cores is not documented as a simple core count: its help describes `0` as all cores enabled and `3fff` as all disabled. |
| Common Configuration | Shared processor reference-code settings, including MMIO resource placement and other platform-wide choices. |
| UPI Configuration | CPU-to-CPU interconnect behavior. UPI is the link between processor sockets, so changes can affect a multi-socket system rather than a single PCIe device. |
| IIO Configuration | The CPU's Integrated I/O, including CPU-connected PCIe ports. IOU lane configuration and port width/speed choices can affect whether devices enumerate. These are different ports from the PCH's PCIe ports. |
| IOAT Configuration | I/O acceleration-related platform controls. Whether a feature is useful depends on hardware and driver support. |
| Memory Configuration | Memory frequency, training policy and related memory-controller choices. The displayed frequency is a limit or requested policy, not a guarantee of the speed the DIMMs will achieve. |
| Memory Timings Override | Manual timing and voltage settings. A valid input range does not establish safe or stable operating values. |
| Memory Map | Memory placement, interleaving and address-map choices. These can affect capacity visible to the OS and device address allocation. |
| Memory RAS Configuration | Reliability, Availability and Serviceability features such as correction and redundancy-related policies. Some modes require a particular DIMM population or trade usable capacity for redundancy. |
| NGN Configuration | Persistent-memory-related settings, including the explicit NVMDIMM erase controls. These should not be treated as ordinary DRAM tuning. |
| Advanced Power Management Configuration | CPU and package power policy, idle states, thermal management, RAPL limits and related tuning. A core C-state and a package C-state affect different levels of idle behavior. |
| Memory Power & Thermal Configuration | DRAM power limits and thermal behavior. The forms include controls that can disable throttling or ignore MEMtrip. |

DFX, BSSA, training tests, error injection and similar pages are engineering or diagnostic functions. Their presence is not evidence of support for routine operation.

## Chipset

[Platform](menu-map/f44ace4934bd-0.md) contains PCH devices and platform-wide controls. The firmware labels this formset Chipset. AMITSE has a separate entry for it, even though a different Chipset reference inside Setup is always suppressed.

| Area | What it controls |
| --- | --- |
| PCH Configuration | Functions on the Platform Controller Hub and references to its device, security and thermal settings. |
| PCH SATA and sSATA | Two storage-controller groups. Mode, port enablement and related settings can affect an installed OS's storage path. |
| USB Configuration | USB controller and port behavior. Changing the wrong port can also remove a keyboard or remote virtual-media path. |
| PCH PCIe | PCH-connected PCIe ports, distinct from the CPU IIO ports. |
| Security Configuration | Firmware-protection controls such as SMM BIOS Write Protect. These are separate from hiding the setup menu. |
| Runtime Error Logging | How platform errors are reported and handled. The neighboring error-injection pages intentionally exercise failure paths. |
| Server ME Debug Configuration | Firmware management-engine/SPS-related debug settings. Showing these controls does not grant flashrom access to the locked ME region. |
| OverClocking Feature | Reference-code ratio and voltage controls. Availability in the form is not proof that the installed processor implements them. |

Some vendor help is imprecise. For example, SATA Mode Options offers AHCI and RAID while its help text talks about identifying SSDs and HDDs. The catalogue preserves that discrepancy. When labels, choices and help conflict, the actual handler would need inspection before relying on an interpretation.

## Server management

[ServerMgmtSetup](menu-map/24368718aeae-0.md) contains BMC information, event logs, watchdog/network-related controls and BMC users. These are management-controller settings, so changing them can affect the way the server is reached or monitored even when the OS configuration is unchanged. Deleting users or clearing logs has consequences beyond changing the BIOS screen layout.

## Other formsets

- [FPGA Configuration](menu-map/8893a580c7a4-0.md) contains controls for a supported FPGA configuration. It does not imply an FPGA is fitted to this server.
- [NVMe information](menu-map/17b300eea373-0.md) is mostly a container for runtime controller and drive information. A static image cannot list every control the driver may insert for installed devices.
- [Recovery](menu-map/bdc5290bdcb5-0.md) contains firmware recovery/update forms rather than normal performance settings.
- RSTe and VROC forms manage compatible Intel storage configurations. Multiple driver variants are bundled in the image; they are kept separate in the catalogue.
- Intel Ethernet and Omni-Path forms describe the corresponding device drivers. Their registration and installed hardware determine whether they appear.
- [Intel DIMM Gen 1 Configuration](menu-map/5fbcd3def87d-0.md) contains persistent-memory management, security, namespace and firmware-update pages. Its English string table was recovered from an original `en` language package.

## Deciding whether a setting needs the unlock

Follow the Access line and the conditions below a control. A CMOS vendor gate is tied to one of the four restriction variables. The map evaluates that part with the flag set to `1` for stock and `0` for unlocked. Other values are left unknown, so conditional means the result depends on hardware, another setting or runtime state.

A control can have a vendor gate and still remain disabled by SystemAccess, Secure Boot state, a missing device, or an unconditional condition. Conversely, a page can have no local vendor gate but sit behind a reference that does. The map carries the selected route's conditions into each entry and lists incoming references for checking alternate routes.

The AMITSESetupData access-level policy and the full callback implementations have not been decoded. A static IFR map therefore cannot guarantee the exact screen or behavior on an unlocked running server.

The [risk notes](risks.md) describe the implications of changing these controls. No configuration changes or boot tests were performed while building the catalogue.
