import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_11",GPIO.IN)  #Echo
GPIO.setup("P8_12",GPIO.OUT) #Trigger
GPIO.output("P8_12", GPIO.HIGH)

def distanceMeasurement(TRIG,ECHO):
    pulseStart = pulseEnd = 0
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulseStart = pulseEnd = time.time()
    while GPIO.input(ECHO) == 1:      
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    return distance

#main Loop
try:
    print "Starting Up...."
    while True:
        recoveredDistance = distanceMeasurement("P8_12","P8_11")
        print "Distance1: ",recoveredDistance,"cm"
        time.sleep(0.2)
except KeyboardInterrupt:
    print "Measurement stopped by user"
    GPIO.cleanup()
