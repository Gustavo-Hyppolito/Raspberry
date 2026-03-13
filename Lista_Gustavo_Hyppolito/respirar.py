from machine import Pin, PWM
from utime import sleep

led = PWM(Pin(15))
led.duty_u16(0)
led.freq(1000)

while True:
    for duty in range(0, 65535, 255):
        led.duty_u16(duty)
        sleep(0.01)
        
    for duty in range(0, 65535, -255):
        led.duty_u16(duty)
        sleep(0.01)

