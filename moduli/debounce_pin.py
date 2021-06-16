from time import ticks_ms
from machine import Pin

class DebouncePin(Pin):
	"""
	Class used to simplify the debounce process using buttons with micropython.
	
	This class completely removes the necessity to use the base Pin class.
	You only need to specify the pin number to use and the mode *
	
	*MODE ARGUMENT
	mode='edge' ----> is used to return True only when the signal is on the negative edge (for example releasing a button)
	mode='level' ----> is used to return True when the signal is on the positive level (after debounce time)
		
		
		
	"""
	def __init__(self, pin: int, mode: str, pull: str = None, active_value: bool = False, debounce_time_ms: int = 100):
	
		if pull == 'up':
			pull = super().PULL_UP
		elif pull == 'down':
			pull = super().PULL_DOWN
		elif pull is not None:
			print('[WARNING] Selected pull mode for pin {p} is not valid, defaulting to None').format(pin)
			
		super().__init__(pin, Pin.IN, pull)
		self.edge_trg = True
		self.change_mode(mode)
		self.active = active_value
		self.deb_time = debounce_time_ms
		self.oldstate = False
		self.passed = 0
		self.active_time = 0
		
	def change_mode(self, mode: str):
	
		if mode == 'level':
			self.edge_trg = False
		elif mode == 'edge':
			self.edge_trg = True
		else: 
			self.edge_trg = True
			print('[WARNING] Selected trigger mode for pin {p} is not valid, defaulting to "edge"').format(pin)
			
	def value(self) -> bool:
		
		self.passed = ticks_ms() - self.active_time 
		
		if super().value() == self.active and not self.oldstate:
				self.oldstate = True
				self.active_time = ticks_ms()
		
		if self.edge_trg:	
			if super().value() != self.active and self.oldstate and self.passed > self.deb_time:
				self.oldstate = False
				return True
			
			return False
		else:
			if self.passed > self.deb_time:
				if super().value() == self.active and self.oldstate:
					return True
					
				self.oldstate = False	
			return False
