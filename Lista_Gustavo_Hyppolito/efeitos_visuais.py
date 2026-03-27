from machine import Pin, PWM, ADC
from utime import sleep
red = PWM(Pin(13))
green = PWM(Pin(14))
blue = PWM(Pin(15))
# Declaração sem laço "for"
red.freq(1000)
green.freq(1000)
blue.freq(1000)
pot = ADC(26)
btn_cor = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_efeito = Pin(15, Pin.IN, Pin.PULL_DOWN)
modo_cor = 0 # 0=R, 1=G, 2=B
modo_efeito = 0 # 0=Fixo, 1=Pisca
estado_cor_ant = 0

estado_efeito_ant = 0
pisca_estado = False
while True:

est_cor = btn_cor.value()
est_ef = btn_efeito.value()
if est_cor == 1 and estado_cor_ant == 0:
modo_cor = (modo_cor + 1) % 3
if est_ef == 1 and estado_efeito_ant == 0:
modo_efeito = (modo_efeito + 1) % 2
estado_cor_ant = est_cor
estado_efeito_ant = est_ef

intensidade = pot.read_u16()
if modo_efeito == 1: 
pisca_estado = not pisca_estado
if pisca_estado == False:
intensidade = 0 
red.duty_u16(intensidade if modo_cor == 0 else 0)
green.duty_u16(intensidade if modo_cor == 1 else 0)
blue.duty_u16(intensidade if modo_cor == 2 else 0)

sleep(0.15)