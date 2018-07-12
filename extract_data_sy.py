import nltk
import random
import json
import re
import csv
from nltk.twitter import Twitter
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
from nltk.sentiment.vader import SentimentIntensityAnalyzer


tw = Twitter()
sid = SentimentIntensityAnalyzer()

# Grab credentials from file
oauth = credsfromfile()

# Search API
client = Query(**oauth)
tweets = client.search_tweets(keywords='Syria', limit=10000)
tweet = next(tweets)

# Open data file
outfile = open("syria_auto.csv","a")
writer = csv.writer(outfile)
mydata = ['DATE', 'TWEET', 'COMPOUND', 'NEGATIVE', 'NEUTRAL', 'POSITIVE','LATITUDE','LONGITUDE']
# writer.writerow(mydata)

def pre_process_text(tweet):
    text = []
    words_list = []
    clean_list = []

    # Get all tweet text in english
    if tweet['lang'] == "en":
        text.append(tweet['text'])
    else:
        return None

    # Break up into individual words
    for w in text:
        words_list.append(w.split())

    # Clean data and remove twitter IDs and RTs
    for element in list(words_list):

        for word in list(element):

            if word.startswith("http") or word.startswith("https"):
                element.remove(word)

            elif element[0].startswith("@"):
                element.remove(element[0])

            elif element[0] == "RT":
                element.remove("RT")

            else:
                regex = re.findall(r"(\w|\s|\#|\'|\!)", word)
                wrd = ''.join(regex)
                element.remove(word)
                element.append(wrd)

    for w in words_list:
        clean_list.append(" ".join(w))

    return clean_list
def main():
    temp = None
    for tweet in tweets:
        
        # Date and Time
        mydata[0] = tweet['created_at']
        
        # Processed text data
        for sentance in pre_process_text(tweet):
            temp = sentance
        mydata[1] = sentance
        
        # Sentiment analysis on text
        ss = sid.polarity_scores(temp)
        mydata[2] = ss['compound']
        mydata[3] = ss['neg']
        mydata[4] = ss['neu']
        mydata[5] = ss['pos']
        
        # Latitude and Longitude if available
        if tweet['place'] is not None:
            mydata[6] = tweet['place']['bounding_box']['coordinates'][0][0][1]
            mydata[7] = tweet['place']['bounding_box']['coordinates'][0][0][0]
        else:
            mydata[6] = None
            mydata[7] = None

        writer.writerow(mydata)

    print("syria_data_extracted")


