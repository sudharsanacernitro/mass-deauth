#!/usr/bin/env python
import os
import sys
import getopt
import time
f = None
l= None
	

argv = sys.argv[1:]

try:
	opts, args = getopt.getopt(argv, "f:l:")
	
except:
	print("Error")

for opt, arg in opts:
	if opt in ['-f']:
		f = arg
	elif opt in ['-l']:
		l=arg

print(l)
print(f)
command="timeout 4s aireplay-ng -0 10 -a "+f+" wlp0s20f3mon"
#os.popen("sudo -S %s"%(command), 'w').write('Sudharsan@ubuntu')
password = "Sudharsan@ubuntu"

# Construct the sudo command
sudo_command = f"echo {password} | sudo -S {command}"

# Execute the sudo command
os.system(sudo_command)
time.sleep(6)


