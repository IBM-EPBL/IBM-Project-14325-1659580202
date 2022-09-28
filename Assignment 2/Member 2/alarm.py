from random import *
import time
import os


while(True):
    temp = randint(1,100)
    humidity = randint(1,100)
    if(temp > 40 and humidity > 40):
        print("alart on")
        os.system("alarm.wav")
        time.sleep(10)
    else:
        print("temperature",temp)
        print("humidity",humidity)
