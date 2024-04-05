import os
import json
import datetime
import nltk
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    translator = str.maketrans('', '', string.punctuation)
    text_no_punctuation = text.translate(translator)
    tokens = nltk.word_tokenize(text_no_punctuation)
    stop_words = set(stopwords.words('english'))
    tokens = [word.lower() for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def idk(test_labels, retrieved_items, D, test_data, th = 1.5917805):
    bad_retrieved_items = [(v,l,n) for (v,l,m,n) in zip(test_labels, retrieved_items, D, test_data) if min(m[0])>=th]
    bad_retrieved_labels = [i[0] for i in bad_retrieved_items]
    bad_retrieved_query = [i[2] for i in bad_retrieved_items]
    bad_retrieved_items = [i[1] for i in bad_retrieved_items]

    good_retrieved_items = [(v,l, n) for (v,l,m, n) in zip(test_labels, retrieved_items, D, test_data) if min(m[0])<th]
    good_retrieved_labels = [i[0] for i in good_retrieved_items]
    good_retrieved_query = [i[2] for i in good_retrieved_items]
    good_retrieved_items = [i[1] for i in good_retrieved_items]

    k = len(good_retrieved_items[0])
    
    bad_retrieved_items = [["None"]*k for i in range(len(bad_retrieved_items))]
    retrieved_items_ = good_retrieved_items + bad_retrieved_items
    test_labels_ = good_retrieved_labels + bad_retrieved_labels
    test_query = good_retrieved_query + bad_retrieved_query

    retrieved_items_clean = []
    for i in retrieved_items_:
        temp = []
        for x in i:
            temp.append(preprocess_text(x))
        retrieved_items_clean.append(temp)

    test_labels_clean = [x if isinstance(x, str) else "None" for x in test_labels_]
    test_labels_clean = [preprocess_text(x) for x in test_labels_clean]

    return test_labels_clean, retrieved_items_clean, test_query