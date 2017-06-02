""" Compression - modules zlib, gzip, bz2, lzma, zipfile and tarfile."""

import zlib
s = b'witch which has which witches wrist watch'
print("Raw", len(s))


t = zlib.compress(s)
print("Compressed", len(t))

zlib.decompress(t)

zlib.crc32(s)
