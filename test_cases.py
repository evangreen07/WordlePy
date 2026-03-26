from wordlepy.wordle_solver import WordleSolver
from wordlepy import word_collection 
from wordlepy import play_wordle
from wordlepy import wordle_word_data


class TestWordleSolver:

    def test_word_get_letter_dict(self):
        """
        This test checks the letter dictionary is loaded correctly.
        """
        letter_dict = wordle_word_data.get_letter_dict()
        assert letter_dict == {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    
    def test_all_etter_frequencies(self):
        """
        This test checks the function correclty identifies the frequencies of different letters.
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        letter_dict = wordle_word_data.all_letter_frequencies(words)
        letter_dict = {letter: letter_dict[letter] for letter in letter_dict if letter_dict[letter] != 0}
        assert letter_dict == {'a': 3, 'b': 1, 'c': 1, 'e': 4, 'g': 2, 'l': 2, 'n': 1, 'p': 3, 'r': 2, 'u': 1}

    def test_letter_pair_frequencies(self):
        """
        This tests the fucntion correclty identifies all the pairs beginning with the letter specified.
        """
        words = ['bagel', 'apple', 'bangs'] 
        letter = 'a'
        pair_dict = wordle_word_data.letter_pair_frequencies(words, letter)
        pair_dict = {pair: pair_dict[pair] for pair in pair_dict if pair_dict[pair] != 0}        
        assert pair_dict == {'g': 1, 'n': 1, 'p': 1}

    def test_letter_pair_frequencies_total(self):
        """
        This test checks the function correctly identifies all the pairs of letters.
        """
        words = ['bagel', 'bangs']
        pair_dict = wordle_word_data.most_common_pairs_total(words)
        pair_dict = {pair: pair_dict[pair] for pair in pair_dict if pair_dict[pair] != 0}      
        assert pair_dict == {'ba': 2, 'ag': 1, 'ge': 1, 'el': 1, 'an': 1, 'ng': 1, 'gs': 1}
        
    def test_frequency_of_letter_in_pos(self):
        """
        This test checks the function correctly identifies the frequencies of a given letter in different positions.
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        letter = 'e'
        pos_dict = wordle_word_data.frequency_of_letter_in_pos(words, letter)
        pos_dict = {pos: pos_dict[pos] for pos in pos_dict if pos_dict[pos] != 0}
        assert pos_dict == {'4': 1, '5': 3}

    def test_frequency_of_letter_in_pos_total(self):
        """
        This test checks the function correctly identifies the frequencies of all letters in different positions.
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        pos_dict = wordle_word_data.frequency_of_letter_in_pos_total(words)
        pos_dict = {pos: pos_dict[pos] for pos in pos_dict if pos_dict[pos] != 0}
        assert pos_dict == {'a1': 1, 'a2': 1, 'a3': 1, 'b1': 1, 'c1': 1, 'e4': 1, 'e5': 3, 'g3': 1, 'g4': 1, 'l4': 1, 'l5': 1, 'n4': 1, 'p1': 1, 'p2': 1, 'p3': 1, 'r2': 1,  'r3': 1, 'u2': 1}

    def test_frequency_of_word_structure(self):
        """
        This checks the function correctly identifies the frequencies of different word structures.
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        structure_dict = wordle_word_data.frequency_of_word_structure(words)
        structure_dict = {structure: structure_dict[structure] for structure in structure_dict if structure_dict[structure] != 0}
        assert structure_dict == {'cvcvc': 1, 'vcccv': 1, 'cvccv': 1, 'ccvcv': 1}

    def test_get_letter_occurences(self):
        """
        This test checks the letter count function works correctly.
        """
        word = 'spree'
        letter_dict = wordle_word_data.get_letter_occurences(word)
        assert letter_dict == {'s': 1, 'p': 1, 'r': 1, 'e': 2}

    def test_frequency_of_letter_variety(self):
        """
        This test checks the function correctly identifies the number of unique letters in each word.
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        variety_dict = wordle_word_data.frequency_of_letter_variety(words)
        assert variety_dict == {'bagel': 5, 'apple': 4, 'crane': 5, 'purge': 5}


    def test_prob_of_letter(self):
        """
        This test checks the probability function works and its values are between 0 and 1.
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        prob_of_letter_dict = wordle_word_data.prob_of_letter(words)
        prob_of_letter_dict = {letter: prob_of_letter_dict[letter] for letter in prob_of_letter_dict if prob_of_letter_dict[letter] != 0}
        assert prob_of_letter_dict == {'a': 0.15, 'b': 0.05, 'c': 0.05, 'e': 0.2, 'g': 0.1, 'l': 0.1, 'n': 0.05, 'p': 0.15, 'r': 0.1, 'u': 0.05}

    def test_prob_of_position(self):
        """
        This test checks the probability of positions function works and its values are between 0 and 1.
        """
        words = ['bagel', 'libel']
        prob_of_position_dict = wordle_word_data.prob_of_position(words)
        prob_of_position_dict = {pos: prob_of_position_dict[pos] for pos in prob_of_position_dict if prob_of_position_dict[pos] != 0}
        assert prob_of_position_dict == {'b1': 0.5, 'a2': 0.5, 'g3': 0.5, 'e4': 1.0, 'l5': 1.0, 'l1': 0.5, 'i2': 0.5, 'b3': 0.5}

    def test_prob_of_pairs(self):
        """
        This test checks the probability of pairs function works and its values are between 0 and 1.
        """
        words = ['bagel', 'label']
        prob_of_pairs_dict = wordle_word_data.prob_of_pairs(words)
        prob_of_pairs_dict = {pair: prob_of_pairs_dict[pair] for pair in prob_of_pairs_dict if prob_of_pairs_dict[pair] != 0}
        assert prob_of_pairs_dict == {'ba': 0.125, 'ag': 0.125, 'ge': 0.125, 'el': 0.25, 'la': 0.125, 'ab': 0.125, 'be': 0.125}

    def test_prob_of_structure(self):
        """
        This test checks the probability of word structure function works and its values are between 0 and 1.
        """
        words = ['bagel', 'apple', 'crane', 'crime']
        prob_of_structure_dict = wordle_word_data.prob_of_structure_score(words)
        prob_of_structure_dict = {structure: prob_of_structure_dict[structure] for structure in prob_of_structure_dict if prob_of_structure_dict[structure] != 0}
        assert prob_of_structure_dict == {'apple': 0.25, 'bagel': 0.25, 'crane': 0.5, 'crime': 0.5}

    def test_prob_of_letter_variety(self):
        """
        This test checks the probability of letter varieties function works and its values are between 0 and 1.
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        prob_of_variety_dict = wordle_word_data.prob_of_letter_variety(words)
        prob_of_variety_dict = {variety: prob_of_variety_dict[variety] for variety in prob_of_variety_dict if prob_of_variety_dict[variety] != 0}
        assert prob_of_variety_dict == {4: 0.25, 5: 0.75}

    def test_word_score_method_weighted_linear(self):
        """
        This test checks the best guess is appropriately returned and scored. 
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        best_guess = wordle_word_data.word_score_method_weighted_linear(words)
        assert best_guess == 'apple'

    def test_word_score_method_weighted_proportional(self):
        """
        This test checks the best guess is appropriately returned and scored. 
        """
        words = ['bagel', 'apple', 'crane', 'purge']
        best_guess = wordle_word_data.word_score_method_weighted_proportional(words)
        assert best_guess == 'purge'

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
        """
        This test checks duplicate letters are marked correctly.

        For example, if 'CHEER' was the guess and 'SMERE', the feedback should return 'BBYYB'.

        As there exists multiple 'E's in different conditions, they should be marked correctly. 
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape', 'crane', 'freer', 'drier']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('freer', 'drier')
        assert feedback == 'BGBGG'

    def test_feedback_all_blacks(self):
        """
        This test checks appropriate feedback for non-existent letters in the guess compared to answer.

        If the guess and the answer share no common letters then the feedback should be 'BBBBB'.
        """
        word_list = ['apple', 'lemon', 'grape', 'kudzu', 'rarer', 'drape', 'crane', 'freer', 'drier']
        solver = WordleSolver(word_list)
        feedback = solver._generate_feedback('freer', 'kudzu')
        assert feedback == 'BBBBB'
        
    def test_wordle_solves_every_word_small_set(self):
        """
        This checks all words in a smaller subset can be guessed in under 6 guesses, as per the rules of Wordle.
        """
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
        """
        This tests all 2315 potential answers for Wordle and if they can be guessed in 6 or less attempts. If not, the test displays
        the word and fails.
        """
        word_list = word_collection.word_collect()
        solved = True
        for word in word_list:
            answer = word
            solver = play_wordle.auto_wordle(answer)
            if solver == None:
                solved = False
                print(answer)
            
        assert solved == True

        

    
    
        




