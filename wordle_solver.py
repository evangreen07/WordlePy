import frequency

def initial_guess_linear(selection):
    return frequency.word_score_method_weighted_linear(selection)

def initial_guess_weighted_porportional(selection):
    return frequency.word_score_method_weighted_proportional(selection)

class WordleSolver:
    def __init__(self, possible_words):
        self.possible_words = possible_words
    
    def suggest_word(self):
        return initial_guess_linear(self.possible_words)
    
    def process_feedback(self, guess, feedback):
        self._update_possible_words(guess, feedback)

    def _update_possible_words(self, guess, feedback):
        black_letters = self._format_words_excluded(guess, feedback)
        yellow_letters = self._format_words_wrong_place(guess, feedback)
        green_letters = self._format_words_correct(guess, feedback)
        removed_words = []

        for letter in yellow_letters:
            if letter[0] in black_letters:
                black_letters.remove(letter[0])


        for word in self.possible_words:
            word_positions = [letter + str(pos + 1) for pos, letter in enumerate(word)]
            correct_count = 0
            for c in green_letters:
                if c in word_positions:
                    correct_count += 1
            
            if correct_count != len(green_letters):
                removed_words.append(word)

        words_after_green_check = [word for word in self.possible_words if word not in removed_words]

        for word in words_after_green_check:
            for pos, letter in enumerate(word):
                if (letter + str(pos + 1)) in yellow_letters:
                    removed_words.append(word)
                    break

        
        words_after_yellow_check = [word for word in words_after_green_check if word not in removed_words]

        for word in words_after_yellow_check:
            for letter in black_letters:
                if letter[0] in word:
                    removed_words.append(word)
                    break
        words_after_black_check = [word for word in words_after_yellow_check if word not in removed_words]

        self.possible_words = words_after_black_check
    
    def _format_words_excluded(self, guess, feedback):
        letter_values = [[letter, status] for letter, status in zip(guess, feedback)]
        return [letter[0] for letter in letter_values if letter[1] == 'B']

    def _format_words_wrong_place(self, guess, feedback):
        letter_values = [[letter, status] for letter, status in zip(guess, feedback)]
        yellow_letters = [letter[0] + str(pos + 1) for pos, letter in enumerate(letter_values) if letter[1] == 'Y']
        return yellow_letters

    def _format_words_correct(self, guess, feedback):
        letter_values = [[letter, status] for letter, status in zip(guess, feedback)]
        green_letters = [letter[0] + str(pos + 1) for pos, letter in enumerate(letter_values) if letter[1] == 'G']
        return green_letters