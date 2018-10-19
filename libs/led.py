import RPi.GPIO as GPIO
import time
import multiprocessing

'''
Wiring:
GND -> LED-Short-End -> LED -> LED-Long-End -> Resistor -> GPIO-Pin
'''

class Led:

  def __init__(self, gpio_pin):
    if gpio_pin <= 0 or gpio_pin > 27:
      raise ValueError('Error: gpio pin should be 0-27')

    self.gpio_pin = gpio_pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin, GPIO.OUT)
    self.isBlinking = 0
    self.off()
    self.processBlink = None
  

  def on(self):
    self.status = 1
    self.stopBlink()
    GPIO.output(self.gpio_pin, self.status)


  def off(self):
    self.status = 0
    self.stopBlink()
    GPIO.output(self.gpio_pin, self.status)


  def toggle(self):
    self.stopBlink()
    if self.status == 0:
      self.on()
    else:
      self.off()


  def __blink(self):
    while True:
      self.toggle()
      time.sleep(self.delay)


  def blink(self, delay):
    if delay <= 0:
      raise ValueError('Error: delay must be greater then 0')

    self.stopBlink()
    
    self.delay = delay
    self.isBlinking = 1
    
    self.processBlink = multiprocessing.Process(target = self.__blink)
    self.processBlink.start()


  def stopBlink(self):
    self.isBlinking = 0
    try:
      self.processBlink.terminate()
    except: 
      pass


  def isOn(self):
    return self.status == 1


  def isBlinking(self):
    return self.isBlinking == 1








