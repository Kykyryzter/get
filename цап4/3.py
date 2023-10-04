import RPi.GPIO as gpio
import sys
from time import sleep
gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.OUT)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)
pwm=gpio.PWM(24, 1000)
pwm.start(0)

try:
    while True:
            DutyCicle=int(input())
            pwm.ChangeDutyCycle(DutyCicle)
            print("{:.2f}".format(DutyCicle*3.3/100))
finally:
    gpio.output(24, 0)
    gpio.output(dac, 0)
    gpio.cleanup()   