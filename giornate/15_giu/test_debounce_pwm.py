"""
SEMPLICE PROGRAMMA PER AUMENTARE E DIMINUIRE LA LUMINOSITÃ€ DI UN LED CON PWM,
UTILIZZANDO LA CLASSE DebouncePin scritta da noi
variazione edge triggered
"""

from machine import Pin, PWM
from time import sleep_ms
from debounce_pin import DebouncePin
			
			
dt = 512

up = DebouncePin(12, 'edge', pull='up')
	
down = DebouncePin(13, 'edge', pull='up')
	
led = PWM(Pin(2, Pin.OUT), duty=dt)
	
while True:
	
	if up.value():
		dt += 100
		print('up')
	if down.value():
		print('down')
		dt -= 100
		
	if dt > 1023:
		dt = 1023
	elif dt < 0:
		dt = 0
		
	led.duty(dt)	
	sleep_ms(10)
