import RPi.GPIO as GPIO
import json, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

with open('/home/pi/Desktop/DT Stuff/save.json') as file:
    data = json.load(file)

if data["light"] == 1:
    GPIO.output(4, False)
    time.sleep(0.5)
    GPIO.output(4, True)
else:
    GPIO.output(4, True)
    time.sleep(0.5)
    GPIO.output(4, False)