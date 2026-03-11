from machine import Pin  # Importa a biblioteca para controlar os pinos da placa
from utime import sleep  # Importa a função de pausa (tempo)

# --- Configurações de Hardware ---
# Define o pino 2 como entrada. 
# Dica: Adicione Pin.PULL_DOWN se o seu botão não tiver resistor externo.
botao = Pin(2, Pin.IN)  

# Define o pino 3 como saída (onde o LED está conectado)
led = Pin(3, Pin.OUT)

# --- Variáveis de Controle de Estado ---
estado_led = False         # Armazena se o LED deve estar Ligado (True) ou Desligado (False)
ultimo_estado_botao = 0    # Guarda o valor da leitura anterior para detectar o clique

while True:
    # 1. Lê o estado atual do botão (0 para solto, 1 para pressionado)
    estado_atual_botao = botao.value()
    
    # 2. Lógica de Detecção de Borda de Subida:
    # Só entra no IF se o botão for 1 AGORA e era 0 na VOLTA ANTERIOR.
    if estado_atual_botao == 1 and ultimo_estado_botao == 0:
        
        # Inverte o valor booleano (se era False vira True e vice-versa)
        estado_led = not estado_led
        
        # Aplica o novo estado ao pino físico do LED
        led.value(estado_led)
        
        # Debounce: Pequena pausa para ignorar ruídos mecânicos do contato do botão
        sleep(0.2)

    # 3. Atualiza a memória: o estado "atual" vira o "último" para a próxima repetição
    ultimo_estado_botao = estado_atual_botao
    
    # Pequena pausa global para evitar que o processador rode a 100% sem necessidade
    sleep(0.01)