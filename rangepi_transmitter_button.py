#Transmiter code
import utime
from machine import UART,SPI
from machine import Pin
import st7789
import time

import vga1_8x16 as font1
#import vga2_8x8 as font
import vga1_16x32 as font
import vga1_16x16 as font2

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)

Mode0 = machine.Pin(2, machine.Pin.OUT)
Mode1 = machine.Pin(3, machine.Pin.OUT)

Mode0.value(0)
Mode1.value(0)


button1 = Pin(13, Pin.IN, Pin.PULL_UP)
button2 = Pin(14, Pin.IN, Pin.PULL_UP)

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB-COMPONENTS", 0,0)
    tft.fill_rect(0, 40, 210,10, st7789.RED)
    
    tft.text(font,"RANGEPI", 0,55,st7789.YELLOW)
    tft.text(font,"TRANSMITTER", 0,100,st7789.YELLOW)
    tft.fill_rect(0, 90, 210, 10, st7789.BLUE)
    time.sleep(1)
    tft.fill(0) #clear screen
    tft.text(font,"SEND MESSAGE", 5,10,st7789.WHITE)
    tft.text(font,"BY PRESSING ", 5,40,st7789.WHITE)
    tft.text(font,"BUTTON", 5,70,st7789.WHITE)
        
info()

while True:
    if button1.value() == 0:
        n = "Hello\n"
        lora.write(n)#send data
        print("hello")
        tft.text(font,n, 10,100,st7789.YELLOW)
        utime.sleep(0.2)#wait 200ms
        tft.text(font,n, 10,100,st7789.BLACK)
        
    if button2.value() == 0:
        n = "World\n"
        lora.write(n)#send data
        print("world")
        tft.text(font,n, 10,100,st7789.YELLOW)
        utime.sleep(0.2)#wait 200ms
        tft.text(font,n, 10,100,st7789.BLACK)





