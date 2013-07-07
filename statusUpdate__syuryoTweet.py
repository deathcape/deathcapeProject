#!/usr/bin/env python
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


def oauth_login(app_name=APP_NAME,consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,token_file='out/twitter_oauth'):

	try:
		(oauth_token, oauth_token_secret) = read_token_file(token_file)
	except IOError, e:
		(oauth_token, oauth_token_secret) = oauth_dance('deathcape', consumer_key, consumer_secret)

		if not os.path.isdir('out'):
			os.mkdir('out')
		write_token_file(token_file,oatuh_token,oauth_token_secret)
		print >> sys.stderr, "OAuth Success. Token file stored to", token_file

	return twitter.Twitter(domain='api.twitter.com', api_version='1.1', auth=twitter.oauth.OAuth(oauth_token,oauth_token_secret, consumer_key, consumer_secret))

if __name__ == '__main__':
	oauth_login(APP_NAME,CONSUMER_KEY,CONSUMER_SECRET)

(oauth_token, oauth_token_secret) = read_token_file('out/twitter_oauth')
t = twitter.Twitter(domain='api.twitter.com', api_version='1.1', auth=twitter.oauth.OAuth(oauth_token,oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET))

Syuryo_t={}

if sys.argv[1]=='1':
	Syuryo_t[0]='a'
else:
	Syuryo_t[0]=sys.argv[1]

if Syuryo_t[0]=='a':
	def errorMessage():
		print 'error.'
	def fnc0():
		Syuryo_t[1]='can'
	def fnc1():
		Syuryo_t[1]='bottle'
	def fnc2():
		Syuryo_t[1]='glass'

else:
	def errorMessage():
		print 'error.'
	def fnc0():
		Syuryo_t[1]='cans'
	def fnc1():
		Syuryo_t[1]='bottles'
	def fnc2():
		Syuryo_t[1]='glasses'
fnc2Dict={'c':fnc0,'b':fnc1,'g':fnc2}
fnc2Dict[sys.argv[2]]()

def errorMessage():
	print "error."
def fnc0():
	Syuryo_t[2]='beer'
def fnc1():
	Syuryo_t[2]='draftBeer'
def fnc2():
	SYuryo_t[2]='wine'
def fnc3():
	Syuryo_t[2]='sake'
fnc3Dict={'b':fnc0,'db':fnc1,'w':fnc2,'s':fnc3}
fnc3Dict[sys.argv[3]]()

#print u'9152'u'91cf'
#print '酒量'
t.statuses.update(status=Syuryo_t[0] + ' ' + Syuryo_t[1] + ' of ' + Syuryo_t[2] + ' #酒量')
