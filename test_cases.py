from wordle_solver import WordleSolver
import word_collection 
import play_wordle


class TestWordleSolver:
    def test_initialisation(self):
        """
        This test checks the word list can be instantiated into the class correctly.
        """
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        assert solver.possible_words == word_list

    def test_suggest_word(self):
        """
        This test checks the suggest_word method works on a small data set based on wordle_word_data.py 
        """
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        assert solver.suggest_word() == 'apple'

    def test_process_feedback(self):
        """
        This test checks the process_feedback method returns the correct word given the unique feedback which signifies the 
        guess is the same as the answer. 
        """
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        solver.process_feedback('apple', 'GGGGG')
        assert solver.possible_words == ['apple']

    def test_process_feedback_no_match(self):
        """
        This test checks the process_feedback method if there exists no match in the given word list that it returns a valid output and not an error.
        In this case if no possible words are left after any feedback input, the function returns an empty list. 
        """
        word_list = ['apple', 'grape', 'melon']
        solver = WordleSolver(word_list)
        solver.process_feedback('apple', 'BBBBB')
        assert solver.possible_words == []

    def test_process_feedback_multiple_letter_states(self):
        """
        This test ensures the process_feedback method works for extreme cases of guesses. The first of these include duplicate letters in
        the answer with each letter having multiple states of existence. 
        
        This test specifically checks if the letter 'r' oocurs in the correct position and the incorrect position in the same word,
        hinting that the answer has more than one 'r' in it and we have correctly identified the position of one of them, however the next
        'r's position is still undetermined. 
        """
        word_list = ['apple', 'trust', 'piper', 'ghost', 'groom', 'slate', 'furry']
        answer = 'furry'
        solver = WordleSolver(word_list)
        solver.process_feedback('rarer', 'YBGBB')
        assert solver.possible_words == [answer]

    def test_wordle_solver_for_all_green(self):
        """
        This test checks if the wordle solver can identify the correct answer given a list of words and the unique feedback which ends the 
        game loop. This being 'GGGGG' means every letter in the guess matches with the position and letter in the answer. The only case in which
        this occurs is is the user's guess and the answer are the same. 
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer']
        answer = 'grape'
        solver = WordleSolver(word_list)
        solver.process_feedback('grape', 'GGGGG')
        assert solver.possible_words == [answer]
    
    def test_wordle_solver_for_all_yellow(self):
        """
        This test checks for the extreme value that all letters in the guess exist, but none are correctly positioned. This implies that all
        subsequent guesses should be different permutations of these letters as they all have been given the 'Y' as their feedback. 
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'pager']
        answer = 'pager'
        solver = WordleSolver(word_list)
        solver.process_feedback('grape', 'YYYYY')
        assert solver.possible_words == [answer]

    def test_wordle_solver_all_green_except_one(self):
        """
        This test checks that the process_feedback() method only returns a word list that differ by one letter compared to the guess. The letter
        which returned 'B' as its feedback should be the only letter that changes in the returned word list. 
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape']
        answer = 'drape'
        solver = WordleSolver(word_list)
        solver.process_feedback('grape', 'BGGGG')
        assert solver.possible_words == [answer]

    def test_feedback_generator_one_black(self):
        """
        This test checks that the generate_feedback() method returns the appropriate feedback given a guess and an answer. The method 
        works like if the letter in the guess is correct and correclty positioned returns a 'G'. If the letter from the guess is nowhere in the answer, it 
        returns 'B'. If the letter from guess exists in the word but its position in the answer and the guess are different, then it returns 'Y'. 
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('grape', 'drape')
        assert feedback == 'BGGGG'

    def test_feedback_generator_yellow(self):
        """
        This test handles more than one 'Y' letter. As the Wordle game assigns 'Y' letters from left to right, meaning if a letter occurs in the guess
        which is in the answer, then it returns 'Y'. However, if their is a duplicate of this letter later in the guess which is in the word but either 
        incorrectly positioned or correctly positioned, and the answer only has one instance of this letter. Then the previous assignment of 'Y' from the 
        first instance of this letter in the guess should be reset to 'B' and the correclty positioned letter should be assigned 'G'. Only if there is several instances
        of the same letter in the guess and the answer should the same letter be assgined 'Y' again. 
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('grape', 'rarer')
        assert feedback == 'BYYBY'

    def test_feedback_generator_all_correct(self):
        """
        This test checks the simple case that if the word and the answer match perfectly, that the feedback provided is a string of five 'G's. This signifies
        every letter is correct and correctly positioned, the unique case in which this occurs is if the two inputs of generate_feedback() are the same. 
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('rarer', 'rarer')
        assert feedback == 'GGGGG'
            
    def test_feedback_all_three_states(self):
        """
        This test checks that the generate_feedback() method can assign all three letter feedback states correctly when they all should occur when
        comparing a given guess and answer
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape', 'crane', 'drain']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('crane', 'drain')
        assert feedback == 'BGGYB'

    def test_feedback_duplicate_yellows(self):
        """
        This tests checks that the generate_feedback method can correctly assign 'Y' letter feedbacks when it exists in both the other two states. 
        If the test returns too many words in the word list, it could then prevent the next best guess algorithm from erroneous suggestions. 
        """
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
        

    def test_feedback_possilbities(self):
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape', 'crane', 'freer', 'drier']
        solver = WordleSolver(word_list)
        answer = 'drape'
        guess = 'apple'
        possible_feedbacks = solver._generate_all_possible_feedbacks(answer)
        print(possible_feedbacks)






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


def number_of_attempts_to_guess():
    word_list = word_collection.word_collect()[1000:1300]
    attempt_dict = {}
    for word in word_list:
        answer = word
        solver = play_wordle.auto_wordle(answer)
        if solver == None:
            print(answer)
        attempt_dict[solver] = attempt_dict.get(solver, 0) + 1
    
    return attempt_dict

# print(number_of_attempts_to_guess())


        

    
    
        




