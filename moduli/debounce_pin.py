from time import ticks_ms

class DebouncePin():
	"""
	Class used to simplify the debounce process using buttons with micropython.
	
	The pin_object argument represents a Pin() from the machine module:
	
		from machine import Pin
		pin = Pin(2, Pin.IN)
		deb_pin = DebouncePin(pin, False, 200)
		
		
	To retrieve the value of the pin with debounce use the value() function in your loop:
	
		while True:
			value = deb_pin.value()
		
		
	"""
	def __init__(self, pin_object, active_value: bool, debounce_time_ms: int):
		self.pin = pin_object
		self.active = active_value
		self.deb_time = debounce_time_ms
		self.oldstate = False
		self.passed = 0
		self.active_time = 0
		
	def value(self) -> bool:
		self.passed = ticks_ms() - self.active_time 
		if self.pin.value() == self.active and not self.oldstate:
			self.oldstate = True
			self.active_time = ticks_ms()
			
		if self.pin.value() != self.active and self.oldstate and self.passed > self.deb_time:
			self.oldstate = False
			return True
			
		return False
