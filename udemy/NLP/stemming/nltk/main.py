from nltk.stem import PorterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer   


words = ["testing","chating","programming","eats"]

stemming = PorterStemmer()

for word in words:
    print("Word --->"+word+" Stemming --->"+stemming.stem(word))


reg_stemmer = RegexpStemmer("ing$|s$|e$|able$",min=4)

print(reg_stemmer.stem("eating"))

snowballstemmer = SnowballStemmer("english") 

for word in words:
    print("Word --->"+word+" Stemming --->"+snowballstemmer.stem(word))