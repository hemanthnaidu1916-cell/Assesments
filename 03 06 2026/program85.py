import zlib

text = "hello world!hello world!hello world!hello world!"

compressed = zlib.compress(text.encode())

print("Compressed data:")
print(compressed)

decompressed = zlib.decompress(compressed).decode()

print("\nDecompressed data:")
print(decompressed)
