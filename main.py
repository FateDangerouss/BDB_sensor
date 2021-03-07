import ultrasonic as us
import threading as th
from time import sleep
import camera
import imageclassify
import gpio


list_1 = []
list_2 = []
list_3 = []

num_1 = 0
num_2 = 0
num_3 = 0

state_1 = 0
state_2 = 0
state_3 = 0
state_4 = 0

state = 0
res = 0

vcc = gpio.myGPIO([21, "OUT", 17, "OUT"])
vcc.output(21, "HIGH")
vcc.output(17, "HIGH")

IO = gpio.myGPIO([19, "OUT", 13, "OUT", 16, "OUT", 12, "OUT", 0, "OUT", 5, "OUT", 1, "OUT", 6, "OUT"])

objdet = us.Ultrasonic(26, 20)
box_1 = us.Ultrasonic(2, 3)
box_2 = us.Ultrasonic(4, 14)
box_3 = us.Ultrasonic(15, 17)
box_4 = us.Ultrasonic(27, 22)

cam = camera.camera()
img = imageclassify.ImageClassify()


def det():
    while True:
        if state == 0:
            while True:
                if objdet.distance() <= 50:
                    break
                else:
                    sleep(0.5)
            cam.get()                                                                                                                                                       
            img.get_file('object.jpg')
            item = img.get_item()   
            print(str(item['result']) + '\n')
            result = ''
            for i in range(0,5):
                if item['result'][i]['score'] >= 0.4:
                    result = result + item['result'][i]['root'] + '\n' + item['result'][i]['keyword'] + '\n\n'
            print(result)
            res = 1
        else:
            time.sleep(0.1)

def getstate():
    while True:
        if res == 1:
            
    
def output():
    pass



th_det = th.Thread(target=det(), name='Threading Detective')


while True:
    th_det.start()