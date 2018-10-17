# importing the module 
# example from: https://www.geeksforgeeks.org/tweet-using-python/
import tweepy 

# personal details 
consumer_key ="067x70cnWGAltFo8YUFIhrN6X"
consumer_secret ="7O9NTSm1oB7BH1hLLIe2pHFPuqm2KQmbDSUQo2yOWyn41p4jyh"
access_token ="1052610096327524355-0nGLxfYObTplXq5lx5gwS7eT8Kf1pQ"
access_token_secret ="NGmpho8ZVqOPFcYuGmHgA3VZgPCwIWuzCioTRvtS5UpoP"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

# update the status 
api.update_status(status ="Hello Everyone !") 

