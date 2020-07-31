from ctypes import *

nedclib = CDLL('nedclib.dll')

class FILE(Structure):
    pass

#--- common external functions ---
nedclib_version = getattr(nedclib, '?nedclib_version@@YAXXZ')
nedclib_version.argtypes = None
nedclib_version.restype = None

is_vpk = getattr(nedclib, '?is_vpk@@YAHPAE@Z')
is_vpk.argtypes = [POINTER(c_uint8)]
is_vpk.restype = c_int

is_nes = getattr(nedclib, '?is_nes@@YAHPAE@Z')
is_nes.argtypes = [POINTER(c_uint8)]
is_nes.restype = c_int

is_bmp = getattr(nedclib, '?is_bmp@@YAHPAD@Z')
is_bmp.argtypes = [c_char_p]
is_bmp.restype = c_int

version_major = c_int.in_dll(nedclib, '?version_major@@3HA')
version_minor = c_int.in_dll(nedclib, '?version_minor@@3HA')
MultiStrip = c_int.in_dll(nedclib, '?MultiStrip@@3HA')

#--- RAW2BMP FUNCTIONS ---
raw2bmp = getattr(nedclib, '?raw2bmp@@YAHPAD0@Z')
raw2bmp.argtypes = [c_char_p, c_char_p]
raw2bmp.restype = c_int

bmp2raw = getattr(nedclib, '?bmp2raw@@YAHPAD0@Z')
bmp2raw.argtypes = [c_char_p, c_char_p]
bmp2raw.restype = c_int

raw2bmp_f = getattr(nedclib, '?raw2bmp_f@@YAHPAEPAD@Z')
raw2bmp_f.argtypes = [POINTER(c_uint8), c_char_p]
raw2bmp_f.restype = c_int

smooth = c_int.in_dll(nedclib, '?smooth@@3HA')

#--- BIN2RAW FUNCTIONS ---
bin2raw = getattr(nedclib, '?bin2raw@@YAHPAD0@Z')
bin2raw.argtypes = [c_char_p, c_char_p]
bin2raw.restype = c_int

raw2bin = getattr(nedclib, '?raw2bin@@YAHPAD0@Z')
raw2bin.argtypes = [c_char_p, c_char_p]
raw2bin.restype = c_int

fixraw = getattr(nedclib, '?fixraw@@YAHPAD@Z')
fixraw.argtypes = [c_char_p]
fixraw.restype = c_int

bin2raw_d = getattr(nedclib, '?bin2raw_d@@YAHPAE0H@Z')
bin2raw_d.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_int]
bin2raw_d.restype = c_int

bin2raw_f = getattr(nedclib, '?bin2raw_f@@YAHPAEPADH@Z')
bin2raw_f.argtypes = [POINTER(c_uint8), c_char_p, c_int]
bin2raw_f.restype = c_int

signature = c_int.in_dll(nedclib, '?signature@@3HA')
signature_str = c_uint8.in_dll(nedclib, '?signature_str@@3PAEA')
dpi_multiplier = c_int.in_dll(nedclib, '?dpi_multiplier@@3HA')

#--- NEVPK FUNCTIONS ---
NVPK_compress = getattr(nedclib, '?NVPK_compress@@YAHPAEHHHHHPAU_iobuf@@0@Z')
NVPK_compress.argtypes = [POINTER(c_uint8), c_int, c_int, c_int, c_int, c_int, POINTER(FILE), POINTER(c_uint8)]
NVPK_compress.restype = c_int

vpk_decompress = getattr(nedclib, '?vpk_decompress@@YAHPAEPAU_iobuf@@@Z')
vpk_decompress.argtypes = [POINTER(c_uint8), POINTER(FILE)]
vpk_decompress.restype = c_int

log_write = getattr(nedclib, '?log_write@@YAXPADZZ')
#log_write.argtypes = [c_char_p, ...]
log_write.restype = None

log = POINTER(FILE).in_dll(nedclib, '?log@@3PAU_iobuf@@A')
verbose = c_int.in_dll(nedclib, '?verbose@@3HA')
bits_written = c_uint32.in_dll(nedclib, '?bits_written@@3KA')
best_move = c_int.in_dll(nedclib, '?best_move@@3HA')
best_size = c_int.in_dll(nedclib, '?best_size@@3HA')
skip_huffman = c_int.in_dll(nedclib, '?skip_huffman@@3HA')
skip_lz77 = c_int.in_dll(nedclib, '?skip_lz77@@3HA')

#--- NES FUNCTIONS ---
make_nes = getattr(nedclib, '?make_nes@@YAHPAE@Z')
make_nes.argtypes = [POINTER(c_uint8)]
make_nes.restype = c_int

nes_enc = getattr(nedclib, '?nes_enc@@YAGG@Z')
nes_enc.argtypes = [c_uint16]
nes_enc.restype = c_uint16

nes_dec = getattr(nedclib, '?nes_dec@@YAGG@Z')
nes_dec.argtypes = [c_uint16]
nes_dec.restype = c_uint16
