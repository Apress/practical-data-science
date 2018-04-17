# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import gutenberg
macbeth = gutenberg.words("shakespeare-macbeth.txt")
stopwords = set(nltk.corpus.stopwords.words())
fd = nltk.FreqDist([w for w in macbeth if w.lower() not in stopwords
      and len(w) > 3 and w.isalpha()])
d=list(fd.keys())
print (d[0:50])