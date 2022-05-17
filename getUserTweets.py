# import requests
import snscrape.modules.twitter as sntwitter


def userTweets(username):
  tweets_list1 = []
  maxTweets = 100
  str='from:'+username
  for i,tweet in enumerate(sntwitter.TwitterSearchScraper(str).get_items()):
    if i>maxTweets:
      break
    # if tweet.content[0]=='@':
    #   continue
    tweets_list1.append(tweet.content)
  return tweets_list1
# Bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAJbbQEAAAAAx9JXxtPeZ%2FK0KQYMTPhKfIKx0YA%3DOm3YaPKoqeiZZV573gD1TGN6QUEpA9SMXkY2iQNY2HzEEPEOGb'
#
# def connect_to_twitter():
#   return {"Authorization" : "Bearer {}".format(Bearer_token)}
#
# def make_request(headers):
#   url = 'https://api.twitter.com/2/users/2244994945/tweets/'
#   #params = 'query=from:TwitterDev'
#   params = "max_results=90&tweet.fields=lang,conversation_id,created_at"
#   return requests.request("GET",url,params=params,headers=headers).json()
#
# headers = connect_to_twitter()
#
# response = make_request(headers)
#
# public_tweet=[]
# def public_tweets():
#     for tweet in response['data']:
#       public_tweet.append(tweet['text'])
#     return public_tweet

