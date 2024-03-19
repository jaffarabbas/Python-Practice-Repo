from pycorenlp import StanfordCoreNLP
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flair.models import TextClassifier
from flair.data import Sentence
from transformers import pipeline
import pandas as pd


def falir_model(text):
    classifier = TextClassifier.load('en-sentiment')
    sentence = Sentence(text)
    classifier.predict(sentence)
    return sentence.labels[0].value


def text_blob(text):
    blob = TextBlob(text)
    sentiment = 0.0
    for sentence in blob.sentences:
        sentiment += sentence.sentiment.polarity
    return sentiment


def evaluatePolartiy(plority, range):
    if plority < range[0]:
        return "Negative"
    elif plority == range[1]:
        return "Neutral"
    else:
        return "Positive"
