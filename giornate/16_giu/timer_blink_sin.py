"""
ESEMPIO CHE AUMENTA E DIMINUISCE LA LUMINOSITÀ DI UN LED
UTILIZZANDO PWM E TIMER, CON ANDAMENTO SINUSOIDALE
"""

from machine import Pin, Timer, PWM
from time import ticks_ms
from math import sin

dt = 0
angle = 0
led = PWM(Pin(2, Pin.OUT), duty=dt)

def change_pwm(t):
	global dt
	global angle
	
	angle += 0.1
	if angle > 360: # per non aumentare eccessivamente la variabile
		angle = 0
		
	dt = int((sin(angle) + 1) * 511) #non 512 perchè porterebbe al valore 1024 non ammesso dal pwm
	
	print(dt)
	led.duty(dt)
		
timer = Timer(1) 

timer.init(period=50, mode=Timer.PERIODIC, callback=change_pwm)

