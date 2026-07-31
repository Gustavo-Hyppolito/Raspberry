from machine import I2C, Pin, ADC
from utime import sleep, sleep_ms
from pico_i2c_lcd import I2cLcd
from dht import DHT22
import math
from picozero import Speaker

# --- CONFIGURAÇÃO DO DISPLAY LCD ---
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.clear()
lcd.putstr("SecureFlow v1.0")
sleep(1.5)
lcd.clear()

# --- HARDWARE CONFIGURADO CORRETAMENTE ---
sensor = DHT22(Pin(15))     # CORRIGIDO: DHT22 está fisicamente no GP15
sensor_gas = ADC(26)        # MQ-2 no GP26

# LEDS
led_verde = Pin(12, Pin.OUT)
led_amarelo = Pin(8, Pin.OUT)
led_vermelho = Pin(4, Pin.OUT)

# BUZZER
speaker = Speaker(14)       # CORRIGIDO: Movido para o GP14 para liberar o GP15

# BOTÃO COM PULL_DOWN ATIVADO
botao = Pin(18, Pin.IN, Pin.PULL_DOWN) # CORRIGIDO: Adicionado PULL_DOWN

# Variável de controle para o LCD não travar
estado_anterior = ""

print("--- SISTEMA MONITOR CONECTADO ---")

while True:
    # 1. Leitura dos sensores com tratamento de erro
    try:
        sensor.measure()
        temp = sensor.temperature()
        umid = sensor.humidity()
    except OSError:
        temp, umid = 24.0, 50.0 # Valores padrão caso falhe

    leitura = sensor_gas.read_u16()
    estado_atual_botao = botao.value()

    print("Temp: {}C | Gas: {} | Botao: {}".format(temp, leitura, estado_atual_botao))

    # 2. Definição do Estado Atual do Sistema
    if estado_atual_botao == 1:
        estado_atual = "MANUAL"
    elif temp >= 50 or leitura >= 55000:
        estado_atual = "EMERGENCIA"
    elif temp >= 35 or leitura >= 45000:
        estado_atual = "ATENCAO"
    else:
        estado_atual = "SEGURO"

    # 3. Atualização Inteligente do LCD (Evita tela apagada/piscando)
    if estado_atual != estado_anterior:
        lcd.clear()
        sleep_ms(20)
        if estado_atual == "MANUAL":
            lcd.move_to(0, 0)
            lcd.putstr("ALARME MANUAL")
            lcd.move_to(0, 1)
            lcd.putstr("EVACUAR AMBIENTE")
        elif estado_atual == "SEGURO":
            lcd.move_to(0, 0)
            lcd.putstr("AMBIENTE")
            lcd.move_to(0, 1)
            lcd.putstr("SEGURO")
        elif estado_atual == "ATENCAO":
            lcd.move_to(0, 0)
            lcd.putstr("ATENCAO")
            lcd.move_to(0, 1)
            lcd.putstr("POSSIVEL RISCO")
        elif estado_atual == "EMERGENCIA":
            lcd.move_to(0, 0)
            lcd.putstr("EMERGENCIA!")
            lcd.move_to(0, 1)
            lcd.putstr("EVACUAR")
        estado_anterior = estado_atual

    # 4. Execução dos Atuadores (LEDs e Buzzer)
    if estado_atual == "MANUAL":
        led_verde.off()
        led_amarelo.off()
        led_vermelho.on()
        speaker.on()
        sleep(0.5)
        led_vermelho.off()
        speaker.off()
        sleep(0.5)

    elif estado_atual == "SEGURO":
        led_verde.on()
        led_amarelo.off()
        led_vermelho.off()
        speaker.off()
        sleep(1)

    elif estado_atual == "ATENCAO":
        led_verde.off()
        led_amarelo.on()
        led_vermelho.off()
        speaker.off()
        sleep(1)

    elif estado_atual == "EMERGENCIA":
        led_verde.off()
        led_amarelo.off()
        # Efeito intermitente do alarme e luzes de evacuação
        led_vermelho.on()
        speaker.on()
        sleep(0.2)
        led_vermelho.off()
        speaker.off()
        sleep(0.2)