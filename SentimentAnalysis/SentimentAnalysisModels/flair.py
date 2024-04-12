from flair.models import TextClassifier
from flair.data import Sentence

# Load the pre-trained sentiment analysis model
classifier = TextClassifier.load('en-sentiment')

# Sample text for sentiment analysis
text = ["Please solved this issue on your top priority."]

# Create a Sentence object
for i in text:
    sentence = Sentence(i)

    # Predict sentiment
    classifier.predict(sentence)

    # Get the predicted sentiment label
    sentiment_label = sentence.labels[0].value

    # Print the predicted sentiment label
    print("Predicted Sentiment:", sentiment_label)
