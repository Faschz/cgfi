# cgfi
A Custom e-Reader Card Creator for Animal Crossing on the Nintendo GameCube.

# Prerequisites
* Animal Crossing e-Reader GBA **.vpk** and associated header file (**.raw** or **.bin** can be converted)
* [NEDCLIB.DLL](https://www.caitsith2.com/ereader/devtools.htm)

# Features
* Generate **.dec** files from **.raw** or **.bin** to obtain e-Reader card information
* Generate **.bin** files to be used on Dolphin + VisualBoyAdvance
* Generate **.bmp** files to be printed and used on actual hardware

# How to Use
The contents of each decoded e-Reader card is as follows:
* 0x00 - 0xF7 = Letter's text
* 0xF8 = Letter's background image
* 0xF9 - 0xFA = ID of item sent with the letter
* 0xFB - 0xFC = ID of villager that sent the letter
* 0xFD = Player's name is inserted in the letter's text at this index
* 0xFE - 0xFF = ID of card (Used in-game to prevent multiple of the same card from being scanned)

These decoded files are created in cgfi.py. With the use of nedclib.py and nedclib.dll they are then converted to .bin or .bmp files. The .bin files can be loaded into VisualBoyAdvance and used in conjunction with a compatible version of Dolphin. The .bmp files can be printed and scanned using an e-Reader and Nintendo GameCube/Wii with a copy of Animal Crossing.

# Thanks
* **caitsith2**, for Nintendo e-Reader Dev Tools
