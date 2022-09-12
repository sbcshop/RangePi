# IMPORTING LIBRARIES

from machine import Pin
import utime
import time

# Imports for communication with LoRa Chip
from machine import UART, SPI
from machine import Pin

# Import for usage of 1.14" LCD
import st7789

# Import fonts for the LCD Screen
import vga2_8x8 as font
import vga1_8x16 as font1
import vga1_16x16 as font2
import vga1_16x32 as font3

# INITIALIZATION

# Initialization for the LCD Screen
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi, 135, 240, reset=Pin(12, Pin.OUT), cs=Pin(
    9, Pin.OUT), dc=Pin(8, Pin.OUT), backlight=Pin(13, Pin.OUT), rotation=1)

# Initialization for the LoRa mode pins
Mode0 = machine.Pin(2, machine.Pin.OUT)
Mode1 = machine.Pin(3, machine.Pin.OUT)

Mode0.value(1)
Mode1.value(0)

# Initialization for the onboard buttons

button1 = Pin(13, Pin.IN, Pin.PULL_UP)
button2 = Pin(14, Pin.IN, Pin.PULL_UP)

# Initialization of UART for communication with the LoRa chip 

lora = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# UTILITY FUNCTIONS

# This function will initiate the LCD screen
def show_info():
    tft.init()
    utime.sleep(0.2)

    tft.text(font3, "SB-COMPONENTS", 0, 0)
    tft.fill_rect(0, 40, 210, 10, st7789.RED)
    tft.text(font3, "RANGEPI", 0, 55, st7789.YELLOW)
    tft.fill_rect(0, 90, 210, 10, st7789.BLUE)
    time.sleep(1)

    tft.fill(0)
    tft.text(font3, "TRANSMISSION", 5, 10, st7789.WHITE)
    tft.text(font3, "MODE", 80, 60, st7789.RED)

def receiveMessage():
    while True:
        data_read = lora.readline()
        if data_read is not None:
            return data_read
                
        utime.sleep(0.2)#wait for 200ms

# MAIN 

show_info()

while True:
    msg = receiveMessage()
    
    tft.text(font, msg, 10, 60, st7789.YELLOW)
    utime.sleep(0.2)#wait 200ms
    tft.text(font, msg, 10, 60, st7789.BLACK)

            
