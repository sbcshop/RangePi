# Example Project Template

This is a example template starter to a project importing all necessary items and then initializing all objects 

Bellow is a description of why certain more notable things where done

## LoRa

the following libraries must be imported in order to communicate with the LoRa Chip

```python 
from machine import UART
from machine import Pin
```

the following could be used to initialize communication with the LoRa chip

```python 
# Initialization for the LoRa mode pins
Mode0 = machine.Pin(2, machine.Pin.OUT)
Mode1 = machine.Pin(3, machine.Pin.OUT)

# Set the chip into transmission mode
Mode0.value(1)
Mode1.value(0)

...

# Initialization of UART for communication with the LoRa chip 
lora = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
```

## 1.14" LCD Screen

the following libraries are needed in order to communicate with the LCD Screen the font libraries are used to allow text of different sizes to be displayed

```python
# Import for usage of 1.14" LCD
from mcahine import SPI
import st7789

# Import fonts for the LCD Screen
import vga2_8x8 as font
import vga1_8x16 as font1
import vga1_16x16 as font2
import vga1_16x32 as font3
```

in order to initialize the screen a SPI link must be initialized and then off the back of that a tft object can be created that we will then use to utilize the screen. 

```python 

...

# Initialization for the LCD Screen
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi, 135, 240, reset=Pin(12, Pin.OUT), cs=Pin(
    9, Pin.OUT), dc=Pin(8, Pin.OUT), backlight=Pin(13, Pin.OUT), rotation=1)

...

```

and then displaying initial information.

```python 

...

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

...

```

to learn more about how the screen works here is a link to the documentation of our 1.14" tft LCD screen breakout board

https://learn.sb-components.co.uk/1.14-lcd-breakout 

## Buttons

the buttons in the code are setup as basic pull up configuration. The buttons are connected to Pins 13,14 on the RPI204

```python
...

from machine import PIN 

...

# Initialization for the onboard buttons

button1 = Pin(13, Pin.IN, Pin.PULL_UP)
button2 = Pin(14, Pin.IN, Pin.PULL_UP)

```

