import cgfi

cgfi.convert_bin_to_vpk("Example.bin", "ac.header", "gba.vpk", "Example.vpk")
cgfi.convert_vpk_to_dec("Example.vpk", "Example.dec")

card = cgfi.Letter()

with open("Example.dec", "rb") as f:
    card.contents = f.read(248)
    card.letter_type = f.read(1)
    card.item_id = f.read(2)
    card.villager = f.read(2)
    card.name_position = f.read(1)
    card.card_id = f.read(2)

print(card.contents)
print("Letter Type:   0x{:02X}".format(int.from_bytes(card.letter_type, byteorder="big")))
print("Item ID:       0x{:04X}".format(int.from_bytes(card.item_id, byteorder="big")))
print("Villager:      0x{:04X}".format(int.from_bytes(card.villager, byteorder="big")))
print("Name Position: 0x{:02X}".format(int.from_bytes(card.name_position, byteorder="big")))
print("Card ID:       0x{:04X}".format(int.from_bytes(card.card_id, byteorder="big")))
