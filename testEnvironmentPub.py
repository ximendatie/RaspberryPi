import paho.mqtt.publish as publish
import time
from time import ctime,sleep
import json
import random

# import RPi.GPIO as GPIO


#hostname='162.105.80.59'
# hostname='192.168.199.231' # hewei IP
hostname='127.0.0.1'


def pub_Temperature(t,h):
    
    content_json={"temperature":t,"humidity":h}
    print("== deviceData Pub:"+json.dumps(content_json))
    msg=[{
        'topic':"rawEnvironment",
        'payload':json.dumps(content_json),
        'qos':0,
        'retain':False
    }]
    publish.multiple(msg,hostname=hostname)



if __name__ == "__main__":
    
    while True :
        temperature=random.randint(15, 30)
        humidity=random.randint(12, 20)
        pub_Temperature(temperature,humidity)
        time.sleep(5)
