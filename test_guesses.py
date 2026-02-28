import pytest
from next_guess import wordle_result

def test_reduce_dict_removes_words_with_letter():
    words = ["apple", "banana", "cherry", "date"]
    result = wordle_result(words, "a")
    assert result == ["cherry"]



def test_reduce_dict_no_matches():
    words = ["xyz", "qwerty"]
    result = wordle_result(words, "a")
    assert result == ["xyz", "qwerty"]


def test_reduce_dict_all_contain_letter():
    words = ["apple", "cherry", "pilot"]
    result = wordle_result('crane', 'BBYGG', words)
    assert result == ['cherry', 'pilot']
