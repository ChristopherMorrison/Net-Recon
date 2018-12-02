# randomly change my mac address every 5 minutes (requires taking the if down and up which kills all tcp sessions and may upset udp responses)
import os
import time

interface = 'tap0'

while 1:
    os.system('ip link set dev ' + interface + ' down')
    os.system('macchanger -r ' + interface)
    os.system('ip link set dev ' + interface + ' up')
    time.sleep(5*60)
    
