import RPi.GPIO as GPIO
import time

class Pin:
	# mode constants
	NONE = GPIO.UNKNOWN
	OUT = GPIO.OUT
	IN = GPIO.IN
	PWM = GPIO.HARD_PWM

	# value constants
	ON = GPIO.HIGH
	OFF = GPIO.LOW

	# pull up down constants
	PUD_OFF = GPIO.PUD_OFF
	UP = GPIO.PUD_UP
	DOWN = GPIO.PUD_DOWN

	# event constants
	RISE = GPIO.RISING
	FALL = GPIO.FALLING
	BOTH = GPIO.BOTH

	pin = None
	pwm = None

	def __init__(self, pin):
		if self.pin != None : self.close()
		self.pin = pin
		GPIO.setmode(GPIO.BCM)

	def output(self, value=PUD_OFF):
		self.close()
		GPIO.setup(self.pin, OUT, pull_up_down=value)
		return self

	def input(self, value=PUD_OFF):
		self.close()
		GPIO.setup(self.pin, IN, pull_up_down=value)
		return self

	def on(self):
		GPIO.output(self.pin, ON)
		return self

	def off(self):
		GPIO.output(self.pin, OFF)
		return self

	def read(self):
		return GPIO.input(self.pin)

	def pwm_init(self, freq, value=0):
		self.close()
		self.pwm = GPIO.PWM(self.pin, freq)
		self.pwm.start(value)
		return self

	def pwm(self, value):
		self.pwm.ChangeDutyCycle(value)
		return self

	def pwm_stop(self):
		self.pwm.stop()
		self.close()
		return self

	def wait_event(self, event, wait=0):
		GPIO.wait_for_edge(self.pin, event, timeout=wait)
		return self

	def add_event(self, event, function=None, wait=0):
		GPIO.add_event_detect(self.pin, event, callback=function, bouncetime=wait)
		return self

	def set_callback(self, function):
		GPIO.add_event_callback(self.pin, function)
		return self

	def event_detected(self):
		return GPIO.event_detected(self.pin)

	def remove_event(self):
		GPIO.remove_event_detect(self.pin)
		return self

	def delay(value):
		time.sleep(value / 1000)

	def close(self):
		GPIO.cleanup(self.pin)

def set_warnings(value):
		if value == self.ON:
			GPIO.setwarnings(True)
		elif value == self.OFF:
			GPIO.setwarnings(False)
		elif value:
			GPIO.setwarnings(True)
		elif not value:
			GPIO.setwarnings(False)
		return self

def delay(value):
	time.sleep(value / 1000)

def reset():
	GPIO.cleanup()
