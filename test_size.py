import pytest
from word_analyzer import word_analyzer

def test_size():
    with pytest.raises(Exception):
        word_analyzer("tooSmall.txt")
