"""
SEMPLICE PROGRAMMA PER AUMENTARE E DIMINUIRE LA LUMINOSITÀ DI UN LED CON PWM,
UTILIZZANDO LA CLASSE DebouncePin scritta da noi
variazione level triggered
"""

from debounce_pin import DebouncePin
from machine import Pin, PWM
from time import sleep_ms

dt = 512

up = DebouncePin(12, 'level', pull='up')
	
down = DebouncePin(13, 'level', pull='up')

led = PWM(Pin(2, Pin.OUT), duty=dt)

while True:

	if up.value():
		dt += 5
		print('up')
	elif down.value():
		print('down')
		dt -= 5
		
	if dt > 1023:
		dt = 1023
	elif dt < 0:
		dt = 0
		
	led.duty(dt)
	sleep_ms(10)
