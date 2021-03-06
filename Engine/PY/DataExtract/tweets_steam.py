
import json
import os
import sys

# Add lins directory to module search path "libs"
parent_dir = os.path.abspath(os.path.dirname(__file__))
libs_dir = os.path.join(parent_dir, 'libs')
sys.path.append(libs_dir)

# Now you can import any library located in the "libs" folder !
import tweepy
from textblob import TextBlob

# For others languages
from textblob.classifiers import NaiveBayesClassifier
import nltk
input_lexicon_fr = open('.\Classifiers\classifier_fr.json', 'r')

#python -m textblob.download_corpora
cl_fr = NaiveBayesClassifier(input_lexicon_fr, format="json")

#Read Config_File
#with open('C:\DEV\Python\config.json') as json_data_file:
with open('D:\Perso\DEV\Python\config.json') as json_data_file:
    config_data = json.load(json_data_file)

consumer_key=config_data['twitter']['CONSUMER_KEY']
consumer_secret=config_data['twitter']['CONSUMER_SECRET']
access_token=config_data['twitter']['ACCESS_TOKEN']
access_token_secret=config_data['twitter']['ACCESS_SECRET']

def analize_sentiment(text):
    analysis = TextBlob(text)
    #print("language : " + analysis.detect_language())
    if(analysis.detect_language() == 'en'):
        if analysis.sentiment.polarity > 0.5:
            return 1
        elif analysis.sentiment.polarity < 0:
            return -1
        else:
            return 0
    else:
        return 0


# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    nb_tweets = 0
    sum_pol = 0
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)        
        #print(json.dumps(tweet, indent=4, sort_keys=True))
        tweet_date = tweet["created_at"]
        tweet_author = tweet['user']['screen_name']
        tweet_text = str(tweet['text'].encode('ascii', 'ignore'))
        # Print out the Tweet
        PrintListener.nb_tweets+=1
        PrintListener.sum_pol += analize_sentiment(tweet_text)        
        print(str(PrintListener.nb_tweets) + ' - ' + tweet_date + ' - @' + tweet_author + ' :   ' + tweet_text)
        print('-----sum pol : ' + str(PrintListener.sum_pol))
        #print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    Words = 'bitcoin'
    # Show system message
    print('I will now print Tweets containing "' + Words + '"! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=[Words])