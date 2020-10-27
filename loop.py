import time, json, datetime, os
def hmToS(hm):
    hm = hm.split(" ")
    seconds = int(hm[0]) * 60 * 60
    seconds += int(hm[1]) * 60
    return seconds

while True:
    time.sleep(5)
    file = open("/home/pi/Desktop/DT Stuff/save.json")
    readFile = file.read()
    file.close()
    data = json.loads(readFile)
    
    todayStamp = time.mktime(time.strptime(datetime.datetime.today().strftime("%d %m %Y"), "%d %m %Y"))

    startStamp = todayStamp + hmToS(data["start"]["hours"]+" "+data["start"]["minutes"])
    endStamp = todayStamp + hmToS(data["end"]["hours"]+" "+data["end"]["minutes"])
    nowStamp = todayStamp + hmToS(datetime.datetime.now().strftime("%H %M"))
    overrideStamp = time.mktime(time.strptime(data["override"], "%d/%m/%Y %H:%M"))
    
    if startStamp > endStamp:
        flip = True
        x = startStamp
        startStamp = endStamp
        endStamp = x
    else:
        flip = False
    
    prevEndStamp = endStamp - 86400
    nextStartStamp = startStamp + 86400
    
    if nowStamp >= prevEndStamp and nowStamp < startStamp:
        nowRange = 1
    elif nowStamp >= startStamp and nowStamp < endStamp:
        nowRange = 2
    elif nowStamp >= endStamp and nowStamp < nextStartStamp:
        nowRange = 3
    
    overrideRange = 0
    if overrideStamp >= prevEndStamp and overrideStamp < startStamp:
        overrideRange = 1
    elif overrideStamp >= startStamp and overrideStamp < endStamp:
        overrideRange = 2
    elif overrideStamp >= endStamp and overrideStamp < nextStartStamp:
        overrideRange = 3
    
    if nowRange != overrideRange:
        if not flip:
            action = ['', 'off', 'on', 'off'][nowRange]
        else:
            action = ['', 'on', 'off', 'on'][nowRange]
        
        if action == 'on':
            os.system('python3 "/home/pi/Desktop/DT Stuff/toggles/light_on.py"')
        else:
            os.system('python3 "/home/pi/Desktop/DT Stuff/toggles/light_off.py"')