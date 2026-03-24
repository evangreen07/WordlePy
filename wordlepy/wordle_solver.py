from . import wordle_word_data
def initial_guess_linear(selection):
    """
    This function is the first output to the user when calling the WordlePy library, specifically, the WordleSolver class.

    The 'linear' part of this function refers to the type of test it uses to suggest the next best word. 
    
    Linear tests are calculated by taking the frequency of several word statistics and simply adding them together.
    
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

    Raises:
    - ZeroDivisionError if the possible word list is empty
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

    def _update_possible_words(self, guess, feedback):
        """
        This function 
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
        This method returns the 

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


