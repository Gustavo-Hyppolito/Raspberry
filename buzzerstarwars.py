from machine import Pin, PWM
import time

# Configura o pino do buzzer (GPIO 16)
buzzer_pin = 16
buzzer = PWM(Pin(buzzer_pin))

# Dicionário expandido com todas as frequências (em Hz) para a música inteira
notas = {
    'F4': 349,  'FS4': 370, 'G4': 392,  'GS4': 415,
    'A4': 440,  'AS4': 466, 'B4': 494,  'C5': 523,
    'CS5': 554, 'D5': 587,  'DS5': 622, 'E5': 659,
    'F5': 698,  'FS5': 740, 'G5': 784,  'GS5': 831,
    'A5': 880,  'PAUSA': 0
}

# Sequência completa da melodia: (Nota, Duração em ms)
melodia = [
    # --- Primeira Parte (O tema principal clássico) ---
    ('A4', 500), ('A4', 500), ('A4', 500), ('F4', 350), ('C5', 150),
    ('A4', 500), ('F4', 350), ('C5', 150), ('A4', 1000), ('PAUSA', 150),
    ('E5', 500), ('E5', 500), ('E5', 500), ('F5', 350), ('C5', 150),
    ('GS4', 500), ('F4', 350), ('C5', 150), ('A4', 1000), ('PAUSA', 150),
    
    # --- Segunda Parte (A escalada aguda) ---
    ('A5', 500), ('A4', 300), ('A4', 150), ('A5', 500), ('GS5', 325), ('G5', 175),
    ('FS5', 125), ('F5', 125), ('FS5', 250), ('PAUSA', 325), 
    ('AS4', 250), ('DS5', 500), ('D5', 325), ('CS5', 175),
    ('C5', 125), ('B4', 125), ('C5', 250), ('PAUSA', 350), 
    ('F4', 250), ('GS4', 500), ('F4', 350), ('A4', 125),
    ('C5', 500), ('A4', 350), ('C5', 125), ('E5', 1000), ('PAUSA', 150),
    
    # --- Terceira Parte (Repetição com final grave) ---
    ('A5', 500), ('A4', 300), ('A4', 150), ('A5', 500), ('GS5', 325), ('G5', 175),
    ('FS5', 125), ('F5', 125), ('FS5', 250), ('PAUSA', 325), 
    ('AS4', 250), ('DS5', 500), ('D5', 325), ('CS5', 175),
    ('C5', 125), ('B4', 125), ('C5', 250), ('PAUSA', 350), 
    ('F4', 250), ('GS4', 500), ('F4', 350), ('C5', 125),
    ('A4', 500), ('F4', 350), ('C5', 125), ('A4', 1000)
]

def tocar_nota(nota, duracao):
    """Toca a nota ou silencia se for PAUSA."""
    if nota == 'PAUSA':
        buzzer.duty_u16(0)
    else:
        frequencia = notas[nota]
        buzzer.freq(frequencia)
        buzzer.duty_u16(32768) # 50% de duty cycle para o som mais alto possível
    
    time.sleep_ms(duracao)
    
    # Micro-pausa de 50ms para as notas não grudarem umas nas outras
    buzzer.duty_u16(0)
    time.sleep_ms(50)

# Inicialização e Loop
print("Executando a Marcha Imperial Completa em loop! (Aperte Stop ou Ctrl+C para parar)")

try:
    while True:
        for nota, duracao in melodia:
            tocar_nota(nota, duracao)
            
        print("Recomeçando em 3 segundos...")
        time.sleep(3) # Pausa estendida para 3 segundos no fim da música longa
        
except KeyboardInterrupt:
    print("Música interrompida pelo usuário.")
    
finally:
    buzzer.duty_u16(0)
    buzzer.deinit()
    print("Buzzer desligado. Que a Força esteja com você.")