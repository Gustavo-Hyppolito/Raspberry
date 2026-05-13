# config.py — MODO A: Broker HiveMQ (nuvem)
# Aula 9: MQTT com Raspberry Pi Pico 2W | SENAI Ítalo Bologna
#
# ⚠️ Cada aluno muda:
#   CLIENT_ID  → pico_seunome  (ex: pico_joao)
#   TOPIC_PUB  → senai/seunome/dht22  (ex: senai/joao/dht22)

WIFI_SSID   = "WIFI_IOT"
WIFI_PASS   = "Ac1ce2ss5@IOT"

BROKER_IP   = "10.132.112.08"   # broker público na nuvem
BROKER_PORT = 1883

CLIENT_ID   = "Ghyppolito"        # ← coloque seu nome aqui
TOPIC_PUB   = "senai/Ghyppolito/hello" # ← coloque seu nome aqui