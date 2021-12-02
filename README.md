# cgfi
A Custom e-Reader Card Creator for Animal Crossing on the Nintendo GameCube.

# Prerequisites
* Animal Crossing e-Reader GBA **.vpk** and associated header file (**.raw** or **.bin** can be converted)
* [NEDCLIB.DLL](https://www.caitsith2.com/ereader/devtools.htm)
* 32-bit Python

# Features
* Generate **.dec** files from **.raw** or **.bin** to obtain e-Reader card information
* Generate **.bin** files to be used on Dolphin + VisualBoyAdvance
* Generate **.bmp** files to be printed and used on actual hardware

# How to Use
The contents of each decoded e-Reader card is as follows:

| Offset | Size (bytes) | Description          |
|--------|--------------|----------------------|
| 0x00   | 248          | Message              |
| 0xF8   | 1            | Background           |
| 0xF9   | 2            | Item ID              |
| 0xFB   | 2            | Villager ID          |
| 0xFD   | 1            | Name Insertion Index |
| 0xFE   | 2            | Card ID              |

These decoded files are created in cgfi.py. With the use of nedclib.py and nedclib.dll they are then converted to .bin or .bmp files. The .bin files can be loaded into VisualBoyAdvance and used in conjunction with a compatible version of Dolphin. The .bmp files can be printed and scanned using an e-Reader and Nintendo GameCube/Wii with a copy of Animal Crossing.

# Thanks
* **caitsith2**, for Nintendo e-Reader Dev Tools
