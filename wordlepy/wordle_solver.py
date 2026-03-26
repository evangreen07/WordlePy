from . import wordle_word_data
def initial_guess_linear(selection):
    """
    This function returns the most likely answer to Wordle using the linear testing method.

    It calculates word score based on the sum of several frequencies of statistics of each word.

    Parameters:
    - selection (list): a list of words 

    Returns: 
    - (str): the most likely answer with the given word list

    Raises:
    - ZeroDivisionError if the possible word list is empty
    - TypeError if selection is not a list
    """
    return wordle_word_data.word_score_method_weighted_linear(selection)

def initial_guess_weighted_porportional(selection):
    """
    This function acts the same as the 'inital_guess_linear' function except it uses a weighted proportional testing style.

    Rather than taking frequencies of the letters, pairs, structures etc, it takes the probabilities of them occuring.

    Each statistic calculated in the word_score_method_weighted_linear() is divided by the length of possible words

    The product of these probabilities is returned as a word's score.

    Parameters:
    - selection (list): the list of possible Wordle answers

    Returns:
    - (str): the best guess from the current word list

    Raises:
    - ZeroDivisionError if selection is an empty list
    - TypeError if selection is not a list
    """
    return wordle_word_data.word_score_method_weighted_proportional(selection)

class WordleSolver:
    def __init__(self, possible_words):
        """
        Initialiser method for WordleSolver class

        Parameters: 
        - possible_words (list): list of all possible words left after a given feedback filter

        Returns:
        None

        Raises
        - TypeError if not instantiated with a list
        """
        
        self.possible_words = possible_words
    
    def suggest_word(self):
        """
        This method returns best word given obtained from several probalistic calculations in wordle_word_data.py

        Parameters :
        - None

        Returns:
        - best guess (str): the most likely answer to Wordle 
        """
        best_guess = wordle_word_data.word_score_method_weighted_proportional(self.possible_words)
        return best_guess
    
    def process_feedback(self, guess, feedback):
        """
        This method calls the private _update_possible_words method which filters the possible words after a given feedback from a guess.

        Parameters:
        - guess (str): the guess suggested by suggest_word() method
        - feedback (str): the feedback provided by Wordle

        Returns:
        - None (filtered word list from called method)
        """
        self._update_possible_words(guess, feedback)

    def wordle_reset(self, reset_words):
        """
        This function resets the word list.

        Parameters:
        - reset_words (list): a list of words

        Returns:
        - None (updates 'possible_words' back to desired word list)
        """
        self.possible_words = reset_words

    def _update_possible_words(self, guess, feedback):
        """
        This function filters the possible words from a given guess and its feedback from Wordle.

        Parameters:
        - guess (str): a 5 letter word 
        - feedback (str): a 5 letter word composed of 'Y', 'G' and 'B'

        Returns:
        - None (re-assigns possible words to the filtered list)
        """
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
            valid_word = True
            for index in range(0, 5):
                if feedback[index] == "G" and word[index] != guess[index]:
                    valid_word = False
                    break
            if not valid_word:
                continue

            for index in range(0, 5):
                if feedback[index] == "Y" and word[index] == guess[index]:
                    valid_word = False
                    break

            if not valid_word:
                continue

            word_counts = {}
            for count in word:
                word_counts[count] = word_counts.get(count, 0) + 1

            for letter, count in min_counts.items():
                if word_counts.get(letter, 0) < count:
                    valid_word = False
                    break

            if not valid_word:
                continue

            for letter, count in max_counts.items():
                if word_counts.get(letter, 0) > count:
                    valid_word = False
                    break

            if valid_word:
                valid_words.append(word)

            self.possible_words = valid_words
    
    def _generate_feedback(self, guess, answer):
        """
        This method returns the feedback string of 'guess' from answer'

        - If the letter is in the word, but in the wrong position it gets assigned 'Y'
        - If the letter is exactly the same as in the answer it gets asdigned 'G'
        - If the letter is not in the word, it gets assigned 'B'

        Parameters:
        - guess (str): 5 letter word attempted by the user
        - answer (str): 5 letter word which the user tries to guess

        Returns:
        - feedback (str): 5 letter feedback string consisting of 'B', 'G' and 'Y' to signify the status of each letter in 'guess' 
        compared to 'answer'
        """
        if guess == answer:
            return 'GGGGG'
        
        feedback = ['B', 'B', 'B', 'B', 'B']
        letter_counts = {}
        for letter in answer:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

        for index in range(0, 5):
            if guess[index] == answer[index]:
                feedback[index] = 'G'
                letter_counts[answer[index]] -= 1

        for index in range(0, 5):
            if feedback[index] == 'B':  
                letter = guess[index]
                if letter in letter_counts and letter_counts[letter] > 0:
                    feedback[index] = 'Y'
                    letter_counts[letter] -= 1
        
        return ''.join(feedback)
    
    def _generate_all_possible_feedbacks(self, answer): 
        """
        This method returns all feedback patterns from an answer and the possible words.

        Args:
        - self
        - answer (str): a 5 letter word

        Returns:
        - probability_of_feedbacks (dict): a dictionary of feedback strings and their probabilities of occuring
        """
        possible_words = self.possible_words
        possible_feedbacks = {}
        for word in possible_words:
            feedback = self._generate_feedback(word, answer)
            possible_feedbacks[feedback] = possible_feedbacks.get(feedback, 0) + 1

        probability_of_feedbacks = {feedback: possible_feedbacks[feedback] / len(possible_words) for feedback in possible_feedbacks}
        return probability_of_feedbacks


