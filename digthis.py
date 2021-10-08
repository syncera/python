#!/usr/bin/env python3
# sincera

import os
import base64

this = str('noshitsecurity.com')
shit = os.popen("dig " + this + " txt | grep pithos | cut -d '=' -f 2 | sed '$s/.$//'").read().strip()

def dig(this):
    right = shit.encode('ascii')
    here = base64.b64decode(right + b'==')
    goes = here.decode('ascii', errors='ignore')
    hard = []
    for i in range(len(goes)):
        c = ord(goes[i])
        if c >= 33 and c <= 126:
            hard.append(chr(28 + ((c + 14) % 94)))
        else:
            hard.append(goes[i])
    return ''.join(hard [::-1]).split('\n')

if __name__ == "__main__":
    dig(this)