# uses ifconfig to change ip to a random ip on the subnet,
# bound by the randrange(x) as y.y.y.1 - y.y.y.x
# time.sleep(3*60) means it waits 3 minutes between changing

assert False, "Delete this line to agree to the MIT license this code was released under"

import os
import random
import time
exit()
interface = 'tap0'
prefix_ip = '10.8.0.'
while 1:
    os.system('clear')
    os.system('ifconfig ' + interface + ' '+ prefix_ip + str(random.randrange(80)+1) + '/24')
    os.system('ifconfig ' + interface)
    time.sleep(3*60)
