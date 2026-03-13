from machine import Pin, ADC, PWM
from utime import sleep


botao = Pin(16, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

while True:
    
    if botao.value() == 1:   
        led.value(1)        
    else:
        led.value(0)         

    sleep(0.01)