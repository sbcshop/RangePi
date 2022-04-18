

#Receiver code
import utime
from machine import Pin, UART,SPI
import time
import st7789

import vga1_8x16 as font1
#import vga2_8x8 as font
import vga1_16x32 as font
import vga1_16x16 as font2



Mode0 = machine.Pin(2, machine.Pin.OUT)
Mode1 = machine.Pin(3, machine.Pin.OUT)

Mode0.value(0)
Mode1.value(0)

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
tft.init()
def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB-COMPONENTS", 0,0)
    tft.fill_rect(0, 40, 210,10, st7789.RED)
    
    tft.text(font,"RANGEPI", 0,55,st7789.YELLOW)
    tft.text(font,"MESSENGER", 0,100,st7789.YELLOW)
    tft.fill_rect(0, 90, 210, 10, st7789.BLUE)
    time.sleep(1)
    tft.fill(0) #clear screen
    tft.text(font,"MESSENGER", 5,10,st7789.WHITE)
    tft.fill_rect(0, 50, 210,10, st7789.RED)

        
info()

a=4
while True:
    print("For transmitter type = 1")
    print("For Receiver type = 2")
    choice = int(input("Enter choice = "))
    if choice == 1:
        n = input("Enter The Message = ")
        lora.write(n)#send data
        tft.text(font,n, 5,60,st7789.YELLOW)
        utime.sleep(0.5)#wait 200ms
        tft.text(font,n, 5,60,st7789.BLACK)
    if choice == 2:
        while a>0:
            data_Read = lora.readline()#read data comming from other pico lora expansion
            if data_Read is not None:
                
                    tft.text(font,data_Read, 5,80,st7789.YELLOW)
                    print(data_Read)
                    time.sleep(2)
                    tft.text(font,data_Read, 5,80,st7789.BLACK)

                    
            utime.sleep(2)#wait for 200ms
            a=a-1
    a=10
        
    
    
 






