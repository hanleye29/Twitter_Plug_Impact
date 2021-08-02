import json
import boto3
import tweepy as tw
import config
import time

def lambda_handler(event, context):
    
    def getTweets():
        auth = tw.OAuthHandler(config.API_Key, config.API_Secret_Key)
        auth.set_access_token(config.Access_Token, config.Access_Token_Secret)
        api = tw.API(auth, wait_on_rate_limit=True)
        
        query = event.get('topic')
        max_tweets = 1000
        search =[status for status in tw.Cursor(api.search, q = query).items(max_tweets)]
        
        tweet_data = []
        desired_fields = ['created_at', 'text','lang']
        user_fields = ['name','screen_name','location','description', 'followers_count','friends_count']
        temp_dict = {}

        for i in range(len(search)):
            temp_dict = {}
            for key, value in search[i]._json.items():
                if key in desired_fields:
                    temp_dict[key] = value
                elif key == 'user':
                    for key2, value2 in search[i]._json['user'].items():
                        if key2 in user_fields:
                            temp_dict[key2] = value2
            tweet_data.append(temp_dict)
    
        return tweet_data
        
    s3 = boto3.client('s3', aws_access_key_id = config.aws_key, aws_secret_access_key = config.aws_secret)
    target_bucket = event.get('bucket')
    topic = event.get('topic')
    tweets = getTweets()
    s3.put_object(Bucket = target_bucket, Key = topic + '/')
    
    for tweet in tweets:
        s3.put_object(
            Body = json.dumps(tweet),
            Bucket = target_bucket,
            Key = topic + '/' + (tweet['created_at'] + tweet['screen_name']).replace(" ",""),
            ContentType = 'text'
            )
    
    return (tweets[0]['screen_name'] + '_____' + tweets[1]['screen_name'])
