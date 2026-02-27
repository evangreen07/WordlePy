import pytest
from next_guess import reduce_dict

def test_reduce_dict_removes_words_with_letter():
    words = ["apple", "banana", "cherry", "date"]
    result = reduce_dict(words, "a")
    assert result == ["cherry"]


def test_reduce_dict_empty_list():
    words = []
    result = reduce_dict(words, "a")
    assert result == []


def test_reduce_dict_no_matches():
    words = ["xyz", "qwerty"]
    result = reduce_dict(words, "a")
    assert result == ["xyz", "qwerty"]


def test_reduce_dict_all_contain_letter():
    words = ["apple", "add", "ants"]
    result = reduce_dict(words, "a")
    assert result == []
