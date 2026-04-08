from machine import Pin
from utime import sleep

ledG = Pin(15, Pin.OUT)
ledB = Pin(17, Pin.OUT)
ledR = Pin(18, Pin.OUT)

botao = Pin(16, Pin.IN, Pin.PULL_DOWN)

while True:
    valor = botao.value()

    if valor == 1:
        ledG.value(1)
        ledB.value(0)
        ledR.value(0)
        sleep(1)

        ledG.value(0)
        ledB.value(1)
        ledR.value(0)
        sleep(1)

        ledG.value(0)
        ledB.value(0)
        ledR.value(1)
        sleep(1)

        ledG.value(1)
        ledB.value(0)
        ledR.value(1)
        sleep(1)

        ledG.value(0)
        ledB.value(1)
        ledR.value(1)
        sleep(1)

        ledG.value(1)
        ledB.value(1)
        ledR.value(0)
        sleep(1)

        ledG.value(1)
        ledB.value(1)
        ledR.value(1)
        sleep(1)

    else:
        ledG.value(0)
        ledB.value(0)
        ledR.value(0)
        sleep(0.1)