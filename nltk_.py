# -*- coding: utf-8 -*-
"""nltk_

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Dq7hc0C8szZtX3xLBj9bRVnZHjMbSU1q
"""

!pip install nltk

paragraph="""Salah ad-Din Yusuf ibn Ayyub[a] (c. 1137 – 4 March 1193), commonly known as Saladin,[b] was the founder of the Ayyubid dynasty. Hailing from a Kurdish family, he was the first sultan of both Egypt and Syria. An important figure of the Third Crusade, he spearheaded the Muslim military effort against the Crusader states in the Levant. At the height of his power, the Ayyubid realm spanned Egypt, Syria, Upper Mesopotamia, the Hejaz, Yemen, and Nubia.

Alongside his uncle Shirkuh, a general of the Zengid dynasty, Saladin was sent to Fatimid Egypt in 1164, on the orders of the Zengid ruler Nur ad-Din. With their original purpose being to help restore Shawar as the vizier to the teenage Fatimid caliph al-Adid, a power struggle ensued between Shirkuh and Shawar after the latter was reinstated. Saladin, meanwhile, climbed the ranks of the Fatimid government by virtue of his military successes against Crusader assaults as well as his personal closeness to al-Adid. After Shawar was assassinated and Shirkuh died in 1169, al-Adid appointed Saladin as vizier. During his tenure, Saladin, a Sunni Muslim, began to undermine the Fatimid establishment; following al-Adid's death in 1171, he abolished the Cairo-based Isma'ili Shia Muslim Fatimid Caliphate and realigned Egypt with the Baghdad-based Sunni Abbasid Caliphate."""

paragraph

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#tokenization --converts paragraph-sentences-words
nltk.download('punkt')
sentences= nltk.sent_tokenize(paragraph)

print(sentences)

stemmer =PorterStemmer

from nltk.stem import PorterStemmer

import nltk
from nltk.stem import PorterStemmer

# Download the required resources for nltk
nltk.download('punkt')

# Instantiate the PorterStemmer
stemmer = PorterStemmer()

# Call the stem method with the required argument
stemmed_word = stemmer.stem('lover')

print(stemmed_word)

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
def lemmatize_words(words):
    return [lemmatizer.lemmatize(word) for word in words]
lemmatize_words('eating')

lemmatize_words('eating')

import nltk
from nltk.stem import WordNetLemmatizer

# Download the necessary NLTK resources
nltk.download('wordnet')
nltk.download('omw-1.4')  # Download this for improved lemmatization

lemmatizer = WordNetLemmatizer()

def lemmatize_words(words):
    # If a single word is passed as a string, convert it to a list
    if isinstance(words, str):
        words = [words]
    return [lemmatizer.lemmatize(word) for word in words]

# Test with a single word
print(lemmatize_words('eating'))

# Test with a list of words
print(lemmatize_words(['eating', 'playing', 'running']))

import re
corpus=[]
for i in range(len(sentences)):
  review=re.sub('[^a-zA-Z]',' ',sentences[i])
  review=review.lower()
  review=review.split()
  corpus.append(review)

corpus

for i in corpus:
  words=nltk.word_tokenize(i)
  for word in words:
    if word not in set(stopwords.words('english')):
      print(stemmer.stem(word))