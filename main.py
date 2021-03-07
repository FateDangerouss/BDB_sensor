import ultrasonic as us
import threading as th
from time import sleep
import camera
import imageclassify
import gpio

state = 0

vcc = gpio.myGPIO([21, "OUT"])
vcc.output(21, "HIGH")

mandet = us.Ultrasonic(20,26)
cam = camera.camera()
img = imageclassify.ImageClassify()

def det():
    while True:
        if state == 0:
            while True:
                if mandet.distance() <= 50:
                    state = 1
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
            state = 0
        else:
            time.sleep(0.5)
            
            

th_det = th.Thread(target=det(), name='Threading Detective')

while True:
    th_det.start()