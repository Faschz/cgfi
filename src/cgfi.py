import nedclib

#TODO: Currently functions passing a FILE* do not work, thus an executable
# provided by the nedclib developer's kit is used as a temporary fix.
import os

class Card():
    def __init__(self):
        pass

class Letter(Card):
    def __init__(self, contents="", letter_type=0x00, item_id=0x00, villager=0xD000, name_position=0x00, card_id=0x0000):
        super().__init__()

        self.contents = contents
        self.letter_type = letter_type
        self.item_id = item_id
        self.villager = villager
        self.name_position = name_position
        self.card_id = card_id

        self.clamp_values()

    def clamp_values(self):
        """
        Set the card contents to specific byte lengths to fit inside the binary
        data for the e-reader card file.
        """

        self.contents = self.contents.ljust(248)[:248]
        self.letter_type &= 0xFF
        self.item_id &= 0xFFFF
        self.villager &= 0xFFFF
        self.name_position &= 0xFF
        self.card_id &= 0xFFFF

    def create_dec(self, file):
        """
        Creates the .dec file from the card object for a post office letter.

        @param file: Path to the .dec file.
        """

        # Make sure all of the data is valid!
        self.clamp_values()

        b = bytearray()

        b.extend(map(ord, self.contents))
        b.extend(self.letter_type.to_bytes(1, byteorder="big"))
        b.extend(self.item_id.to_bytes(2, byteorder="big"))
        b.extend(self.villager.to_bytes(2, byteorder="big"))
        b.extend(self.name_position.to_bytes(1, byteorder="big"))
        b.extend(self.card_id.to_bytes(2, byteorder="big"))

        with open(file, "wb") as f:
            f.write(b)

class Design(Card):
    def __init__(self):
        super().__init__()

def convert_dec_to_vpk(src, dst):
    """
    Convert an e-reader .dec to .vpk.

    @param src: Path to the .dec file.
    @param dst: Path to the .vpk file.
    """

    #TODO: Replace the command line functionality with nedclib capabilities.
    #nedclib.NVPK_compress(data_in, 256, 2, 4096, 256, 0, file_out, None)
    os.system("nevpk.exe -i {} -o {} -v -c -level 2".format(src, dst))

def convert_vpk_to_dec(src, dst):
    """
    Convert an e-reader .vpk to .dec.

    @param src: Path to the .vpk file.
    @param dst: Path to the .dec file.
    """

    #TODO: Replace the command line functionality with nedclib capabilities.
    #nedclib.vpk_decompress(data_in, file_out)
    os.system("nevpk.exe -i {} -o {} -v -d".format(src, dst))

def convert_vpk_to_bin(src1, src2, src3, dst):
    """
    Converts an e-reader's .vpk files and header file into a .bin file.

    @param src1: Path to the header file.
    @param src2: Path to the GBA .vpk file.
    @param src3: Path to the GC .vpk file.
    @param dst: Path to the .bin file.
    """

    b = bytearray()

    with open(src1, "rb") as f:
        b.extend(f.read())

    with open(src2, "rb") as f:
        b.extend(f.read())

    with open(src3, "rb") as f:
        b.extend(f.read())

    b = b.ljust(0x081C, b'\x00')[:0x081C]

    with open(dst, "wb") as f:
        f.write(b)

def convert_bin_to_vpk(src, dst1, dst2, dst3):
    """
    Converts an e-reader .bin file to .vpk files and a header file.

    @param src: Path to the .bin file.
    @param dst1: Path to the header file.
    @param dst2: Path to the GBA .vpk file.
    @param dst3: Path to the GC .vpk file.
    """

    with open(src, "rb") as f:
        b = f.read()

    # 'vpk0' signifies the start of a .vpk file.
    b = b.split(b"vpk0")

    with open(dst1, "wb") as f:
        f.write(b[0])

    with open(dst2, "wb") as f:
        f.write(b"vpk0")
        f.write(b[1])

    with open(dst3, "wb") as f:
        f.write(b"vpk0")
        f.write(b[2])

def convert_bin_to_raw(src, dst):
    """
    Convert an e-reader .bin to .raw.

    @param src: Path to the .bin file.
    @param dst: Path to the .raw file.
    """

    nedclib.bin2raw(src, dst)

def convert_raw_to_bin(src, dst):
    """
    Convert an e-reader .raw to .bin.

    @param src: Path to the .raw file.
    @param dst: Path to the .bin file.
    """

    nedclib.raw2bin(src, dst)

def convert_raw_to_bmp(src, dst):
    """
    Convert an e-reader .raw to .bmp.

    @param src: Path to the .raw file.
    @param dst: Path to the .bmp file.
    """

    nedclib.dpi_multiplier.value = 2
    nedclib.raw2bmp(src, dst)
