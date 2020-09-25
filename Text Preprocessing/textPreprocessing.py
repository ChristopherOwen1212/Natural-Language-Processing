
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer
import string

# remove punctuation 
def remove_punctuation(text): 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator) 

text = "National health services worldwide are struggling to deal with a flood of coronavirus patients"

case_folding = remove_punctuation(text).lower()

tokens = word_tokenize(case_folding)

tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
print(tokens_without_sw)

ps = PorterStemmer()
lemmatizer=WordNetLemmatizer()

print("lemmatize: ")
for word in tokens_without_sw:
  print(lemmatizer.lemmatize(word))

print("\n\n")

print("Stemmer: ")
for word in tokens_without_sw:
  print(ps.stem(word))  
