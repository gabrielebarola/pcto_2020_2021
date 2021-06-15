from machine import Pin, PWM
from time import sleep_ms, ticks_ms
from debounce_pin import DebouncePin
			
			
dt = 512

up = DebouncePin(
	Pin(12, Pin.IN, Pin.PULL_UP),
	active_value=False,
	debounce_time_ms=200
	)
	
down = DebouncePin(
	Pin(13, Pin.IN, Pin.PULL_UP),
	active_value=False,
	debounce_time_ms=200
	)
	
led = PWM(
	Pin(2, Pin.OUT),
	duty=512
	)
	
while True:
	
	if up.update():
		dt += 100
		print('up')
	if down.update():
		print('down')
		dt -= 100
		
	if dt > 1023:
		dt = 1023
	elif dt < 0:
		dt = 0
		
	led.duty(dt)	
	sleep_ms(10)
