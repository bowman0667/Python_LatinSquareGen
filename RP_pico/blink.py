#%%

from machine import Pin
import time
import utime
led = Pin(25, Pin.OUT)


while True:
    led.toggle()
    time.sleep_ms(100)