import tweepy
from textblob import TextBlob

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

consumerKey="G0oiJID1FORIUB06d7jThBk1E"
consumerSecret="9oFncuIEBcF0dqaIkA5Y0gGct5CRECc1SjKPGTzKzllCjNoujr"
accessToken="1411813969321291776-2OyZoRrwgyY5bQg1sMY7qc3qQryvIp"
accessTokenSecret="E6Fzg9HRBwiA1Cl3CmZZt9ogTwqJIEahG8hi6aMPDzymM"

authenticate=tweepy.OAuthHandler(consumerKey,consumerSecret)
authenticate.set_access_token(accessToken,accessTokenSecret)
api=tweepy.API(authenticate,wait_on_rate_limit=True)

x="sachin_rt"
posts=api.user_timeline(screen_name=x,count=100,lang="en",tweet_mode="extended")
for tweet in posts[0:5]:
  print(tweet.full_text+'\n')

df=pd.DataFrame([tweet.full_text for tweet in posts],columns=['Tweets'])
df.head

def cleanTxt(text):
  text=re.sub(r'@[A-Za-z0-9]+','',text)
  text=re.sub(r'#','',text)
  text=re.sub(r'RT[\s]+','',text)
  text=re.sub(r'https?:\/\/\S+','',text)
  return text

df['Tweets']=df['Tweets'].apply(cleanTxt)
df

def getSubjectivity(text):
  return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
  return TextBlob(text).sentiment.polarity

df['Subjectivity']=df['Tweets'].apply(getSubjectivity)
df['Polarity']=df['Tweets'].apply(getPolarity)
df

def getAnalysis(score):
  if score<0:
    return 'Negative'
  elif score==0:
    return 'Neutral'
  else:
    return 'Positive'

df['Analysis']=df['Polarity'].apply(getAnalysis)
df

plt.figure(figsize=(8,6))
for i in range(0,df.shape[0]):
  plt.scatter(df['Polarity'][i],df['Subjectivity'][i],color='Blue')

plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()

ptweets=df[df.Analysis=='Positive']
ptweets=ptweets['Tweets']
round((ptweets.shape[0]/df.shape[0]*100),1)

ntweets=df[df.Analysis=='Negative']
ntweets=ntweets['Tweets']
round((ntweets.shape[0]/df.shape[0]*100),1)

df['Analysis'].value_counts()

plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind='bar')
plt.show()