from textblob import TextBlob

text = """
Kindly resolve this on priority bases as this issue is stop our daily working.
"""

blob = TextBlob(text)

def evaluatePolartiy(plority):
    if plority < 0:
        return "Negative"
    elif plority == 0:
        return "Neutral"
    else:
        return "Positive"

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
    print(evaluatePolartiy(sentence.sentiment.polarity))