from machine import Pin, ADC, PWM
from utime import sleep

ledG= Pin(16, Pin.OUT)
ledY = Pin(17, Pin.OUT)
ledR = Pin(18, Pin.OUT)

while True:
    ledG.value(1)
    ledY.value(0)
    ledR.value(0)
    sleep(1)
    
    ledG.value(0)
    ledY.value(1)
    ledR.value(0)
    sleep(1)
    
    ledG.value(0)
    ledY.value(0)
    ledR.value(1)
    sleep(1)
    
     