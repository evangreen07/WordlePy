import wordle_word_data

def initial_guess_linear(selection):
    """
    This function is the first output to the user when calling the WordlePy library, specifically, the WordleSolver class.

    The 'linear' part of this function is the type of test it uses to suggest the next best word. 
    
    Linear test is calculated by taking the frequency of several word statistics and simply adding them together.
    
    A word's score is the sum of all these tests. For example:

    The word 'eerie':
    - Has 3 'e's, 1 'r' and 1 'i'
    - Has pairs of letters, 'ee', 'er', 'ri', 'ie'
    - Follows a vowel-vowel-consonant-vowel-vowel word structure

    The data gathered in wordle_word_data shows that in all words, 'e' occurs 1233 times, 'r' has 899 and 'i' has 671.
    
    Therefore its cumulative score from just this test is the sum of all these frequencies of 5269. (3 * 1233) + 899 + 671.

    Parameters:
    - selection, this is the current word list which is filtered after each incorrect guess. (where the feedback is not 'GGGGG')

    Returns:
    - The next best guess using the linear testing format in wordle_word_data.py
    """
    return wordle_word_data.word_score_method_weighted_linear(selection)

def initial_guess_weighted_porportional(selection):
    """
    This function acts the same as the 'inital_guess_linear' function except it uses a weighted proportional testing style.

    Rather than taking frequencies of the letters, pairs, structures etc, it takes the probabilities of them occuring.

    Take 'eerie' as an example:
    - Letter 'e'
    """
    return wordle_word_data.word_score_method_weighted_proportional(selection)

class WordleSolver:
    def __init__(self, possible_words):
        self.possible_words = possible_words
    
    def suggest_word(self):
        return wordle_word_data.word_score_method_weighted_linear(self.possible_words)
    
    def process_feedback(self, guess, feedback):
        self._update_possible_words(guess, feedback)

    def _update_possible_words(self, guess, feedback):
        #black_letters = self._format_words_excluded(guess, feedback)
        #yellow_letters = self._format_words_wrong_place(guess, feedback)
        #green_letters = self._format_words_correct(guess, feedback)   
        # valid_words = []     
        # min_counts = {}
        # for i in range(0, 5):
        #     letter = guess[i]
        #     if feedback[i] in ("G", "Y"):
        #         if letter not in min_counts:
        #             min_counts[letter] = 0
        #         min_counts[letter] += 1

        # max_counts = {}

        # for i in range(0, 5):
        #     letter = guess[i]
        #     if feedback[i] == "B":
        #         if letter in min_counts:
        #             max_counts[letter] = min_counts[letter]
        #         else:
        #             max_counts[letter] = 0

        # for word in self.possible_words:
        #     valid_word = True
        #     for i in range(len(guess)):
        #         if feedback[i] == "G":
        #             if word[i] != guess[i]:
        #                 valid_word = False
        #                 break
        #     if not valid_word:
        #         continue
        #     for i in range(0, 5):
        #         if feedback[i] == "Y":
        #             letter = guess[i]

        #             if word[i] == letter:
        #                 valid_word = False
        #                 break

        #             if letter not in word:
        #                 valid_word = False
        #                 break

        #     if not valid_word:
        #         continue

        #     word_counts = self._letter_counter(word)

        #     for letter in min_counts:
        #         if word_counts.get(letter, 0) < min_counts[letter]:
        #             valid_word = False
        #             break

        #     if not valid_word:
        #         continue

        #     for letter in max_counts:
        #         if word_counts.get(letter, 0) > max_counts[letter]:
        #             valid_word = False
        #             break

        # if valid_word:
        #     valid_words.append(word)
        
    
        # self.possible_words = valid_words
            
        min_counts = {}
        max_counts = {}

        for index in range(0, 5):
            if feedback[index] in ("G", "Y"):
                letter = guess[index]
                min_counts[letter] = min_counts.get(letter, 0) + 1

        for index in range(0, 5):
            letter = guess[index]
            if feedback[index] == "B":
                if letter in min_counts:
                    max_counts[letter] = min_counts[letter]
                else:
                    max_counts[letter] = 0
        valid_words = []

        for word in self.possible_words:
            valid = True
            for index in range(0, 5):
                if feedback[index] == "G" and word[index] != guess[index]:
                    valid = False
                    break
            if not valid:
                continue

            for index in range(0, 5):
                if feedback[index] == "Y" and word[index] == guess[index]:
                    valid = False
                    break

            if not valid:
                continue

            word_counts = {}
            for c in word:
                word_counts[c] = word_counts.get(c, 0) + 1

            for letter, count in min_counts.items():
                if word_counts.get(letter, 0) < count:
                    valid = False
                    break

            if not valid:
                continue

            for letter, count in max_counts.items():
                if word_counts.get(letter, 0) > count:
                    valid = False
                    break

            if valid:
                valid_words.append(word)

            self.possible_words = valid_words
        #words_after_green_check = [word for word in self.possible_words if word not in removed_words]

        #removed_words = []

        #for word in words_after_green_check:
         #   word_positions = [letter + str(pos + 1) for pos, letter in enumerate(word)]
          #  for y in yellow_letters:
           #     letter = y[0]
            #    pos = int(y[1]) - 1
               # if word[pos] == letter or letter not in word:
                #    removed_words.append(word)
        
        #words_after_yellow_check = [word for word in words_after_green_check if word not in removed_words]

        #removed_words = []
        
        #for word in words_after_yellow_check:
         #   for letter in black_letters:
         #       if letter[0] in word:
         #           removed_words.append(word)
         #           break
        #words_after_black_check = [word for word in words_after_yellow_check if word not in removed_words]

        #removed_words = []


    
    # def _format_words_excluded(self, guess, feedback):
    #     letter_values = [[letter, status] for letter, status in zip(guess, feedback)]
    #     return [letter[0] for letter in letter_values if letter[1] == 'B']

    # def _format_words_wrong_place(self, guess, feedback):
    #     letter_values = [[letter, status] for letter, status in zip(guess, feedback)]
    #     yellow_letters = [(letter[0], pos + 1) for pos, letter in enumerate(letter_values) if letter[1] == 'Y']
    #     return yellow_letters

    # def _format_words_correct(self, guess, feedback):
    #     letter_values = [[letter, status] for letter, status in zip(guess, feedback)]
    #     green_letters = [(letter[0], pos + 1) for pos, letter in enumerate(letter_values) if letter[1] == 'G']
    #     return green_letters
    
    