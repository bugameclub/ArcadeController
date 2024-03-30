import hid
import pyautogui

SPEED = 20


#open device:

h2 = hid.device()
h2.open(0x0079, 0x0006)


try:
    while True:
        d = h2.read(64, 100)
        if d:
            x = d[0]
            y = d[1]
            x = (x - 127) // 127
            y = (y - 127) // 127
            x *= SPEED 
            y *= SPEED
            perint(x, y)
            

            pyautogui.move(x, y)
            time.sleep(0.05)
            
except KeyboardInterrupt:
    pass


h2.close()
