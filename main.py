import ultrasonic as us
from time import sleep
import camera
import imageclassify
import gpio

man_info = 0

out1 = gpio.myGPIO([27,"OUT"])
out1.output(27,"HIGH")

mandet = us.Ultrasonic(21,18)
cam = camera.camera()
img = imageclassify.ImageClassify()

while True:
    while True:
        if mandet.distance() <= 50:
            man_info = 1
            print("start working")
            break
        else:
            man_info = 0
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
