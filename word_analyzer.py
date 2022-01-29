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
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def word_analyzer(document):
    with open(document) as f:
        lines = f.readlines()
    sentences = "".join(lines)
    new_tokens = word_tokenize(sentences)
    new_tokens = [t.lower() for t in new_tokens]
    new_tokens = [t for t in new_tokens if t not in stopwords.words('english')]
    new_tokens = [t for t in new_tokens if t.isalpha()]
    lemmatizer = WordNetLemmatizer()
    new_tokens = [lemmatizer.lemmatize(t) for t in new_tokens]
    counted = Counter(new_tokens)
    word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
    # print(word_freq.head(30))

    plt.plot(figsize=(8,20))
    sns.barplot(x='frequency',y='word',data=word_freq.head(30))
    plt.show()
    # print("It all ran")

    return word_freq

def main():
    document = input("Please enter the name of the text file you wish to analyze: ")
    word_analyzer(document)

if __name__ == "__main__":
    main()