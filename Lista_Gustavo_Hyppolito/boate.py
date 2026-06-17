
# from machine import I2C, Pin, ADC
# from utime import sleep
# from pico_i2c_lcd import I2cLcd
# from dht import DHT22
# import math 
# from picozero import Speaker

# # LCD
# i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# I2C_ADDR = i2c.scan()[0]

# lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# lcd.putstr("Testando o LCD")
# sleep(2)
# lcd.clear()


# #SENSOR DE UMIDADE
# sensor = DHT22(Pin(15))
#  sensor.measure()  # Solicita ao sensor que faça a medição de temperatura e umidade
#     temp = sensor.temperature()  # Lê a temperatura medida
#     umid = sensor.humidity()  # Lê a umidade medida

#     if temp != None and umid != None:
#         print("Temperatura: {}°C".format(temp))  # Exibe a temperatura no console serial
#         #print(f"Temperatura: {temp} }°C)
#         print("Umidade: {}%".format(umid))  # Exibe a umidade no console serial
#     else:
#         print("Falha na leitura dos dados.")  # Caso algo anormal aconteça (por segurança)

#     sleep(2)  # Aguarda 2 segundos antes da próxima medição


# #SENSOR DE GÁS 
# sensor_gas = ADC(26)
# RL = 5000                         
# R0 = 10000                        

# m = -0.42                       
# b = 1.92 

# leitura = sensor_gas.read_u16()
#     print("Nível de gás/fumaça:", leitura)
# sleep(1)


# #LEDS
# led_verde = Pin(12, Pin.OUT)
# led_amarelo = Pin(8, Pin.OUT)
# led_vermelho = Pin(4, Pin.OUT)

# estado_led_verde = False  # Estado inicial do LED
# estado_led_amarelo = False  # Estado inicial do LED
# estado_led_vermelho = False  # Estado inicial do LED

# #BUZZER
# buzzer = Pin(15, Pin.OUT)

# speaker.on()     
#     sleep(1)         
#     speaker.off()    
#     sleep(1)

# #BUTTON PULL DOWN
# botao = Pin(18, Pin.IN)
# ultimo_estado_botao = 0  # Para detectar borda de subida
 
#  estado_atual_botao = botao.value()
#  if estado_atual_botao == 1 and ultimo_estado_botao == 0:
#         estado_led = not estado_led
#         led.value(estado_led)
#         sleep(0.2)  # Debounce simples

#     ultimo_estado_botao = estado_atual_botao
#     sleep(0.01)  # Loop mais estável

from machine import I2C, Pin, ADC
from utime import sleep
from pico_i2c_lcd import I2cLcd
from dht import DHT22
import math
from picozero import Speaker

# LCD
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.putstr("Testando o LCD")
sleep(2)
lcd.clear()

# SENSOR DE UMIDADE
sensor = DHT22(Pin(13))

# SENSOR DE GÁS
sensor_gas = ADC(26)

RL = 5000
R0 = 10000

m = -0.42
b = 1.92

# LEDS
led_verde = Pin(12, Pin.OUT)
led_amarelo = Pin(8, Pin.OUT)
led_vermelho = Pin(4, Pin.OUT)

# BUZZER
speaker = Speaker(15)

# BUTTON
botao = Pin(18, Pin.IN)
ultimo_estado_botao = 0

while True:

    # SENSOR DE TEMPERATURA/UMIDADE
    sensor.measure()
    temp = sensor.temperature()
    umid = sensor.humidity()

    if temp != None and umid != None:
        print("Temperatura: {}°C".format(temp))
        print("Umidade: {}%".format(umid))
    else:
        print("Falha na leitura dos dados.")

    # SENSOR DE GÁS
    leitura = sensor_gas.read_u16()
    print("Nível de gás/fumaça:", leitura)

    # BOTÃO MANUAL
    estado_atual_botao = botao.value()

    if estado_atual_botao == 1:

        led_verde.off()
        led_amarelo.off()

        led_vermelho.on()

        speaker.on()

        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("ALARME MANUAL")
        lcd.move_to(0, 1)
        lcd.putstr("EVACUAR!")

    # AMBIENTE SEGURO
    elif temp < 35 and leitura < 45000:

        led_verde.on()
        led_amarelo.off()
        led_vermelho.off()

        speaker.off()

        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("AMBIENTE")
        lcd.move_to(0, 1)
        lcd.putstr("SEGURO")

    # ATENÇÃO
    elif temp < 50 and leitura < 55000:

        led_verde.off()
        led_amarelo.on()
        led_vermelho.off()

        speaker.off()

        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("ATENCAO")
        lcd.move_to(0, 1)
        lcd.putstr("POSSIVEL RISCO")

    # EMERGÊNCIA
    else:

        led_verde.off()
        led_amarelo.off()

        led_vermelho.on()
        speaker.on()

        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("EMERGENCIA!")
        lcd.move_to(0, 1)
        lcd.putstr("EVACUAR")

        sleep(0.003)

        led_vermelho.off()
        speaker.off()

        sleep(0.003)

    sleep(1)