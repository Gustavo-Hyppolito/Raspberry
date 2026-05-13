# wifi_connect.py — função de conexão WiFi

import network
import time

def conectar_wifi(ssid, senha):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Conectando em {ssid}...")
        wlan.connect(ssid, senha)
        
        # Aguarda conexão com timeout de 15 segundos
        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
            print(".", end="")
    
    if wlan.isconnected():
        print(f"\nConectado! IP: {wlan.ifconfig()[0]}")
        return True
    else:
        print("\nFalha na conexão WiFi")        return False