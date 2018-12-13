#!/usr/bin/env python
#(c) Harshad Joshi, 2011
#firewalrus [AT] gmail DOT com

import sys
import tweepy

CONSUMER_KEY = '067x70cnWGAltFo8YUFIhrN6X'
CONSUMER_SECRET = '7O9NTSm1oB7BH1hLLIe2pHFPuqm2KQmbDSUQo2yOWyn41p4jyh'

ACCESS_KEY = '1052610096327524355-0nGLxfYObTplXq5lx5gwS7eT8Kf1pQ'
ACCESS_SECRET = 'NGmpho8ZVqOPFcYuGmHgA3VZgPCwIWuzCioTRvtS5UpoP'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

def start():
	a = raw_input ("\n Enter mentions or home or exit to quit :")

	if (a == "exit"):
		sys.exit(0)

	if (a == 'mentions'):
		mymentions = api.mentions_timeline() 		
		for tweet in mymentions:
			d = str(unicode(tweet.text).encode("utf-8"))+" >>  "+str(unicode(tweet.user.screen_name).encode("utf-8"))
			print d
	else:
		if (a.lower() == 'home'):
			home = api.home_timeline()
			for i in home:
				print i.text + " >> " + i.user.screen_name		
		else:
			api.update_status(a)
	
while(1):
	start()
