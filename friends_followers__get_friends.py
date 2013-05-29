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

while cursor != 0:
 if wait_period > 3600: 
  print 'Too many retries. Saving partial data to disk and exiting'
  f = file('%s.friend_ids' % str(cursor), 'wb')
  cPickle.dump(ids, f)
  f.close()
  exit()

 try:
  response = t.friends.ids(screen_name=SCREEN_NAME, cursor=cursor)
  ids.extend(response['ids'])
  wait_period = 2
 except twitter.api.TwitterHTTPError, e:
  if e.e.code == 401:
   print 'Encountered 401 Error (Not Authorized)'
   print 'User %s is protecting their tweets' % (SCREEN_NAME, )
  elif e.e.code in (502, 503):
   print 'Encountered %i Error. Trying again in %i seconds' % (e.e.code, wait_period)
   time.sleep(wait_period)
   wait_period *= 1.5
   continue
  elif t.account.rate_limit_status()['remaining_hits'] == 0:
   status = t.account.rate_limit_status()
   now = time.time() # UTC
   when_rate_limit_resets = status['reset_time_in_seconds'] # UTC
   sleep_time = when_rate_limit_resets - now
   print 'Rate limit reached. Trying again in %i seconds' % (sleep_time,)
   time.sleep(sleep_time)
   continue
 cursor = response['next_cursor']
 print 'Fetched %i ids for %s' % (len(ids), SCREEN_NAME)
 if len(ids) >= friends_limit:
  break

print ids
