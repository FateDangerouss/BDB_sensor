import ultrasonic as us
import time
import camera
import imageclassify
import gpio


tuple_1 = ("平板电脑", "笔记本电脑", "商品-数码产品")
tuple_2 = ("书本", "商品-图书", "书稿", "文字图片", "电纸书", "书籍")
tuple_3 = ("商品-床上用品", "商品-家纺", "商品-医疗器材", "商品-汽车用品", "商品-布料", "商品-穿戴", "商品-箱包")

objlist = []

num_1 = 0
num_2 = 0
num_3 = 0

state_1 = 0
state_2 = 0
state_3 = 0
state_4 = 0

state = 0
res = 0

vcc = gpio.myGPIO([21, "OUT"])
vcc.output(21, "HIGH")

IO = gpio.myGPIO([19, "OUT", 13, "OUT", 16, "OUT", 12, "OUT", 0, "OUT", 5, "OUT", 1, "OUT", 6, "OUT", 7, "IN"])
IO.output(19, "LOW")
IO.output(13, "LOW")
IO.output(16, "LOW")
IO.output(12, "LOW")
IO.output(0, "LOW")
IO.output(5, "LOW")
IO.output(1, "LOW")
IO.output(6, "LOW")

objdet = us.Ultrasonic(26, 20)
box_1 = us.Ultrasonic(2, 3)
box_2 = us.Ultrasonic(4, 14)
box_3 = us.Ultrasonic(15, 17)
box_4 = us.Ultrasonic(27, 22)

cam = camera.camera()
img = imageclassify.ImageClassify()


while True:
    while True:
        if state == 0:
            while True:
                if objdet.distance() <= 50:
                    break
                else:
                    time.sleep(0.5)
            objlist = []
            cam.get()                                                                                                                                                       
            img.get_file('object.jpg')
            item = img.get_item()   
            print(str(item['result']) + '\n')
            result = ''
            for i in range(0,5):
                if item['result'][i]['score'] >= 0.3:
                    objlist.append(item['result'][i]['root'])
                    objlist.append(item['result'][i]['keyword'])
                    result = result + item['result'][i]['root'] + '\n' + item['result'][i]['keyword'] + '\n\n'
            print(result)
            res = 1

        if res == 1:
            num_1 = 0
            num_2 = 0
            num_3 = 0
            for i in objlist:
                if i in tuple_1:
                    num_1 += 1
                elif i in tuple_2:
                    num_2 += 1
                elif i in tuple_3:
                    num_3 += 1
            if (num_1 * num_2 != 0) or (num_2 * num_3 != 0) or (num_3 * num_1 != 0):
                print("请每次放置一种物品。")
            elif num_1 != 0:
                IO.output(19, "HIGH")
                print(1)
                time.sleep(1)
                IO.output(19, "LOW")
            elif num_2 != 0:
                print(2)
                IO.output(13, "HIGH")
                time.sleep(1)
                IO.output(13, "LOW")
            elif num_3 != 0:
                print(3)
                IO.output(16, "HIGH")
                time.sleep(1)
                IO.output(16, "LOW")
            elif num_1 == num_2 == num_3 == 0 and objlist != []:
                print(4)
                IO.output(12, "HIGH")
                time.sleep(1)
                IO.output(12, "LOW")
            res = 0

        if state == 0 and IO.input(7) == 1:
            state = 1
        elif state == 1 and IO.input(7) == 0:
            state = 0
        
        time.sleep(0.1)
