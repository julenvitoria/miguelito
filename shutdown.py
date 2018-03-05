import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(03, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    print GPIO.input(03)
    print GPIO.input(27)
    if(GPIO.input(03) == False):
        os.system("sudo shutdown -h now")
        break
    if(GPIO.input(27) == False):
        os.system("sudo shutdown -h now")
        break
    time.sleep(1)

