from machine import Pin, PWM
from utime import sleep

botao = Pin(16, Pin.IN, Pin.PULL_DOWN)

led = PWM(Pin(17))
led.freq(1000)

estado_led = False
ultimo_estado = 0

while True:
    
    estado_atual = botao.value()

    
    if estado_atual == 1 and ultimo_estado == 0:
        
        if estado_led == False:
            
            for i in range(0, 65535, 500):
                led.duty_u16(i)
                sleep(0.01)
            estado_led = True

        else:
            
            for i in range(65535, 0, -500):
                led.duty_u16(i)
                sleep(0.01)
            estado_led = False

        sleep(0.2)  

    ultimo_estado = estado_atual
    sleep(0.01)