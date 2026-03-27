from machine import Pin, PWM
from utime import sleep


botao_1 = Pin(16, Pin.IN, Pin.PULL_DOWN)  
botao_2 = Pin(14, Pin.IN, Pin.PULL_DOWN)  

led = PWM(Pin(17))
led.freq(1000)

brilho = 0

passo = 500

while True:
    
    if botao_1.value() == 1:
        brilho += passo
        if brilho > 65535:
            brilho = 65535

    if botao_2.value() == 1:
        brilho -= passo
        if brilho < 0:
            brilho = 0

    led.duty_u16(brilho)

    print("Brilho:", brilho)

    sleep(0.01)