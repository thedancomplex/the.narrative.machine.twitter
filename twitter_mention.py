#!/usr/bin/env python
#(c) Harshad Joshi, 2011
#firewalrus [AT] gmail DOT com

import sys
import tweepy
import time

CONSUMER_KEY = '067x70cnWGAltFo8YUFIhrN6X'
CONSUMER_SECRET = '7O9NTSm1oB7BH1hLLIe2pHFPuqm2KQmbDSUQo2yOWyn41p4jyh'

ACCESS_KEY = '1052610096327524355-0nGLxfYObTplXq5lx5gwS7eT8Kf1pQ'
ACCESS_SECRET = 'NGmpho8ZVqOPFcYuGmHgA3VZgPCwIWuzCioTRvtS5UpoP'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


theLast = None

def start():
        global theLast
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
        time.sleep(1)
