from wordle_solver import WordleSolver

class TestWordleSolver:
    def test_initialisation(self):
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        assert solver.possible_words == word_list

    def test_suggest_word(self):
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        assert solver.suggest_word() == 'apple'

    def test_process_feedback(self):
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        solver.process_feedback('apple', 'GGGGG')
        assert solver.possible_words == ['apple']

    def test_process_feedback_no_match(self):
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        solver.process_feedback('apple', 'BBBBB')
        assert solver.possible_words == []

    def test_process_feedback_multiple_letter_states(self):
        word_list = ['apple', 'trust', 'piper', 'ghost', 'groom', 'slate', 'furry']
        answer = 'furry'
        solver = WordleSolver(word_list)
        solver.process_feedback('rarer', 'YBGBB')
        assert solver.possible_words == [answer]

    def test_wordle_solver_for_all_green(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer']
        answer = 'grape'
        solver = WordleSolver(word_list)
        solver.process_feedback('grape', 'GGGGG')
        assert solver.possible_words == [answer]
    
    def test_wordle_solver_for_all_yellow(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'pager']
        answer = 'pager'
        solver = WordleSolver(word_list)
        solver.process_feedback('grape', 'YYYYY')
        assert solver.possible_words == [answer]
    
    
        




