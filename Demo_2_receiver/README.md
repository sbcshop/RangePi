# Demo 2 - Receiving Data

The code in this demo uses the same initialization that is described in the project_template directory.

## Sending a message (Without Buttons)

when using the LoRa chip to receive a message you would simply read it through UART. The chip can buffer up to 256 bytes of data so it can bank 256 characters before you start to lose data.


the following is code to a function that will wait until a message is received.

```python 

...

def receiveMessage():
    while True:
        data_read = lora.readline()
        if data_read is not None:
            return data_read
                
        utime.sleep(0.2)#wait for 200ms

... 

```

Using the function above we can then construct the main loop of the program that would continuously read for received data and then display it.

```python 

...

while True:
    msg = receiveMessage()
    
    tft.text(font, msg, 10, 60, st7789.YELLOW)
    utime.sleep(0.2)#wait 200ms
    tft.text(font, msg, 10, 60, st7789.BLACK)


```

the message will first yellow and then go black to distinguish between messages.

