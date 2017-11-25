import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

list = ["India"]

with open('new300.csv') as f:
    for line in f:
        list.append(line)

vect = TfidfVectorizer(min_df=1)

tfidf = vect.fit_transform(list)
print(tfidf.toarray())
print ((tfidf * tfidf.T).A)

print(vect.get_feature_names())
fout = open("vector-matrix.txt",encoding='utf8',mode='w') 
fout.write(tfidf.toarray())
fout.close()

