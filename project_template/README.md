# Example Project Template

This is a example template starter to a project importing all necessary items and then initializing all objects 

Bellow is a description of why certain more notable things where done

## LoRa Specific Code

### Libraries 

the following libraries must be imported in order to communicate with the LoRa Chip

```python 
from machine import UART, SPI
from machine import Pin
```

### Initialization

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


