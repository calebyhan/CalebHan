All tweets bar plot
![All tweets bar](https://cdn.discordapp.com/attachments/905301278647783428/1079226601839001608/image.png)

Average polarity over time
![Avg polarity](https://cdn.discordapp.com/attachments/905301278647783428/1079226671003086898/image.png)

Unfortunately, due to lack of academic access, only last 7 days of replies are available. However, technically, this application would theoretically work with that access.

Process:
1. Gather tweets since Elon Musk bought twitter (October 27, 2022)
2. Gather top 100 replies to those tweets (if less than 100 replies then gets all those replies)
3. Sentiment analysis for those replies
4. Data analysis

Data from python library [tweepy](https://github.com/tweepy/tweepy), [twitter v2 API](https://developer.twitter.com/en/docs/twitter-api), and sentiment analysis from python library [TextBlob](https://textblob.readthedocs.io/en/dev/).
