All tweets bar plot
![All tweets bar](https://cdn.discordapp.com/attachments/905301278647783428/1079792702360649728/image.png)

Average polarity over time
![Avg polarity](https://cdn.discordapp.com/attachments/905301278647783428/1079792812431777863/image.png)

Unfortunately, due to lack of academic access, only last 7 days of replies are available. However, technically, this application would theoretically work with that access.

Process:
1. Gather tweets with keyword "collegeboard"
2. Sentiment analysis for those replies
3. Data analysis

Data from python library [tweepy](https://github.com/tweepy/tweepy), [twitter v2 API](https://developer.twitter.com/en/docs/twitter-api), and sentiment analysis from python library [TextBlob](https://textblob.readthedocs.io/en/dev/).