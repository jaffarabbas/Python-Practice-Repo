# import stanfordnlp

# # Initialize StanfordCoreNLP
# nlp = stanfordnlp.Pipeline(processors='tokenize,sentiment', lang='en', use_gpu=False)

# # Sample text for analysis
# text = "I love this product! It's amazing."

# # Perform sentiment analysis
# doc = nlp(text)
# sentiment = doc.sentences[0].sentiment

# # Print sentiment
# print(sentiment)
from pycorenlp import StanfordCoreNLP
import json

# Initialize StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

# Sample text for sentiment analysis
text = "Kindly resolve this on priority bases as this issue is stop our daily working."

# Perform sentiment analysis
output = nlp.annotate(text, properties={
    'annotators': 'tokenize,ssplit,pos,lemma,sentiment',
    'outputFormat': 'json'
})


data = json.loads(output)

# Extract sentiment from each sentence
for sentence in data['sentences']:
    sentiment_value = sentence['sentimentValue']
    sentiment = sentence['sentiment']
    print(f"Sentiment: {sentiment}, Sentiment Value: {sentiment_value}")