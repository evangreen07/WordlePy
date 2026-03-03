import pytest
import word_collection
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

    def test_process_feedback_multiple_letter_states(self):
        word_list = ['apple', 'trust', 'piper', 'ghost', 'groom', 'slate', 'furry']
        answer = 'furry'
        solver = WordleSolver(word_list)
        solver.process_feedback('rarer', 'YBGBB')
        assert solver.possible_words == [answer]




