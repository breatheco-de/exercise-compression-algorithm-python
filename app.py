import sys, time
from pathlib import Path
from compress import compress
from decompress import decompress


f = open("data/document.txt","r") # open the original document
content = ''.join(list(f)) # add every line to the "content" variable
f.close() #close the file after finishing reading it.

start_time = time.time() # capture time before compressing
_compressed = compress(content) # calling the compression algorithm
length_in_time = time.time() - start_time # capture time after compressing and meassure the differenec
_decompressed = decompress(_compressed) # calling the decompression algorithm

# save the compressed version of the document
f = open("data/compressed.txt","w+")
f.write(compress(content))
f.close()

# make sure source matches the decompressed (to avoid data loss)
if(_decompressed == content):
    print("✅No data lost.")
else:
    print(f"❌Some data was lost", _decompressed, content)

initial = Path('data/document.txt').stat().st_size
last = Path('data/compressed.txt').stat().st_size
percentage = 100 - round(last / initial * 100)
print(f"\033[1;33;40m document.txt has {initial} size, compressed.txt has {last} size, compression of {percentage}% in {length_in_time} seconds \033[0m")

