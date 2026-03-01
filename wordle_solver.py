import next_guess
import word_collection
import frequency

def initial_guess_linear():
    selection = word_collection.word_collect()
    return frequency.word_score_method_weighted_linear(selection)

def initial_guess_weighted_porportional():
    selection = word_collection.word_collect()
    return frequency.word_score_method_weighted_proportional(selection)

class WordleSolver:
    def __init__(self, possbile_words):
        self.possile_words = possbile_words

    def suggest_word(self):
        return self.possile_words[0]
    
    def process_feedback(self, guess, feedback):
        self._update_possible_words(guess, feedback)

    def _update_possible_words(self, guess, feedback):
        excluded = self._format_words_excluded(guess, feedback)
        wrong_place = self._format_words_wrong_place(guess, feedback)
        correct = self._format_words_correct(guess, feedback)
        removed_words = []
        for word in self.possile_words:
            for letter in excluded:
                if letter in word:
                    removed_words.append(word)
                    break

        words_after_1 = [word for word in self.possile_words if word not in removed_words]

        for word in words_after_1:
            for pos, letter in enumerate(word):
                if (letter + str(pos + 1)) in wrong_place:
                    removed_words.append(word)
                    break

        
        words_after_2 = [word for word in words_after_1 if word not in removed_words]

        for word in words_after_2:
            word_positions = [letter + str(pos + 1) for pos, letter in enumerate(word)]
            correct_count = 0
            for c in correct:
                if c in word_positions:
                    correct_count += 1
            
            if correct_count != len(correct):
                removed_words.append(word)


        
        words_after_3 = [word for word in words_after_2 if word not in removed_words]
        self.possile_words = words_after_3
    
    
    
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