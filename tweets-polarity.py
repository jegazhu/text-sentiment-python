from textblob import TextBlob
import tweepy
import sys

mykeys = open('twitterkeys.txt', 'r').read().splitlines()

api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'stocks'
tweet_amount = 200

tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)

polarity = 0
positive = 0
negative = 0
neutral = 0

for tweet in tweets:
  final_text = tweet.text.replace('RT', '')
  if final_text.startswith(' @'):
    position = final_text.index(':')
    final_text = final_text[position+2:]
  if final_text.startswith(' @'):
    position = final_text.index(' ')
    final_text = final_text[position+2:]
  #print(final_text)
  analysis = TextBlob(final_text)
  tweet_polarity += analysis.polarity

  if tweet_polarity > 50:
    positive += 1
  elif tweet_polarity < 50:
    negative += 1
  else:
    neutral += 1
  polarity += tweet_polarity

print(polarity)
print(f'Amount of positive tweets: {positive} ')
print(f'Amount of negative tweets: {negative} ')
print(f'Amount of neutral tweets: {neutral} ')
