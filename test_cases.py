import random
from wordle_solver import WordleSolver
import word_collection 
import play_wordle


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

    def test_wordle_solver_all_green_except_one(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape']
        answer = 'drape'
        solver = WordleSolver(word_list)
        solver.process_feedback('grape', 'BGGGG')
        assert solver.possible_words == [answer]

    def test_feedback_generator_one_black(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('grape', 'drape')
        assert feedback == 'BGGGG'

    def test_feedback_generator_yellow(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('grape', 'rarer')
        assert feedback == 'BYYBY'

    def test_feedback_generator_all_correct(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('rarer', 'rarer')
        assert feedback == 'GGGGG'
            
    def test_feedback_all_three_states(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape', 'crane', 'drain']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('crane', 'drain')
        assert feedback == 'BGGYB'

    def test_feedback_duplicate_yellows(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape', 'crane', 'freer']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('freer', 'rarer')
        assert feedback == 'BYBGG'

    def test_feedback_duplicate_letters(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape', 'crane', 'freer', 'drier']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('freer', 'drier')
        assert feedback == 'BGBGG'

    def test_feedback_all_blacks(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape', 'crane', 'freer', 'drier']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('freer', 'kudzu')
        assert feedback == 'BBBBB'

    def test_wordle_solves_every_word_small_set(self):
        word_list = ['buyer', 'apple', 'rarer', 'drape', 'eerie', 'melon', 'crane']
        solved = True
        for word in word_list:
            answer = word
            solver = play_wordle.auto_wordle(answer)
            if solver == None :
                solved = False
                break
        assert solved == True

    def test_wordle_solves_all_words(self):
        word_list = word_collection.word_collect()
        solved = True
        for word in word_list:
            answer = word
            solver = play_wordle.auto_wordle(answer)
            if solver == None:
                print(answer)
            
        assert solved == True



        

    
    
        




