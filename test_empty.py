from word_analyzer import word_analyzer

def test_empty():
    with pytest.raises(Exception):
        word_analyzer("empty.txt")
