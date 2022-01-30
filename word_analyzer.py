# sources: https://www.absentdata.com/python-graphs/python-word-frequency/
# original code modified by dpe22, comments added by dpe22

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import ngrams
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def word_analyzer(document):

    filesize = os.path.getsize(document)
    if filesize == 0: 
        raise Exception("The file is empty, please try again with another text file.")

    # open the document and tokenize words using nltk
    with open(document) as f:
        lines = f.readlines()
    sentences = "".join(lines)
    new_tokens = word_tokenize(sentences)

    # convert all letters to lower-case
    new_tokens = [t.lower() for t in new_tokens]

    # remove english stopwords ("a", "in", "the", etc)
    new_tokens = [t for t in new_tokens if t not in stopwords.words('english')]

    # remove non-words (chapter numbers, page numbers, etc)
    new_tokens = [t for t in new_tokens if t.isalpha()]

    # lemmatize (group together the inflected forms of a word so they can be counted as a single item, identified by the word's lemma or dictionary form)
    lemmatizer = WordNetLemmatizer()
    new_tokens = [lemmatizer.lemmatize(t) for t in new_tokens]

    # create the word_freq data frame (essentially a spreadsheet of words sorted by frequency)
    counted = Counter(new_tokens)
    word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)

    # plot and show the histogram of word frequency
    plt.plot(figsize=(8,20))
    sns.barplot(x='frequency',y='word',data=word_freq.head(30))
    plt.show()

    return word_freq

def main():
    document = input("Please enter the name of the text file you wish to analyze: ")
    word_analyzer(document)

if __name__ == "__main__":
    main()