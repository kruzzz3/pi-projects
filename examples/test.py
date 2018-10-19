import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
import time
import sys
sys.path.insert(0, '/home/pi/pi-projects/libs')

from led import Led

led = Led(4)

led.stopBlink()

#led.blink(0.1)

print "sfsdf"

led.blink(1)
time.sleep(4)
led.blink(0.1)
time.sleep(4)
led.blink(1)
led.off()


print "sfsdf"