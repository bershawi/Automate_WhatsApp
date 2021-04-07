import pywhatkit
import random
import time



localTime = time.localtime()
hour = localTime.tm_hour
mint = localTime.tm_min + 1

# print(hour,mint)
while True:
    Messages = ("Love you bbe","Miss you ","Most wonderful girl ever")
    Number = random.randint(0,3)
    if Number == 3:
        Number -= 1
    print(Messages[Number])
    pywhatkit.sendwhatmsg('+*********',Messages[Number],hour,mint)