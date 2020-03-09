#!/usr/bin/env python3
# sincera

import string
k = input("Enter the key to rotate: ")
rot13 = bytes.maketrans(
    b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
b'k'.translate(rot13)