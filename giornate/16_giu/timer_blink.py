"""
ESEMPIO CHE AUMENTA E DIMINUISCE LA LUMINOSITÀ DI UN LED
UTILIZZANDO PWM E TIMER
"""

from machine import Pin, Timer, PWM

dt = 0
direction = True
led = PWM(Pin(2, Pin.OUT), duty=dt)

def change_pwm(t):
	global dt
	global direction
	
	if direction:
		dt += 20
	else:
		dt -= 20
		
	if dt > 1023:
		dt = 1023
		direction = False
	if dt < 0:
		dt = 0
		direction = True
		
	led.duty(dt)
		
timer = Timer(1) 

timer.init(period=100, mode=Timer.PERIODIC, callback=change_pwm)

