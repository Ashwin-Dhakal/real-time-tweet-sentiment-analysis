from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="w8wyoAKvlN9MEDR18HFzKyzUA"
csecret="W4R5i6VAkTgs6Tr6Ij3Jfk8x6k1rkqdPzb5R2JkFq2ccTQqdVr"
atoken="4157664553-PmCikHvFMBXmUf71TruTVi4hg8L4s2kdYaZgg5i"
asecret="Y4rxXI6s8TDmJD5YQZLRqHLPb7d9iTBFi40eoO7weE7Sw"

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])