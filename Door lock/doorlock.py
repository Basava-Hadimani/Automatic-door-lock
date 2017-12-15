import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pins=[3,5,18,19]
for p in pins:
        GPIO.setup(p,GPIO.OUT)
        GPIO.output(p,0)
GPIO.setup(15,GPIO.IN)
GPIO.setup(13,GPIO.OUT)
seq=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
seq1=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
while True:
    if (GPIO.input(15)==1):
        GPIO.output(13,True)
        time.sleep(1)
        print('object is  detected')
        for i in range (512):
            for fullstep in range(4):
                for p in range(4):
                    GPIO.output(pins[p],seq[fullstep][p])
                    time.sleep(0.001)
    else:
        print('object is not detected')
        for i in range (512):
            for fullstep in range(4):
                for p in range(4):
                    GPIO.output(pins[p],seq1[fullstep][p])
                    time.sleep(0.001)
       
GPIO.cleanup()
            
