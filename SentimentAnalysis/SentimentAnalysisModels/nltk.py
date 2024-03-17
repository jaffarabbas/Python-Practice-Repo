from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
text = "Kindly resolve this on priority bases as this issue is stop our daily working."

# Analyze sentiment
sentiment_scores = sia.polarity_scores(text)

# Get the compound sentiment score
compound_score = sentiment_scores['compound']

# Determine sentiment label based on the compound score
if compound_score >= 0.05:
    sentiment_label = 'positive'
elif compound_score <= -0.05:
    sentiment_label = 'negative'
else:
    sentiment_label = 'neutral'

# Print the predicted sentiment label
print("Predicted Sentiment:", sentiment_label)