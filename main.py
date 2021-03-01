import ultrasonic as us
from time import sleep
import threading

man_info = 0
state = 0

mandet = us.Ultrasonic(17,18)

def det_man():
    while True:
        if mandet.distance() <= 50:
            man_info = 1
            print(1)
            print("start working")
            break
        else:
            man_info = 0
            print(0)
        sleep(0.5)

t_dm = threading.Thread(target = det_man, name = "det_man")

t_dm.start()
t_dm.join()
print("end")