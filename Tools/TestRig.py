from scipy.stats import entropy

words_in_clus = ["hi", "bye", "no"]

word_count = 7

ent = entropy([len(words_in_clus) / word_count], base=2)
