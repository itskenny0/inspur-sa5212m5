# BIOS 3.0.29 menu map

This is a static catalogue of the setup forms found in the researched Thor02 BIOS. Each form page lists its controls, firmware help, choices, static defaults, storage and visibility conditions. It includes internal questions and option ROM forms as well as the main BIOS menus.

[Unlock research](../README.md) | [Guide to the main areas](../menu-guide.md) | [Risks and recovery](../risks.md) | [Compact setting index](settings.tsv) | [Machine-readable catalogue](catalog.json)

## Coverage

| Item | Count |
| --- | --- |
| sources | 18 |
| form packages | 21 |
| forms | 533 |
| controls including references and internal questions | 8544 |
| question records excluding navigation | 7453 |
| navigation references | 1091 |
| controls with blank prompts | 687 |
| rendered controls and information | 16898 |
| vendor condition on selected path | 5557 |
| controls without help | 1223 |
| conditions | 4255 |
| unparsed condition expressions | 0 |

## Menus and drivers

| Area | Source | Forms |
| --- | --- | --- |
| [FixedBootOrder Group Form](7b6d9df896c5-0.md) | `FboGroupForm` | 10 |
| [iSCSI Configuration](f4e3a92c081e-0.md) | `IScsiDxe` | 5 |
| [Setup](53022c42f931-0.md) | `Setup` | 27 |
| [Server Mgmt](24368718aeae-0.md) | `ServerMgmtSetup` | 11 |
| [Intel PRO/1000 Network Connection](8b45847244f3-0.md) | `4953F720-006D-41F5-990D-0AC7742ABB60` | 7 |
| [Intel(R) Virtual RAID on CPU](15615bf68898-0.md) | `117828F1-DA7D-4BC1-8B58-9A954FED5121` | 17 |
| [Intel DIMM Gen 1 Configuration](5fbcd3def87d-0.md) | `5038E34E-0774-47A0-A5EF-4B94AF1A43DA` | 18 |
| [Intel PRO/1000 Network Connection](85197704ea5c-0.md) | `1A7828FC-DA7D-4BC1-8B58-9A954FED7D70` | 5 |
| [Intel PRO/1000 Network Connection](85197704ea5c-1.md) | `1A7828FC-DA7D-4BC1-8B58-9A954FED7D70` | 12 |
| [Intel(R) RSTe](c6e97345be81-0.md) | `A0327FE0-1FDA-4E5B-905D-B510C45A61D0` | 11 |
| [Intel(R) RSTe](c6e97345be81-1.md) | `A0327FE0-1FDA-4E5B-905D-B510C45A61D0` | 24 |
| [Intel(R) RSTe](761fa09952d9-0.md) | `A0327FE0-1FDA-4E5B-905D-B510C45A61D0` | 11 |
| [Intel(R) RSTe](761fa09952d9-1.md) | `A0327FE0-1FDA-4E5B-905D-B510C45A61D0` | 24 |
| [Intel PRO/1000 Network Connection](d3d39a6b7d36-0.md) | `A0327FE0-1FDA-4E5B-905D-B510C45A61D0` | 8 |
| [Intel Omni-Path HFI Network Connection](98acba206e9f-0.md) | `A0327FE0-1FDA-4E5B-905D-B510C45A61D0` | 2 |
| [!!!! PCI Resource ERROR !!!!](5cd5a764b782-0.md) | `PciOutOfResourceSetupPage` | 1 |
| [Recovery](bdc5290bdcb5-0.md) | `ReFlash` | 2 |
| [NVMe controller and Drive information](17b300eea373-0.md) | `NvmeDynamicSetup` | 2 |
| [Processor](c4ed43ec5ea4-0.md) | `SocketSetup` | 268 |
| [FPGA Configuration](8893a580c7a4-0.md) | `FpgaSocketSetup` | 3 |
| [Chipset](f44ace4934bd-0.md) | `Platform` | 65 |

## Reading the map

- Firmware help explains the vendor's intended behavior. When help is missing or just repeats a label, the map does not invent a description.
- Static defaults are compiled into the form. They are not a readout of current settings, and callbacks or external default stores may override them.
- CMOS vendor gate means a condition refers to byte 1 of one of the four restriction variables controlled by CMOS 0x54. It does not mean the setting will definitely appear or work after unlock.
- SuppressIf hides an item when its expression is true. GrayOutIf and DisableIf restrict interaction. Other condition types can validate or reject changes.
- Expression results only substitute the vendor flag: 1 for stock and 0 for unlock. Other question values remain unknown. No live hardware state or current configuration is assumed.
- Conditions include the selected reference path. Incoming references let you check alternate routes. The selected path prefers routes without a known active suppression after unlock.
- AMITSE GUID/form pairs are root candidates, not proof that a particular menu table is selected at runtime. Driver roots and option ROM pages depend on registration and installed devices.
- AMITSESetupData access-level policy is not decoded here. IFR conditions and question flags describe only part of the setup engine's access decisions.
- Blank spacer subtitles are omitted from the prose pages. Internal questions, blank references and named information fields remain in the JSON.
- Runtime insertion labels mark places where drivers can add device-specific pages. Those generated controls cannot be recovered completely from static IFR.
- Some bundled driver images contain multiple forms and English string tables. The generator chooses a table with sufficient IDs nearest the form package and records that choice in JSON.
- The Intel DIMM Gen 1 driver's original language tag is 'en'. IFRExtractor overlooks that short header. A temporary copy uses 'en-US' with the same string blocks; JSON records the original location and adaptation. No labels are guessed.
- If no English strings can be recovered, explicit unresolved IDs are used. There are no unresolved string-package components in this build.
- Text line breaks and dash typography are normalized. All offsets are in the extracted source body, unless explicitly described as variable or AMITSE offsets.
- This map has not been checked against a rebooted unlocked server. Consult the risk notes before changing controls.

## Searching

Each module index links to its form pages. Search the complete local catalogue with:

```bash
python3 bios/query_menu.py 'CSM Support'
python3 bios/query_menu.py 'voltage' --module Platform
python3 bios/query_menu.py --needs-unlock --limit 50
```

The TSV file can also be opened in a spreadsheet. The JSON contains all conditions, incoming references, source hashes and extraction choices.

## Regenerating

Run UEFIExtract A76 against a copy of the original image, then use IFRExtractor-RS 1.6.1:

```bash
/path/to/uefiextract /path/to/original.bin all
python3 bios/build_menu_map.py --image /path/to/original.bin \
  --dump /path/to/original.bin.dump --ifrextractor /path/to/ifrextractor \
  --output bios/menu-map
```

The generator uses only Python's standard library and the external extractor. It reads the dump, uses temporary files for extraction and writes documentation. It does not access server hardware.

Encoding and condition semantics: [EDK II IFR definitions](https://github.com/tianocore/edk2/blob/master/MdePkg/Include/Uefi/UefiInternalFormRepresentation.h). Firmware extraction: [UEFITool](https://github.com/LongSoft/UEFITool) and [IFRExtractor-RS](https://github.com/LongSoft/IFRExtractor-RS).
