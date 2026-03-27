from machine import Pin, PWM, ADC
from utime import sleep

pot = ADC(26)          

led_r = PWM(Pin(17))
led_b = PWM(Pin(18))
led_g = PWM(Pin(15))  

led_r.freq(1000)
led_b.freq(1000)
led_g.freq(1000)

led_r.duty_u16(0)
led_b.duty_u16(0)
led_g.duty_u16(0)

while True:
    
    val = pot.read_u16()         

    porc_val = int((val * 100) / 65535)
    print(f"Valor porcentagem: {porc_val}%")

    # balanço de cores
    azul = val
    vermelho = 65535 - val

    led_b.duty_u16(azul)
    led_r.duty_u16(vermelho)
    led_g.duty_u16(0)

    print("Vermelho:", vermelho, "Azul:", azul)

    sleep(0.05)