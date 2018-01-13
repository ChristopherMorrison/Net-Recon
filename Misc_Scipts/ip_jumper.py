# Compilation of the other Check_IP, Mac_Scramble, and Randomize_IP to create a host that continually randomizes mac and ip then runs nmap

import time
import os
import random
import time


prefix_ip = '192.168.2.'
node_ip = None
interface = 'tap0' # doesn't play well with wireless networks

while 1:
    
    # change mac
    os.system('ip link set dev ' + interface + ' down')
    os.system('macchanger -r ' + interface)
    os.system('ip link set dev ' + interface + ' up')
    
    # change ip
    node_ip  = str(random.randrange(255)+1)
    os.system('ifconfig ' + interface + ' '+ prefix_ip + node_ip + '/24')
    os.system('ifconfig ' + interface)
    
    # run scan
    os.system('nmap -sn '+prefix_ip+'1-25')
    print('pausing for 10s')
    time.sleep(10)
    
    
