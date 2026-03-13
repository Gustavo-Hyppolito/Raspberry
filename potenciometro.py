from machine import Pin, PWM, ADC
from utime import sleep

pot = ADC(26)          
led = PWM(Pin(15))     
led.freq(1000)
led.duty_u16(0)

while True:
    val = pot.read_u16()         
    porc_val = int((val * 100) / 65535)
    print(f"Valor porcentagem: {porc_val}%")
      
    def mapear (leitura_pot, in_min, in_max, out_min, out_max):
        return int ((leitura_pot - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    val_mapeado = mapear(val, 0, 65535, 0, 255)
    print(f"Valor mapeado: ", val_mapeado)
    
    led.duty_u16(val)
    sleep(0.3)
                
    