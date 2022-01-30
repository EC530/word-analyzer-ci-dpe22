import pytest
from word_analyzer import word_analyzer

def test_noFile():
    with pytest.raises(Exception):
        word_analyzer("joker.txt")
