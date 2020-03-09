# This script is designed to scan the two domain controllers
# and then the subnet
# sincera

import nmap
import datetime
weekday = datetime.date.today().weekday()
nm = nmap.Portscanner()
if weekday == 1:
    nm.scan('10.10.10.254')
elif weekday == 3:
    nm.scan('10.10.10.253')
else:
    nm.scan('10.10.10.0/23')
