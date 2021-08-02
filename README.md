# Twitter_Plug_Impact
This project was originally designed to be an analysis of how influencers interact with other users on Twitter. Now it has evolved into a repository of general Twitter Rest API related projects.

## High Profile Impacts.ipynb
Original project with some analysis on how an influencer can increase the interaction with a lower-popularity user on Twitter. It sought to answer the question: How much does a plug by an influencer increase a user's interaction on Twitter?

## twitter_to_S3.py
This is a lambda function that receives a JSON command {'bucket':'bucket_name', 'topic':'topic_for_analysis_on_Twitter'} and prints the first 1000 tweets to a new folder in the specified bucket. You need a config.py file with Twitter API and AWS Credentials. Additionally, you'll need to make a Lambda Layer with the tweepy module included, which is best done via CloudFormation.
