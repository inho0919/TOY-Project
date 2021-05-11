import NPi.GPIO as GPIO
import time

motor = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor, GPIO.OUT)

#def a(text, degree, t):
    #if '켜' in text or '키' in text:
    #    pwm = GPIO.PWM(motor, 50)
    #    pwm.start(3)
    #    time.sleep(t)
    #    pwm.ChangeDutyCycle(2)
    #    time.sleep(t)
    #    pwm.stop()
    #    GPIO.cleanup(motor)
    #elif '꺼' in text or '끄' in text:
    #    pwm = GPIO.PWM(motor, 50)
    #    pwm.start(3)
    #    time.sleep(t)
    #    pwm.ChangeDutyCycle(12)
    #    time.sleep(t)
    #    pwm.stop()
    #    GPIO.cleanup(motor)
def a(text):
    if('켜' in text or '키' in text):
        GPIO.output(motor,1)
    elif('끄' in text or '꺼' in text ):
        GPIO.output(motor,0)
    return True
#def a(text):
#    if('die Lampe an' in text or 'die lampe an' in text):
#        GPIO.output(rot,1)
#        GPIO.output(weiss,1)
#    elif('die Lampe aus' in text or 'die lampe aus' in text ):
#        GPIO.output(rot,0)
#        GPIO.output(weiss,0)
#    return True    