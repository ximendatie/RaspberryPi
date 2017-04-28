
import paho.mqtt.publish as publish
from time import ctime,sleep
import json

import os
import time
 
# Return CPU temperature as a character string                                     
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("\n",""))
 
# Return RAM information (unit=kb) in a list                                      
# Index 0: total RAM                                                              
# Index 1: used RAM                                                                
# Index 2: free RAM                                                                
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
 
# Return % of CPU used by user as a character string                               
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
 
# Return information about disk space as a list (unit included)                    
# Index 0: total disk space                                                        
# Index 1: used disk space                                                        
# Index 2: remaining disk space                                                    
# Index 3: percentage of disk used                                                 
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])
 

#hostname='162.105.80.59'
# hostname='192.168.199.231' # hewei IP
hostname='127.0.0.1'

def pub_Info(Info):

    msg=[{
        'topic':"RaspberryPiInfo",
        'payload':json.dumps(Info),
        'qos':0,
        'retain':False
    }]
    publish.multiple(msg,hostname=hostname)

 

 
if __name__ == '__main__':

    while True:

        # CPU informatiom
        CPU_temp = getCPUtemperature()
        CPU_usage = getCPUuse()
         
        # RAM information
        # Output is in kb, here I convert it in Mb for readability
        RAM_stats = getRAMinfo()
        RAM_total = round(int(RAM_stats[0]) / 1000,1)
        RAM_used = round(int(RAM_stats[1]) / 1000,1)
        RAM_free = round(int(RAM_stats[2]) / 1000,1)
         
        # Disk information
        DISK_stats = getDiskSpace()
        DISK_total = DISK_stats[0]
        DISK_used = DISK_stats[1]
        DISK_perc = DISK_stats[3]

        print('\n-------------------  RaspberryPiInfo.py  ------------------')
        print('CPU Temperature = '+CPU_temp)
        print('CPU Use = '+CPU_usage + '%')
        print('')
        print('RAM Total = '+str(RAM_total)+' MB')
        print('RAM Used = '+str(RAM_used)+' MB')
        print('RAM Free = '+str(RAM_free)+' MB')
        print('') 
        print('DISK Total Space = '+str(DISK_total)+'B')
        print('DISK Used Space = '+str(DISK_used)+'B')
        print('DISK Used Percentage = '+str(DISK_perc))
        
        RaspberryPiInfo = {"CPUTemperature":CPU_temp,"CPUUse":CPU_usage+"%","RAMUsed":str(RAM_used)+"MB","RAMFree":str(RAM_free)+"MB","DiskTotal":str(DISK_total)+"B","DiskUsed":str(DISK_used)+"B","DiskUsedPercentage":str(DISK_perc)}
        pub_Info(RaspberryPiInfo)


        time.sleep(5)
