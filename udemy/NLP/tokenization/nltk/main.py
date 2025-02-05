#Tokenisation
# Sentence --> paragragh

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer


corpus = """Hello World's,this is jaffar abbas.
Please follow my github repository
"""

print(sent_tokenize(corpus))

document = sent_tokenize(corpus)
print(word_tokenize(document[0]))
print(wordpunct_tokenize(document[0]))

tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize(corpus))