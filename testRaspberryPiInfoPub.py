
import paho.mqtt.publish as publish
from time import ctime,sleep
import json

import os
import time
import random
 
# Return CPU temperature as a character string                                     
# def getCPUtemperature():
#     res = os.popen('vcgencmd measure_temp').readline()
#     return(res.replace("temp=","").replace("\n",""))
 
# # Return RAM information (unit=kb) in a list                                      
# # Index 0: total RAM                                                              
# # Index 1: used RAM                                                                
# # Index 2: free RAM                                                                
# def getRAMinfo():
#     p = os.popen('free')
#     i = 0
#     while 1:
#         i = i + 1
#         line = p.readline()
#         if i==2:
#             return(line.split()[1:4])
 
# # Return % of CPU used by user as a character string                               
# def getCPUuse():
#     return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
 
# # Return information about disk space as a list (unit included)                    
# # Index 0: total disk space                                                        
# # Index 1: used disk space                                                        
# # Index 2: remaining disk space                                                    
# # Index 3: percentage of disk used                                                 
# def getDiskSpace():
#     p = os.popen("df -h /")
#     i = 0
#     while 1:
#         i = i +1
#         line = p.readline()
#         if i==2:
#             return(line.split()[1:5])
 

#hostname='162.105.80.59'
# hostname='192.168.199.231' # hewei IP
hostname='127.0.0.1'

def pub_Info(Info):

    msg=[{
        'topic':"rawRaspberryPiInfo",
        'payload':json.dumps(Info),
        'qos':0,
        'retain':False
    }]
    publish.multiple(msg,hostname=hostname)
    print(Info)

 

 
if __name__ == '__main__':

    while True:
        
        RaspberryPiInfo = {"CPUTemperature":random.randint(30,80),"CPUUse":random.randint(10,100),"RAMUsed":random.randint(300,1000),"RAMFree":random.randint(300,800),"DiskTotal":1024,"DiskUsed":random.randint(500,800),"DiskUsedPercentage":random.randint(50,80)/100.0}
        pub_Info(RaspberryPiInfo)


        time.sleep(5)
