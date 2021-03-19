import LCD1602
import time


class LCDoutput:
    def __init__(self):
        self.lcd = LCD1602.Screen(bus=1, addr=0x27, cols=16, rows=2)
        self.lcd.enable_backlight()
        self.lcd.display_data("", "")
        
    def output(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.lcd.display_data(self.data1, self.data2)
        time.sleep(2)
        self.lcd.display_data("", "")

if __name__ == "__main__":
    lcd = LCD1602.Screen(bus=1, addr=0x27, cols=16, rows=2)
    lcd.enable_backlight()
    lcd.display_data("fuck", "shit")
    time.sleep(0.1)
    lcd.display_data("", "")