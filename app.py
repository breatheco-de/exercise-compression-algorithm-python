import sys, time
from pathlib import Path
from compress import compress
from decompress import decompress

    
f = open("data/document.txt","r")
content = ''.join(list(f))
f.close()

start_time = time.time()
_compressed = compress(content)
length_in_time = time.time() - start_time
_decompressed = decompress(_compressed)

f = open("data/compressed.txt","w+")
f.write(compress(content))
f.close()

if(_decompressed == content):
    print("✅No data lost.")
else:
    print(f"❌Some data was lost", _decompressed, content)
initial = Path('data/document.txt').stat().st_size
last = Path('data/compressed.txt').stat().st_size
percentage = 100 - round(last / initial * 100)
print(f"\033[1;33;40m document.txt has {initial} size, compressed.txt has {last} size, compression of {percentage}% in {length_in_time} seconds \033[0m")

