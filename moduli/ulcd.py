from machine import Pin
from time import sleep_ms

class Lcd():

	def __init__(self, en: int, rs: int, d4: int, d5: int, d6: int, d7: int):
		self.en = Pin(en, Pin.OUT)
		self.rs = Pin(rs, Pin.OUT)
		self.d4 = Pin(d4, Pin.OUT)
		self.d5 = Pin(d5, Pin.OUT)
		self.d6 = Pin(d6, Pin.OUT)
		self.d7 = Pin(d7, Pin.OUT)
		
		self._setup()
		
		self.rs.value(1)
		self._send(0b01001000)
		
	def enable(self):
		sleep_ms(2)
		self.en.value(1)
		sleep_ms(2)
		self.en.value(0)
		
	def _send(self, data: int, send_4bits: bool = False):
	
		if not send_4bits:
			self.d7.value(data & 0b10000000 >> 7)
			self.d6.value(data & 0b01000000 >> 6)
			self.d5.value(data & 0b00100000 >> 5)
			self.d4.value(data & 0b00010000 >> 4)
			self.enable()
		
		self.d7.value(data & 0b00001000 >> 3)
		self.d6.value(data & 0b00000100 >> 2)
		self.d5.value(data & 0b00000010 >> 1)
		self.d4.value(data & 0b00000001 >> 0)
		self.enable()
		
		
	def _setup(self):
		
		self.rs.value(0)
		sleep_ms(150)
		for i in range(3):
			self._send(0b0011, send_4bits=True)
			sleep_ms(10)
		
		self._send(0b0010, send_4bits=True)
		self._send(0b00101000)
		self._send(0b00001000)
		self._send(0b00000001)
		sleep_ms(5)
		self._send(0b00000110)
		self._send(0b00001111)
		
		
		
			
		
		
			
		

