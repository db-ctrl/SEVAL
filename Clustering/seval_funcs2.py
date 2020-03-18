from sklearn.cluster import KMeans
from sklearn.neighbors import NearestCentroid
from scipy.stats import entropy
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import pandas as pd
import scipy.stats
import numpy as np

from SEVAL.Tools import SpacyFuncs

# ignore divide by zero
np.seterr(divide='ignore', invalid='ignore')


def text_2_list(corpus):
    # Get raw text as string.
    with open(corpus) as f:
        text = f.read()
        f.close()

    sent_list = str(SpacyFuncs.break_sentences(text)).split(",")
    documents = sent_list

    return documents


def cluster_texts(documents, true_k,):

    vectorizer = TfidfVectorizer(stop_words='english')
    x = vectorizer.fit_transform(documents)

    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(x)

    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()

    return terms, order_centroids


def count_words_in_clus(true_k, order_centroids, terms, sentence, word_count):

    # initialise counters
    words_in_clus, hit_list = ([] for i in range(2))

    # convert sentence to lowercase & split into list of words
    sentence.lower()
    word_list = sentence.split(" ")

    # check if a specific word is in a cluster
    for i in range(true_k):
        print("Cluster %d:" % i),
        # Print x amount of words from each cluster
        for ind in order_centroids[i, :20]:
            hit_list.insert(ind, terms[ind])
            print(' %s' % terms[ind])

        # check if a specific word is in a cluster
        if terms[ind] in word_list:
            words_in_clus.append(str(terms[ind]) + " " + "[" + "%d" % i + "] ")

    ent = entropy([len(words_in_clus) / word_count, (word_count - len(words_in_clus)) / word_count], base=2)

    return [len(words_in_clus), ent]

