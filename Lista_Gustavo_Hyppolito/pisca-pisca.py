from machine import Pin, ADC
from utime import sleep

led = Pin(14, Pin.OUT)
pot = ADC(26)

def mapear(valor, in_min, in_max, out_min, out_max):
    return (valor - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:

    val = pot.read_u16()  

    
    tempo = mapear(val, 0, 65535, 0.5, 3)

    print("Tempo de pisca:", tempo)

    led.value(1)
    sleep(tempo)

    led.value(0)
    sleep(tempo)  


                