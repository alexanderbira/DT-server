try:
    import RPi.GPIO as GPIO
    import time, json, os, datetime
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.IN)
    GPIO.setup(21, GPIO.IN)

    oneDown = False
    twoDown = False

    while True:
        time.sleep(0.05)
        data = json.load(open('/home/pi/Desktop/DT Stuff/save.json'))
        
        if (GPIO.input(20)==GPIO.LOW) and not oneDown:
            if (data["light"] == 0):
                os.system('python3 "/home/pi/Desktop/DT Stuff/toggles/light_on.py"')
            else:
                os.system('python3 "/home/pi/Desktop/DT Stuff/toggles/light_off.py"')
            oneDown = True
            with open("/home/pi/Desktop/DT Stuff/save.json") as file:
                data =  json.load(file)
                data["override"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                json.dump(data, open("/home/pi/Desktop/DT Stuff/save.json", "w"))
            
        elif not (GPIO.input(20)==GPIO.LOW):
            oneDown = False
            
            
            
        if (GPIO.input(21)==GPIO.LOW) and (not twoDown):
            if (data["aeration"] == 0):
                os.system('python3 "/home/pi/Desktop/DT Stuff/toggles/aeration_on.py"')
            else:
                os.system('python3 "/home/pi/Desktop/DT Stuff/toggles/aeration_off.py"')
            twoDown = True

        elif not (GPIO.input(21)==GPIO.LOW):
            twoDown = False
except Exception as e:
    open("why.txt","w+").write(str(e))