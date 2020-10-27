import RPi.GPIO as GPIO
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.output(5, False)

with open('/home/pi/Desktop/DT Stuff/save.json') as file:
    data = json.load(file)
    data["aeration"] = 0
    json.dump(data, open('/home/pi/Desktop/DT Stuff/save.json','w'))
