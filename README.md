# word-analyzer-ci-dpe22  [![Python test](https://github.com/EC530/word-analyzer-ci-dpe22/actions/workflows/python-test.yml/badge.svg)](https://github.com/EC530/word-analyzer-ci-dpe22/actions/workflows/python-test.yml)

### Purpose
    - This script counts the number of times each word appears in a text file.
    - The word_analyzer function returns a dataframe containing words and frequencies
    - The word_analyzer function outputs a histogram of the top 30 words by frequency
    - This script requires a text file input specified by the user, which must be located in the same directory
    - This script removes NLTK english stop words from the frequency count
    
### System Requirements
    - Python 3.7, 3.8, 3.9, 3.10
    - Ubuntu latest release
    
### Unit Testing
    - Empty text file
    - Too few words
    - Too few unique words
    - Wrong file format
    - File not found

### Sample Output (US Constitution)
![image](https://user-images.githubusercontent.com/74585697/151681831-97b8bc03-1d37-447c-bbd8-87a8e7919f63.png)

### Sample Output (KJV Bible)
![image](https://user-images.githubusercontent.com/74585697/151681835-dfe22fe4-7c62-426f-93b7-23e8e2b5ccd9.png)
