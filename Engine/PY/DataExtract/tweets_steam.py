import libs.tweepy.utils
import json



#Read Config_File
with open('C:\DEV\Python\config.json') as json_data_file:
#with open('D:\Perso\DEV\Python\config.json') as json_data_file:
    config_data = json.load(json_data_file)

consumer_key=config_data['twitter']['CONSUMER_KEY']
consumer_secret=config_data['twitter']['CONSUMER_SECRET']
access_token=config_data['twitter']['ACCESS_TOKEN']
access_token_secret=config_data['twitter']['ACCESS_SECRET']


# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    nb_tweets = 0
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)        
        #print(json.dumps(tweet, indent=4, sort_keys=True))
        tweet_date = tweet["created_at"]
        tweet_author = tweet['user']['screen_name']
        tweet_text = str(tweet['text'].encode('ascii', 'ignore'))
        # Print out the Tweet
        PrintListener.nb_tweets+=1
        print(str(PrintListener.nb_tweets) + ' - ' + tweet_date + ' - @' + tweet_author + ' :   ' + tweet_text)
        #print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Python"! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['Bitcoin'])