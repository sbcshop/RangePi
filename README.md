# RangePi
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img1.jpg" />
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img2.jpg" />

Range-Pi is a low cost portable “Plug and Play LoRaTM Dongle” based on Raspberry Pi RP2040 and  LoRaTM Modules, comes with an onboard 1.14" LCD that covers 433/868/915 MHz frequency band to enable data transmission up to 5 KM.

## Features
  * Two push button
    * **Button A** (Connect to GP13)
    * **Button B** (Connect to GP14)  
  * Two GP Pins ( for input/output devices )
    * **GP4**
    * **GP5**
  * UART Interface Direct to LORA Module

## Load Python File To RangePi And Install Thonny Python IDE
Use thonny python IDE for programming,link of the software is given below :

https://thonny.org/

### Steps to load python file to RangePi

Step 1 - Open thonny 
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img12.JPG" />

Step 2 - Select micropython and port in thonny for this go to run-> select interpreter
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img9.jpg" />
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img10.JPG" />

Step 3 - Save python file to RangePi
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img13.png" />
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img14.png" />
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img11.JPG" />

Step 4 - Run(execute) and stop file (script)
<img src= "https://github.com/sbcshop/RangePi/blob/main/images/img8.JPG" />

## Uploading the ST7789 Python Firmware (we already update in github)
 * The firmware includes frozen python font files and pre-compiled objects with the st7789 C driver for a variety of devices.
 * The driver's library is provided as a single firmware.uf2 file, which is accessible here:
    https://github.com/russhughes/st7789_mpy/tree/master/firmware/RP2
    
 * Holding down the RangePi BOTSEL button while dragging this file into the mounted RP2 folder will allow you to load it.

## code
### First you need to install firmware of 1.14 lcd screen to RangePi, for this press boot button then plug to laptop/desktop after that release the button, you see new        storage device. then drag and drop **firmware.uf2** file to RangePi

* Receiver
  * **rangepi_receiver.py** - Run this file if you make RangePi as receiver ( in all case receiver is same ) 
    <img src = "https://github.com/sbcshop/RangePi/blob/main/images/img6.JPG" />
 
* Transmitter  
  * **rangepi_transmitter.py** - Run this file if you make RangePi as transmitter 
    <img src = "https://github.com/sbcshop/RangePi/blob/main/images/img5.JPG" />
  
  * **user_input_transmitter.py** - Run this file if you make RangePi as transmitter or you can transmit using window applications like XCTU, Tera Term etc.
    <img src = "https://github.com/sbcshop/RangePi/blob/main/images/img3.JPG" />
    
  * **messenger.py** - Run this file if you want to talk through message like messenger(run the file in both rangepi)
    <img src = "https://github.com/sbcshop/RangePi/blob/main/images/img7.JPG" />
    
* **rangepi_configuration.py** - Rename this file as main.py and save this file inside RangePi and go to below video link to configure your RangePi board.
 
    https://www.youtube.com/watch?v=InQ0FwF4tLk&ab_channel=SBComponentsLtd


* **RangePi Getting started video**

   https://www.youtube.com/watch?v=ilqfkI1IL44&ab_channel=SBComponentsLtd
  


## Our Other LoRa Products

* GatePi 4Channel
* GatePi 8channel
* RangePi*
* LoRA HAT for RPi
* PICO LoRa Expansion

You will simply need to make one device to work as reciever and another one is as a transmitter. So that you can communicate to each other and this can be done with any of our LoRa products mentioned above. For working with our other products please follow the below link:

* GatePi 4Channel
https://github.com/sbcshop/GatePi-4CH

* GatePi 8channel
https://github.com/sbcshop/GatePi-8CH
* RangePi* (Itself)
* LoRA HAT for RPi
https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi
* PICO LoRa Expansion
https://github.com/sbcshop/PICO-LORA-EXPANSION


### Note: Every time you choose the different transmit device the transmit code of that device should be run in it and reciever code will always same(or depending upon what you want to control or recieve).

