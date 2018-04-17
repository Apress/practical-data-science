# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "I am reading a book called Practical Data Science \
and it is making me a better data scientist."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        
print('\n','Complete List of Words','\n')
print(word_tokens)
print('\n', 'Filtered List of Words','\n')
print(filtered_sentence)