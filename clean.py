from datetime import datetime
import time

Alarm = "12:00:00"
while True:
    t = time.localtime()

    current = time.strftime("%H:%M:%S", t)
    print(current)

    if(current == Alarm):
        with open("/var/log/auth.log", "w") as file:
            file.write('')
        print("Data Wiped")
        break
