from flair.models import TextClassifier
from flair.data import Sentence
import pandas as pd

# Load the pre-trained sentiment analysis model
classifier = TextClassifier.load('en-sentiment')

# scrape data from excel
df = pd.read_excel('C:\\Users\\DARKLORD\\Documents\\CustomerResponses.xlsx')
data_list = df.to_dict(orient='records')

# Dictionary to store sentiment scores by customer title
sentiment_scores = {}

# Iterate over each row in the data list
for row in data_list:
    text = row['CustomerRemarks']
    title = row['CustomerTitle']

    # Skip rows where CustomerRemarks is not a string
    if not isinstance(text, str):
        continue

    # Predict sentiment
    sentence = Sentence(text)
    classifier.predict(sentence)
    sentiment_label = sentence.labels[0].value

    # Update sentiment scores for the current customer title
    if title not in sentiment_scores:
        sentiment_scores[title] = {'POSITIVE': 0, 'NEGATIVE': 0, 'NEUTRAL': 0}
    sentiment_scores[title][sentiment_label] += 1

# Calculate sentiment percentages for each customer title
for title, scores in sentiment_scores.items():
    total = sum(scores.values())
    percentages = {label: (count / total) * 100 for label, count in scores.items()}
    print(f"Customer Title: {title}")
    for label, percentage in percentages.items():
        print(f"{label}: {percentage:.2f}%")
    print()
