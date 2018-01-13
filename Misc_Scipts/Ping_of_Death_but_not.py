# failed attempt to slow down select remote hosts with large pings,
# doesn't cycle hosts -> start multiple ping processes
# doesn't send large enough packets -> use another program besides ping
import os

#while 1:
for i in [126,111,108]:
    if i != 86:
        os.system('ping -s 65507 10.8.0.' + str(i))
