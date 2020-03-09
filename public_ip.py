#!/usr/bin/env python3
# doesn't actually work
# sincera

import urllib

def whatsmyip(target):
    gotcha = urllib.build_opener()
    gotcha.addheaders = [('User-agent','Mozilla/5.0')]
    try:
        whatsmyip = gotcha.open(target).read()
    except urllib.HTTPError:
        print("There was an error trying to get this IP: %s " % (error))
    except urllib.URLError:
        print("There was an error trying to get this IP: %s " % (error))
    return whatsmyip

    pub = "None"
    target = "http://ip.42.pl/raw"
    ip = pub(target)

    if not "None" in ip:
        print("Your pubic IP address is %s " % str(ip))
    else:
        print("Your public IP was not found.")
