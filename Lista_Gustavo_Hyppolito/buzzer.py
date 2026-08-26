from utime import sleep
from machine import Pin, PWM

buzzer = PWM(Pin(16))
#buzzer = Pin(15, Pin.OUT)
buzzer.freq(1000)


while True:
    buzzer.duty_u16(62000)
    #buzzer.on()
    sleep(0.5)
    
   