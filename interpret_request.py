try:
    import sys, json, os
    os.system('sudo date --set=\'TZ="Europe/London"'+ sys.argv[1] +"'")
    
    if (sys.argv[2] == 'start'):
        with open("/home/pi/Desktop/DT Stuff/save.json") as file:
            data =  json.load(file)
            data["start"][sys.argv[3]] = (sys.argv[4] if len(sys.argv[4]) == 2 else "0"+sys.argv[4])
            json.dump(data, open("/home/pi/Desktop/DT Stuff/save.json", "w"))
        os.system('python3 "/home/pi/Desktop/DT Stuff/light_flash.py"')

    elif (sys.argv[2] == 'end'):
        with open("/home/pi/Desktop/DT Stuff/save.json") as file:
            data =  json.load(file)
            data["end"][sys.argv[3]] = (sys.argv[4] if len(sys.argv[4]) == 2 else "0"+sys.argv[4])
            json.dump(data, open("/home/pi/Desktop/DT Stuff/save.json", "w"))
        os.system('python3 "/home/pi/Desktop/DT Stuff/light_flash.py"')

    elif (sys.argv[2] == 'light'):
        if (sys.argv[3] == 'on'): 
            import toggles.light_on
        elif (sys.argv[3] == 'off'):
            import toggles.light_off
        with open("/home/pi/Desktop/DT Stuff/save.json") as file:
            data =  json.load(file)
            requestTime = sys.argv[1].split(' ')
            print(requestTime)
            data["override"] = requestTime[0]+"/"+(str(['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].index(requestTime[1])) if len(str(['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].index(requestTime[1]))) == 2 else ("0"+str(['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].index(requestTime[1]))) )+"/"+requestTime[2]+" "+requestTime[3]
            json.dump(data, open("/home/pi/Desktop/DT Stuff/save.json", "w"))
            
    elif (sys.argv[2] == 'aeration'):
        if (sys.argv[3] == 'on'):
            import toggles.aeration_on
        elif (sys.argv[3] == 'off'):
            import toggles.aeration_off
        os.system('python3 "/home/pi/Desktop/DT Stuff/light_flash.py"')

except Exception as e:
    open('e.txt','w+').write(str(e))