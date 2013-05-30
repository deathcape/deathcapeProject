# -*- coding: utf-8 -*-
import sys
import os
import time
import cPickle
import twitter
from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

CONSUMER_KEY = 'rNpyePNusL8TEinRoLTQw'
CONSUMER_SECRET = 'HTXxYscwjjDCxJl3FJHgOpJO6oIJvRzpWH6yKncTo'
APP_NAME = 'deathcapeProject'

SCREEN_NAME = sys.argv[1]
friends_limit = 10000 

def oauth_login(app_name=APP_NAME,consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,token_file='out/twitter_oauth'):

	try:
		(oauth_token, oauth_token_secret) = read_token_file(token_file)
	except IOError, e:
		(oauth_token, oauth_token_secret) = oauth_dance('deathcape', consumer_key, consumer_secret)

		if not os.path.isdir('out'):
			os.mkdir('out')
		write_token_file(token_file,oatuh_token,oauth_token_secret)
		print >> sys.stderr, "OAuth Success. Token file stored to", token_file

	return twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(oauth_token,oauth_token_secret, consumer_key, consumer_secret))

if __name__ == '__main__':
	oauth_login(APP_NAME,CONSUMER_KEY,CONSUMER_SECRET)

(oauth_token, oauth_token_secret) = read_token_file('out/twitter_oauth')
t = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(oauth_token,oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET))

ids = []
wait_period = 2 
cursor = -1

r = t.users.show.name(screen_name='deathcape',include_entities='id')
for t in r:
	print t.id
