# main.py — MODO A: Broker HiveMQ (nuvem)
# Aula 9: MQTT com Raspberry Pi Pico 2W | SENAI Ítalo Bologna
#
# Fluxo: DHT22 → Pico 2W → WiFi → broker.hivemq.com → Navegador

from config import *
from wifi_connect import conectar_wifi
from umqtt.simple import MQTTClient
from dht import DHT22
from machine import Pin
from utime import sleep

# Sensor DHT22 — ajuste o pino se necessário
sensor = DHT22(Pin(15))

# Se o WiFi falhar, não tem sentido tentar MQTT
if not conectar_wifi(WIFI_SSID, WIFI_PASS):
    print("[MAIN] Sem WiFi. Reinicie o dispositivo.")

else:
    # Cria o cliente com as configurações do config.py
    cliente = MQTTClient(CLIENT_ID, BROKER_IP, port=BROKER_PORT)

    try:
        # Conecta ao broker e se identifica com o CLIENT_ID
        cliente.connect()
        print(f"[MQTT] Conectado em: {BROKER_IP}")
        print(f"[MQTT] Publicando em: {TOPIC_PUB}")

        while True:
            # measure() obriga o sensor a fazer uma nova leitura
            sensor.measure()
            temp = sensor.temperature()
            umid = sensor.humidity()

            # :.1f = 1 casa decimal | encode() = converte para bytes (exigido pelo MQTT)
            mensagem = f"temp:{temp:.1f},umid:{umid:.1f}"
            cliente.publish(TOPIC_PUB, mensagem.encode())
            print(f"[PUB] {mensagem}")

            sleep(3)  # DHT22 suporta no máximo 1 leitura/segundo

    except Exception as e:
        print(f"[ERRO] {e}")
        print("[MQTT] Verifique o broker e a conexão WiFi.")

    finally:
        # Executa sempre — garante desconexão limpa do broker
        try:
            cliente.disconnect()
            print("[MQTT] Desconectado.")
        except:
            pass