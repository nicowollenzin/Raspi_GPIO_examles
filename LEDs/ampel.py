import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup( 3,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
status = "rot" 

def init():
   GPIO.output(11,1) #rote Ampel
   GPIO.output(13,0)
   GPIO.output(15,0)

def set_gruen():
   time.sleep(0.5)
   GPIO.output(13,1)
   time.sleep(1)
   GPIO.output(11,0)
   GPIO.output(13,0)
   GPIO.output(15,1)

def set_rot():
   time.sleep(0.5)
   GPIO.output(15,0)
   GPIO.output(13,1)
   time.sleep(1)
   GPIO.output(13,0)
   GPIO.output(11,1)

try:
  init()
  while True:
     if(GPIO.input(3) == False):
        if(status == "rot"):
           print "Ampel Gruen"
           status = "gruen"
           set_gruen()
     else:
        if(status == "gruen"):
           print "Ampel Rot"
           status = "rot"
           set_rot()
except:      
  GPIO.cleanup()
