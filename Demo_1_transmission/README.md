# Demo 1 - Transmission  

The code in this demo uses the same initialization that is described in the project_template directory.

## Sending a message (Without Buttons)

when using the LoRa chip to send a message you would simply write it to the chip through UART. 

the line ```python lora.write(message)``` can be used to send a message on the air with the chip and hence the main loop of the code.

```python 

...

test_msg = "HELLO WORLD"

while True:
    tft.text(font,test_msg, 10,60,st7789.BLACK)
    lora.write(test_msg)
    tft.text(font,test_msg, 10,60,st7789.YELLOW)
    utime.sleep(0.2)#wait 200ms

```

the code above first would send the text "HELLO WORLD" over the air every 200 milliseconds. before sending the message being sent would be black and then it would change to yellow upon writing the data on UART to the chip. 

## Sending Messages (With Buttons)

Because of the way the buttons where setup the value of ```python button.value()``` would be ```0``` when  the button is pressed so using this fact we can check if a button has been pressed. 

when using the LoRa chip to send a message you would simply write it to the chip through UART. 

the line ```python lora.write(message)``` can be used to send a message on the air with the chip and hence the main loop of the code.

```python 

...

while True:
    if button1.value() == 0:
        message = "Hello"
        lora.write(message)#send data

        tft.text(font,message, 10,100,st7789.YELLOW)
        utime.sleep(0.2)#wait 200ms
        tft.text(font,message, 10,100,st7789.BLACK)
        
    if button2.value() == 0:
        message = "World"
        lora.write(message)#send data

        tft.text(font,message, 10,100,st7789.YELLOW)
        utime.sleep(0.2)#wait 200ms
        tft.text(font,message, 10,100,st7789.BLACK)
```

The code above is the main loop of the main_with_buttons.py file. It will continuously check if a button has been pressed and if it has then it would send ethier ```python "Hello" ``` or ```python "World" ```
