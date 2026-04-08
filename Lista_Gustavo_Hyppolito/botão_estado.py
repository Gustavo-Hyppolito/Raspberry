from machine import Pin
from utime import sleep  

botao = Pin(2, Pin.IN
led = Pin(3, Pin.OUT)

estado_led = False         
ultimo_estado_botao = 0    

while True:

    estado_atual_botao = botao.value()
    

    if estado_atual_botao == 1 and ultimo_estado_botao == 0:
        

        estado_led = not estado_led
        
        led.value(estado_led)
        

        sleep(0.2)


    ultimo_estado_botao = estado_atual_botao
    

    sleep(0.01)