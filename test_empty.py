from word_analyzer import word_analyzer

def test_empty():
    with word_analyzer.raises(Exception):
        word_analyzer("empty.txt")
