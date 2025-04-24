import time
import math
import pigpio
import RPi.GPIO as GPIO

STEP_PIN=16
DIR_PIN=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN,GPIO.OUT)
GPIO.setup(DIR_PIN,GPIO.OUT)

def stepper_run(direction,speed_delay):
    GPIO.output(DIR_PIN,direction)
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(speed_delay)
    GPIO.output(STEP_PIN, GPIO.LOW)   
    time.sleep(speed_delay)

def delay_time(w):  
    if w == 0:
        return 0
    else:
        return(math.pi/(100*abs(w))) 
    
CH_1=22
CH_2=23
CH_3=27
pi = pigpio.pi()
last_tick={'ch_1:0','ch_2:0','ch_3:0'}

def normalize(x):
    x = (x-1500)/500
    return x

pwm_x=1500
pwm_y=1500
pwm_w=1500

def rc_callback(gpio,level,tick):
    global pwm_x,pwm_y,pwm_w
    if level == 1:
        last_tick[gpio] = tick
    elif level==0 and gpio in last_tick:
        width = pigpio.tickDiff(last_tick[gpio],tick)
    if gpio == CH_1:
        pwm_x=width
    elif gpio == CH_2:
        pwm_y=width
    elif gpio == CH_3:
        pwm_w=width

pi.set_mode(CH_1,pigpio.INPUT)
pi.set_mode(CH_2,pigpio.INPUT)
pi.set_mode(CH_3,pigpio.INPUT)
pi.callback(CH_1,pigpio.EITHER_EDGE, rc_callback)
pi.callback(CH_2,pigpio.EITHER_EDGE, rc_callback)
pi.callback(CH_3,pigpio.EITHER_EDGE, rc_callback)

while True:
    x=normalize(pwm_x)
    y=normalize(pwm_y)
    w=normalize(pwm_w)
    Vx=14*x
    Vy=14*y
    W=1.5*w
    w3=((W*15)-(Vx/2)+(Vy*(math.sqrt(3))/2))/2.5
    t=delay_time(w3)

    if t==0:
        True
    elif w3>0:
        stepper_run(direction=1,speed_delay=t)
    elif w3<0:
        stepper_run(direction=0,speed_delay=t)
    
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
    pi.stop()