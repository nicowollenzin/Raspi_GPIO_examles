########################################################################
# ampel.py - Trafficlight simulation
#
# Copyright (C) 2013 Nico Wollenzin
#
# This file is part of Raspi_GPIO_Examples.
#
# ampel.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# ampel.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
########################################################################

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
