import nltk
import random
import json
import re
import pickle
from nltk.twitter import Twitter
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import datetime

tw = Twitter()

# Grab credentials from file
oauth = credsfromfile()

# Search API
client = Query(**oauth)
tweets = client.search_tweets(keywords='Korean, summit', limit=10000)
tweet = next(tweets)

# Open data file
outfile = open("korean_summit_data.txt","ab+")

# Timestamp to file
timestamp = datetime.datetime.now()
timestamp = timestamp.isoformat()
outfile.write(timestamp)
outfile.write("\n\n")

# File for testing
# out_file = open("tweet_data")


def pre_process_tweets(unprocessed_tweets):
    text = []
    words_list = []
    clean_list = []

    # Get all tweet text in english
    for tweet in unprocessed_tweets:
        if tweet['lang'] == "en":
            text.append(tweet['text'])

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


tweet_text = pre_process_tweets(tweets)

# for text in tweet_text:
#     print(text)

sid = SentimentIntensityAnalyzer()
for sentence in tweet_text:
    outfile.write(sentence)
    outfile.write("\n")
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        outfile.write('{0}: {1}, '.format(k, ss[k]))
    outfile.write("\n\n")


# documents = tweet_text
# random.shuffle(documents)
# all_words = []
#
# for w in tw:
#     all_words.append(w.lower())
#
# all_words = nltk.FreqDist(all_words)
# print(all_words)

# word_features = list(all_words.keys())[:3000]


# print(word_features)

# def find_features(document):
#     words = set(document)
#     features = {}
#     for wrd in word_features:
#         features[wrd] = (wrd in words)
#
#     return features
#
#
# ftrs = find_features(movie_reviews.words('neg/cv000_29416.txt'))
# f1 = json.dumps(ftrs)
# file = open("foo.txt", "w")

# file.write(f1)
# file.close()
# feature_sets = [(find_features(rev), category) for (rev, category) in documents]
# print("feature sets below\n---------------------\n")
# print(feature_sets)

# set that we'll train our classifier with
# training_set = feature_sets[:1900]

# set that we'll test against.
# testing_set = feature_sets[1900:]

# define classifier as NB
# classifier = nltk.NaiveBayesClassifier.train(training_set)

# print accuracy
# print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set)) * 100)

# Show most informative features
# classifier.show_most_informative_features(15)

# Saving a classifier with pickle
# save_classifier = open("naivebayes.pickle", "wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

# Using an existing classifier
# classifier_f = open("naivebayes.pickle", "rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()
print("Run Successful")
