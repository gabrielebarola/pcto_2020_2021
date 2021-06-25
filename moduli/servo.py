from machine import Pin, PWM

class Servo():
	def __init__(self, pin_number):
		self.pin = PWM(Pin(pin_number))
		
		self.pin.freq(50)
		self.move(0)
	
	def _get_duty(self, angle):
		period = (angle/180)+1
		dc = period/20 
		duty = int(dc*1023)
		return duty
		
	def move(self, angle):
		if angle < 0:
			print('[WARNING] Value under minumum angle, moving to 0')	
			angle = 0
		elif angle > 180:
			print('[WARNING] Value over maximum angle, moving to 180')	
			angle = 180
			
		duty = self._get_duty(angle)
		self.angle = angle
		self.pin.duty(duty)
