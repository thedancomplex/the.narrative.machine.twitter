#!/usr/bin/env python
#(c) Harshad Joshi, 2011
#firewalrus [AT] gmail DOT com

import sys
import tweepy
import time
import os

CONSUMER_KEY = '067x70cnWGAltFo8YUFIhrN6X'
CONSUMER_SECRET = '7O9NTSm1oB7BH1hLLIe2pHFPuqm2KQmbDSUQo2yOWyn41p4jyh'

ACCESS_KEY = '1052610096327524355-0nGLxfYObTplXq5lx5gwS7eT8Kf1pQ'
ACCESS_SECRET = 'NGmpho8ZVqOPFcYuGmHgA3VZgPCwIWuzCioTRvtS5UpoP'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


theLast = None
ri = 0
def start():

        global theLast, ri
        a = 'mentions'
	if (a == 'mentions'):
		mymentions = api.mentions_timeline()
                doExit = False 		
		for tweet in mymentions:
                     if (not doExit):   
			d = str(unicode(tweet.text).encode("utf-8"))+" >>  "+str(unicode(tweet.user.screen_name).encode("utf-8"))
                        ##### d is the most recent received test #####
                        if(theLast != d):
			  print d
                          theLast = d
                          os.system("python runNM.py &")
                          time.sleep(5.0)
                          if ri == 0:
                            os.system("aplay audio/1a.wav")
                          if ri == 1:
                            os.system("aplay audio/2a.wav")
                          if ri == 2:
                            os.system("aplay audio/3a.wav")
                          if ri == 3:
                            os.system("aplay audio/4a.wav")
                          ri = ri+1
                          if ri > 3:
                            ri = 0
                        doExit = True
                     
	else:
		if (a.lower() == 'home'):
			home = api.home_timeline()
			for i in home:
				print i.text + " >> " + i.user.screen_name		
		else:
			api.update_status(a)
	
while(1):
	start()
        time.sleep(30)
