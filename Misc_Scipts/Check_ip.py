# prints the current interface settings every second,
# used to track your own ip / MAC quickly when automating jumping

import os
import time
while 1:
    time.sleep(1)
    os.system('clear')
    os.system('ifconfig tap0')
