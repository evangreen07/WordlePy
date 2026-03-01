import pytest

from wordle_solver import WordleSolver

class TestWordleSolver:
    def test_initialisation(self):
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        assert solver.possile_words == word_list

    def test_suggest_word(self):
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        assert solver.suggest_word() == 'apple'

    def test_process_feedback(self):
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        solver.process_feedback('apple', 'GGGGG')
        assert solver.possile_words == ['apple']

    def test_process_feedback_no_match(self):
        word_list = ['apple', 'grape', 'miron']
        solver = WordleSolver(word_list)
        solver.process_feedback('apple', 'BBBBB')
        assert solver.possile_words == ['miron']

    




