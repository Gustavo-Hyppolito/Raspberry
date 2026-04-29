from machine import Pin
from utime import sleep


sensor_presenca = Pin(15, Pin.IN)

while True:
    leitura_sensor = sensor_presenca.value()
    
    if(leitura_sensor == 0):
        print("Presença detectada")
        
    else:
        print("Nada detectado")
        
    sleep(0.5)