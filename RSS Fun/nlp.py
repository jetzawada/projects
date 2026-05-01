import nltk
from nltk.sentiment import *
nltk.download('vader_lexicon')
import pandas as pd

data = pd.read_csv("news.csv")
print(data.head())


sentiments = pd.DataFrame(columns=['title_sentiment', 'summary_sentiment'])

sid = SentimentIntensityAnalyzer()

for row in data.itertuples():
    title_sentiment = sid.polarity_scores(row.title).get('compound')
    summary_sentiment = sid.polarity_scores(row.summary).get('compound')

    nr = [title_sentiment, summary_sentiment]

    sentiments.loc[len(sentiments)] = nr

print(sentiments)





