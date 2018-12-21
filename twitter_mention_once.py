#!/usr/bin/env python
#(c) Harshad Joshi, 2011
#firewalrus [AT] gmail DOT com

import sys
import tweepy
import time
import os
import random
a='none'

theLast = None
ri = 0
ri = random.randint(0,3)
def start():
        global theLast, ri,a
	if True:
                          os.system("python /home/pi/projects/the.narrative.machine.twitter/runNM.py &")
                          time.sleep(25.0)
                          if ri == 0:
                            os.system("aplay /home/pi/projects/the.narrative.machine.twitter/audio/1a.wav &")
                          if ri == 1:
                            os.system("aplay /home/pi/projects/the.narrative.machine.twitter/audio/2a.wav &")
                          if ri == 2:
                            os.system("aplay /home/pi/projects/the.narrative.machine.twitter/audio/3a.wav &")
                          if ri == 3:
                            os.system("aplay /home/pi/projects/the.narrative.machine.twitter/audio/4a.wav &")
                          time.sleep(10.0)
                          for xi in range(3):
                           if ri == 0:
                            os.system("aplay /home/pi/projects/the.narrative.machine.twitter/audio/1a.wav &")
                           if ri == 1:
                            os.system("aplay /home/pi/projects/the.narrative.machine.twitter/audio/2a.wav &")
                           if ri == 2:
                            os.system("aplay /home/pi/projects/the.narrative.machine.twitter/audio/3a.wav &")
                           if ri == 3:
                            os.system("aplay /home/pi/projects/the.narrative.machine.twitter/audio/4a.wav &")
                           time.sleep(10)
                          ri = ri+1
                          if ri > 3:
                            ri = 0
                          doExit = True
                     
	else:
            print "no play"		
start()

