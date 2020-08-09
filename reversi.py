#!/usr/bin/env python3
# sincera

def rev(n):
    return n[::-1]
fetch = input("Paste the string to be reversed: " + "\n")
if __name__ == "__main__":
    print( "\n" + rev(fetch))