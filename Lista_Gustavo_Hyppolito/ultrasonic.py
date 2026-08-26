from machine import Pin
from utime import sleep, ticks_us, ticks_diff

# Configurações de pinos
trig = Pin(14, Pin.OUT)  # Pino de disparo do sensor
echo = Pin(17, Pin.IN)   # Pino de recepção do sensor

while True:
    # Garante que o TRIG está em nível baixo
    trig.low()
    sleep(0.002)  # Aguarda 2ms para estabilizar
    
    # Envia um pulso de 10us
    trig.high()
    sleep(0.00001)
    trig.low()

    # Espera o início do pulso no ECHO
    while echo.value() == 0:
        start = ticks_us()

    # Espera o fim do pulso no ECHO
    while echo.value() == 1:
        end = ticks_us()

    # Calcula a duração do pulso
    # duracao → é o tempo (em microssegundos) que o pulso ultrassônico demorou para ir até o objeto e voltar.
    duracao = ticks_diff(end, start)

    # Calcula a distância em centímetros
    #0.0343 → é a velocidade do som em centímetros por microssegundo.
    distancia = (duracao * 0.0343) / 2

    """
    343 metros/segundo = 34.300 centímetros/segundo
    1 segundo = 1.000.000 microssegundos
    34300 ÷1.000.000 = 0,0343 centímetros por microssegundo
    """

    print(f"Distância: {distancia:.2f} cm")
    
    sleep(1)  # Aguarda 1 segundo antes da próxima leitura