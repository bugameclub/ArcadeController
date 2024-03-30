import hid
import pyautogui

#open device:

h2 = hid.device()
h2.open(0x0079, 0x0006)


try:
    while True:
        d = h2.read(64)
        if d:
            x = d[0]
            y = d[1]

            pyautogui.move(x * 10, y * 10)
except KeyboardInterrupt:
    pass


h2.close()
