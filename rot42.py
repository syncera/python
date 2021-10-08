#!/usr/bin/env python3
# sincera

def rtr(n):
    d = []
    for i in range(len(n)):
        c = ord(n[i])
        if c >= 33 and c <= 126:
            d.append(chr(28 + ((c + 14) % 94)))
        else:
            d.append(n[i])
    return ''.join(reversed(d))

rtr('test string here')