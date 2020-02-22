#!/usr/bin/env python3
# random string generator for 16 characters
# sincera

import random, string
r = int(input("What length of characters? "))
code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(r))
print(code)

#while True:
#    remake = str(input("Regenerate? y / n "))
#    while remake.lower() not in ("y", "n"):
#        if remake == "y":
#            r += 1
#            print(gen)
#        exit()
