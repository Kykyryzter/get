import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec_bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc(troyka):
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        GPIO.output(dac, dec_bin(value))
        time.sleep(0.0008)

        if GPIO.input(comp) == 1:
            value -= 2**i
    return value


try:
    while True:
        print(dec_bin(adc(troyka)), "{:4f}".format(adc(troyka) / 256 * 3.3) + "B")

finally:
    GPIO.output(dac, [0] * 8)

GPIO.output(dac, [0] * 8)
GPIO.cleanup()