import pytest
from word_analyzer import word_analyzer

def test_unique():
    with pytest.raises(Exception):
        word_analyzer("notUnique.txt")
