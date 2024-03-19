from transformers import pipeline

# Load the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Sample text for sentiment analysis
text = "I love this product! It's amazing."

# Analyze sentiment
result = classifier(text)

# Get the predicted sentiment label
sentiment_label = result[0]['label']
sentiment_score = result[0]['score']

# Print the predicted sentiment label and score
print("Predicted Sentiment:", sentiment_label)
print("Confidence Score:", sentiment_score)
