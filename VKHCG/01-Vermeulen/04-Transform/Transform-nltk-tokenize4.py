# -*- coding: utf-8 -*-
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

  
new_text = "Practical Data Science"

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
    