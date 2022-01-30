import pytest
from word_analyzer import word_analyzer

def test_format():
    with pytest.raises(Exception):
        word_analyzer("EE-2025.pdf")
