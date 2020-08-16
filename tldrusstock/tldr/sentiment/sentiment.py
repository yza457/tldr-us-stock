import multiprocessing as mp
import tweepy as tp
import re
from textblob import TextBlob

numTweets = 100

def getOneStock(api, s, error):
  if error:
    return (0.0, 0.0)
  # get tweet
  tweet = []
  try:
    tweets = [tw.full_text for tw in api.search(q=s,lang="en",count=numTweets,tweet_mode='extended')]
  except:
    print("exception in twitter search")
    return (None, None)

  # clean @tag, $tag, ampersand (words like S&P), RT, links and numbers (e.g. 500, 500M)
  # hashtag is reserved
  for i, v in enumerate(tweets):
    tweets[i] = ' '.join(re.sub( "(@[A-Za-z0-9_]+)|(\$[A-Za-z_]+)|([0-9]+[a-zA-Z]+)|([^\s]+\&[^\s]+)|([^A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", v).split())

  # for each tweet analyse the sentiment
  positiveCount = 0
  negativeCount = 0

  for t in tweets:
    # get if one tweet is positive or negative
    res = TextBlob(t)
    sen = res.sentiment.polarity 
    if  sen > 0:
      positiveCount += 1
    elif sen < 0:
      negativeCount += 1

  return (positiveCount / numTweets, negativeCount / numTweets)

def getSentiment(stockList, error):
  # do twitter auth
  key = 'wlDYofYZvBD5PR7zKKHbZvtCZ'
  secret = '8m2IlKMZo2R9SwcYnapWLXqIiK2RmXJzsORfHkREw6XlGOooYb'

  try:
    auth = tp.AppAuthHandler(key, secret)
    api = tp.API(auth)
  except:
    print("exception in twitter auth")
  
  argList = zip(stockList, error)

  # parallel map the sentiment analysis for each stock
  p = mp.Pool(mp.cpu_count())
  res = p.starmap(getOneStock, [(api, arg[0], arg[1]) for arg in argList] )
  p.close()

  # print(res)
  return res

# if __name__ == "__main__":
#   getSentiment(["tsla", "aapl", "msft", "goog"])