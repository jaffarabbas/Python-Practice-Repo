from textblob import TextBlob

text = """
i am disappointed
"""

blob = TextBlob(text)

def evaluatePolartiy(plority):
    if plority < 0:
        return "Negative"
    elif plority == 0:
        return "Neutral"
    else:
        return "Positive"

sentences = 0.0

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
    print(evaluatePolartiy(sentence.sentiment.polarity))
    
    
