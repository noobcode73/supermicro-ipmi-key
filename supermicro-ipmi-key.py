#!/usr/bin/python3
from hashlib import sha1
import hmac
import re
import sys


KEY = b"\x85\x44\xe3\xb4\x7e\xca\x58\xf9\x58\x30\x43\xf8"

arg = "empty" if len(sys.argv) == 1 else sys.argv[1]
mac = "".join(re.findall('[a-fA-F0-9]', arg))[:12]

if len(mac) == 12:
    data = bytes.fromhex(mac)
    hashed = hmac.new(KEY, data, sha1).hexdigest()[:24]
    out = " ".join(re.findall('....', hashed))
    
    print("MAC:", arg)
    print("KEY:", out)
else:
    print("mac not validated:", arg)
