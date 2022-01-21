import time
import func

countfight = 8  # chaque 40 secs
countchop = 12   # chaque 60 secs

while True:
    func.send("m!m")
    m = func.retrieve_last_message()
    if countfight == 8:
        countfight = 0
        func.send("m!f")
        f = func.retrieve_last_message()
    else:
        countfight += 1
    
    if countchop == 12:
        countchop = 0
        func.send("m!c")
        f = func.retrieve_last_message()
    else:
        countchop += 1

    time.sleep(4.4)
    