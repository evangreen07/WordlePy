import matplotlib.pyplot as plt
import itertools
from . import word_collection

def get_letter_dict():
    """
    This function returns a dictionary for each letter with all intial values of 0.

    Parameters:
    - None

    Yields:
    - (dict): dictionary of all letters from a-z as keys with values all equal to 0
    """
    return {
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

all_words = word_collection.word_collect()
def most_common_letter(words):
    """
    This function determines the most common letter in all the possible answers.

    It does this by iterating through each word in the answer and tracking which letters appear in each word.

    For example: 'creep':
    c: 1
    r: 1
    e: 2
    p: 1

    Parameters:
    - words (list): a list of 5 letter words 

    Returns:
    - (dict): a dictionary of letter (key) and number of total occurences (value), 'letter freq'
    """
    letter_freq = get_letter_dict()
    for word in words:
        for letter in word:
            letter_freq[letter] += 1
    
    return letter_freq

def graph_of_data(data):
    """
    This function creates a bar chart for any given data.

    The x-axis is the keys of the dictionary and the y-axis is the values of the keys.
    
    Parameters:
    - data (dict): a dictionary of letters/words and their respective scores/probabilities
    Returns:
    None
    """
    x_axis = [letter for letter in data]
    y_axis = [data[letter] for letter in data]
    fig, ax = plt.subplots()
    ax.bar(x_axis, y_axis, width=1, edgecolor="white", linewidth=0.7)
    plt.show()
    return 

def most_common_vowels(words):
    """
    This function evaluates the occurences of each vowel in the word list by returning only the vowel entries from most_common_letter

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - (dict) : dictionary of the instances of every vowel in 'words'
    """
    vowels = ['a','e','i','o','u']
    vowel_freq = most_common_letter(words)
    return {vowel: vowel_freq[vowel] for vowel in vowels}

def most_common_consonants(words):
    """
    This function finds the frequency of each letter in all the words in 'words'.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - consonant_freq (dict) : dictionary of the instances of every vowel in 'words'

    Raises:
    - TypeError if words is not a list
    """

    vowels = ['a','e','i','o','u']
    consonant_freq = most_common_letter(words)
    for vowel in vowels:
        consonant_freq.pop(vowel)
    return consonant_freq

def most_common_pairs_with_letter_first(words, letter):
    """
    This function finds the frequencies of all possible letter pairs from a given first letter.  

    Parameters:
    - words (list): list of words which could be the answer to Wordle
    - letter (str): a single letter 

    Returns:
    - letter_dict (dict): a dictionary containing the letter pairs and their respective number of occurences in 'words'

    Raises:
    - TypeError if 'words' is not a list
    - KeyError if 'letter' is not a single letter
    """
    letter_dict = get_letter_dict()
    condensed_words = [word for word in words if (letter in word) and (word.index(letter) != 4)]
    for word in condensed_words:
        for index in range(0, 4):
            if word[index] == letter:
                letter_dict[word[index + 1]] += 1
    
    return letter_dict

def most_common_pairs_total(words):
    """
    This function accumulates all the possible consecutive letter pairs of the alphabet, and their number of occurences in 'words'.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - word_pair_score (dict): a dictionary containing each word and its letter pairs

    Raises:
    - TypeError if words is not a list
    """
    letter_dict = get_letter_dict()
    pairs_with_letter_first = {letter : most_common_pairs_with_letter_first(words, letter) for letter in letter_dict}
    word_pairs = {}
    for letter_frequency_first in pairs_with_letter_first:
        for letter in pairs_with_letter_first[letter_frequency_first]:
            word_pairs.update({letter_frequency_first + letter : pairs_with_letter_first[letter_frequency_first][letter]})

    return word_pairs

def most_common_pair_score(words):
    """
    This function returns the score of each word from its 4 pairs of consecutive letters in each word in 'words'.

    For example, the word 'CRANE' would be scored by the frequency of: 'CR' + 'RA' + 'AN' + 'NE'. 

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - word_scores (dict): dictionary of each word and its score

    Raises:
    - TypeError if words is not a list
    """
    pair_dict = most_common_pairs_total(words)
    word_scores = {}
    for word in words:
        word_total = 0
        for index in range(0, 4):
            if word[index: index + 2] in pair_dict:
                word_total += pair_dict[word[index: index + 2]]
        word_scores.update({word: word_total})

    return word_scores

def frequency_of_letter_in_pos(words, letter):
    """
    This function returns the frequency of the positions of a given letter in every word in 'words'.

   Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - position_dict (dict): a dictionary of the occurences of a given letter in positions 1-5

    Raises:
    - TypeError if words is not a list
    """
    position_dict = {
        '1' : 0,
        '2' : 0,
        '3' : 0,
        '4' : 0,
        '5' : 0
    }
    condensed_words = [word for word in words if letter in word]
    for word in condensed_words:
        for index in range(0,5):
            if word[index] == letter:
                position_dict[str(index + 1)] += 1
    
    return position_dict

def frequency_of_letter_in_pos_total(words):
    """
    This function accummulates every letter and its position dictionary into a single dictionary.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - all_letter_positions (dict): a dictionary of all letters and their number of occurences in 'words;

    Raises:
    - TypeError if words is not a list
    """
    letter_dict = get_letter_dict()
    letter_positions = {letter : frequency_of_letter_in_pos(words, letter) for letter in letter_dict}
    all_letter_positions = {}
    for letter_pos in letter_positions:
        for pos in letter_positions[letter_pos]:
            all_letter_positions.update({letter_pos + pos: letter_positions[letter_pos][pos]})

    return all_letter_positions

def probability_of_letter_in_word(words, letter):
    """
    This function calculates the probability of a given letter in any word.

    It calculates it simply by dividing the number of words which include the letter at least once by the number of total words.

    Parameters
    - words (list): list of words which could be the answer to Wordle
    - letter (str): a single letter

    Returns:
    - (float): the probability of a given letter in 'words'

    Raises:
    - TypeError if words is not a list
    - KeyError if letter is not a single letter
    """
    return sum(1 for word in words if letter in word) / len(words)

def probability_of_letter_in_word_total(words):
    """
    This function accummulates all the probabilities of each letter occurring in 'words'.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns: 
    - (dict): a dictionary of the probability of each letter occuring in 'words'

    Raises:
    - TypeError if words is not a list
    """
    letter_dict = get_letter_dict()
    return {letter: probability_of_letter_in_word(words, letter) for letter in letter_dict}

def probability_of_pair_in_word(words):
    """
    This function calculates the probability of a pair of consecutive letters occurring in 'words'.

    It calculates this by dividing all the words that include a given pair by the number of total words.

    Parameters:    
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - condensed_pairs (dict): a dictionary of the probabilities of all pairs of consecutive letters

    Raises:
    - TypeError if words is not a list
    """
    condensed_pairs = {pair : most_common_pairs_total(words)[pair] / len(words) for pair in most_common_pairs_total(words) if most_common_pairs_total(words)[pair] != 0}
    return condensed_pairs

def frequency_of_same_letter_pair(words, letter):
    """
    This function returns a subset of the letter pairs frequency, it returns the number of occurences of the same letter twice. 

    Parameters:
    - words (list): list of words which could be the answer to Wordle
    - letter (str): a single letter

    Returns:
    - (int): given a letter, the number of occurences of the letter twice

    Raises:
    - TypeError if words is not a list
    """
    return most_common_pairs_total(words)[letter + letter]

def frequency_of_same_letter_total(words):
    """
    This function returns every frequency of all duplicate letter pairs.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - frequency_dict (dict): a dictionary of the occurences of all duplicate letter pairs

    Raises:
    - TypeError if words is not a list
    """
    letter_dict = get_letter_dict()
    frequency_dict = {letter: frequency_of_same_letter_pair(words, letter) for letter in letter_dict}
    return frequency_dict

def word_score_frequent_letters(words):
    """
    This function calculates the the score of words from their letter frequencies.

    A word is scores by the sum of the frequencies of each letter it contains in 'words'

    For example, the word CRANE', would have a  total score equal to the sum of the frequency of 'C', 'R', 'A', 'N' and 'E'.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns: 
    - word_scores (dict): a dictionary with all words and their respective letter frequency scores

    Raises:
    - TypeError if words is not a list
    """
    letter_frequencies = most_common_letter(words)
    word_scores = {}
    for word in words:
        word_total = 0
        for letter in word:
            word_total += letter_frequencies[letter]
        
        word_scores.update({word: word_total})
    
    return word_scores

def word_score_position_of_letter(words):
    """
    This function calculaetes the word score of a word from its frequency of letters in their positions in the word.

    For example, the word 'CRANE' would have a score equal to the sum of the frequency of:
    - 'C' in position 1
    - 'R' in position 2
    - 'A' in position 3
    - 'N' in position 4
    - 'E' in position 5

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - word_scores (dict): a dictionary of all words and their letter position frequency scores

    Raises:
    - TypeError if words is not a list
    """
    position_freq = frequency_of_letter_in_pos_total(words)
    word_scores = {}
    for word in words:
        word_total = 0
        enumerated = enumerate(word)
        for pos, letter in enumerated:
            word_total += position_freq[letter + str(pos + 1)]

        word_scores.update({word: word_total}) 


    return word_scores

def word_score_common_pairs(words):
    """
    This function calculates the word score from the frequency of consecutive letter pairs in each word.

    For example, the word 'CRANE' would have a score equal to the sum of the frequencies of:
    - 'CR'
    - 'RA'
    - 'AN'
    - 'NE'

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - word_scores (dict): a dictionary of all the words and their consecutive letter pair frequency scores

    Raises:
    - TypeError if words is not a list
    """
    pairs_freq = most_common_pairs_total(words)
    word_scores = {}
    for word in words:
        word_total = 0
        for index in range(0, 4):
            word_total += pairs_freq[word[index: index + 2]]
        
        word_scores.update({word: word_total})

    
    return word_scores

def get_combos():
    """
    This function generates all the combinations of vowels-consonant word structure a 5 letter word can take.

    It does this by calculating the Cartesian product of 'v' and 'c' and repeating the pattern until the combination is five letters long.

    Parameters:
    - None

    Yields:
    - combo_dict (dict): a dictionary of all combinaions with initial values of 0
    """
    combos = list(itertools.product(['v','c'], repeat=5))
    combo_dict = {}
    for combo in combos:
        combo_structure = '' 
        for value in combo:
            combo_structure += value

        combo_dict.update({combo_structure: 0})
    
    return combo_dict

def frequency_of_word_structure(words):
    """
    This function returns the frequency of all possible word structures a 5 letter word could take.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - combo_dict (dict): a dictionary with the frequencies of all word structures

    Raises:
    - TypeError if words is not a list
    """
    vowels = ['a','e','i','o','u']
    combo_dict = get_combos()
    for word in words:
        word_structure = ''
        for letter in word:
            if letter in vowels:
                word_structure += 'v'
            else:
                word_structure += 'c'

        combo_dict[word_structure] += 1

    return combo_dict

def get_word_structure(word):
    """
    This function returns the vowel-consonant composition of a given word.

    Parameters:
    - word (str): a 5 letter word

    Returns:
    - word_structure (str): a 5 letter string composed of 'v's and 'c's to identify vowels and consonants respectively

    Raises:
    - TypeError if word is not a string
    """
    vowels = ['a','e','i','o','u']
    word_structure = ''
    for letter in word:
        if letter in vowels:
            word_structure += 'v'
        else:
            word_structure += 'c'

    return word_structure

def frequency_of_word_structure_score(words):
    """
    This function returns the frequency of word structures in 'words'.

    If two different words have the same vowel-consonant composition, they are assigned the same score.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - (dict): a dictionary of the word and its frequency from its vowel-consonant composition 

    Raises:
    - TypeError if words is not a list
    """
    structure_dict = frequency_of_word_structure(words)
    return {word: structure_dict[get_word_structure(word)] for word in words}

def prob_of_structure_score(words):
    """
    This function returns the probability of a word structure.

    It is calculated by dividing the number of word of a given vowel-consonant composition by the number of total words.

    If two different words have the same composition, they are assigned the same score.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - (dict): a dictionary of the probabilities of each word composition

    Raises:
    - TypeError if words is not a list
    """
    frequency_of_word_structures = frequency_of_word_structure_score(words)
    return {word: frequency_of_word_structures[word] / len(words) for word in words}

def get_letter_occurences(word):
    """
    This function returns the number of occurences of a given letter in a word.

    Parameters:
    - word (str): a 5 letter word

    Returns:
    - (dict): a frequency dictionary of the number of occurences of each letter in the word

    Raises:
    - TypeError if word is not a string
    """
    return {letter : word.count(letter) for letter in word}

def frequency_of_letter_variety(words):
    """
    This function returns the number of unique letters of each word in 'words'.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - letter_variety_dict (dict): a dictionary of the number of unqiue letters in each word

    Raises:
    - TypeError if words is not a list
    """
    letter_variety_dict = {word: len(get_letter_occurences(word)) for word in words}
    return letter_variety_dict

def prob_of_letter_variety(words):
    """
    This function returns the probabiity of the number of unique letters in a word in 'words'.

    Let n be the number of unqiue letters in a word.

    It is calculated by dividing the number of words with n unique letters by the number of total words.

    Different words with the same amount of unique letters are assigned the same probability.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - probability_of_variety (dict): a dictionary of the probabilities of a word having n unique letters

    Raises:
    - TypeError if words is not a list
    """
    instances = [1, 2, 3, 4, 5]
    letter_varieties = frequency_of_letter_variety(words)
    probability_of_variety = {}
    for instance in instances:
        condensed_words = [word for word in words if letter_varieties[word] == instance]
        probability_of_variety.update({instance: len(condensed_words) / len(words)})
    
    return probability_of_variety

def prob_of_letter_variety_score(words):
    """
    This function returns the probability of each word from its letter variety.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - (dict): a dictionary of every word and its respective letter variety probability score

    Raises:
    - TypeError if words is not a list
    """
    letter_varieties = frequency_of_letter_variety(words)
    prob_of_variety = prob_of_letter_variety(words)
    return {word:  prob_of_variety[letter_varieties[word]] for word in words}

def frequency_of_letter_variety_score(words):
    """
    This function returns the frequency of each word fromm is letter variety. 

    It is calculated by the sum of the frequency of letter varieties in the given word.

    For example, 'CRANE' would be assigned the frequency of words with 5 unique letters.

    Different words of the same letter variety are assigned the same score.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - (dict): a dictionary of all words and their letter variety frequency score

    Raises:
    - TypeError if words is not a list
    """
    word_variety = frequency_of_letter_variety(words)
    return {word: word_variety[word] for word in words}

def word_score_method_weighted_linear(words):
    """
    This function returns the collective linear score of all words in 'words'.

    It calculates each score by the sum of:
    - letter frequencies
    - position frequencies
    - pair frequencies
    - word structure frequencies
    - letter variety frequencies

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    suggested_word[0] (str): the first (most likely) word out of 'words' for the answer to Wordle

    Raises:
    - TypeError if words is not a list
    - ZeroDivisionError if 'words' is empty
    """
    letter_freq = word_score_frequent_letters(words)
    position_freq = word_score_position_of_letter(words)
    pair_freq = most_common_pair_score(words)
    structure_freq = frequency_of_word_structure_score(words)
    variety_freq = frequency_of_letter_variety_score(words)
    collective_word_score = {word: letter_freq[word] + position_freq[word] + pair_freq[word] + structure_freq[word] + variety_freq[word] for word in words}
    suggested_word = max(collective_word_score.items(), key=lambda item : item[1])
    return suggested_word[0]

def prob_of_letter(words):
    """
    This function returns the probability that a letter is in any word.

    It calculates this by dividing the number of occurrences of a letter by the total number of letters. 

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - letter_prob (dict): a dictionary of letter probabilites 

    Raises:
    - TypeError if words is not a list
    """
    letter_dict = get_letter_dict()
    total_letters = len(words) * 5
    letter_prob = {letter : most_common_letter(words)[letter] / total_letters for letter in letter_dict}
    return  letter_prob

def prob_of_letter_score(words):
    """
    This function returns the probability score of a word from its letter probabilities.

    It is calculated by the product of the probabilities of each of its letters.

    For example, 'CRANE' would have a score equal to the probability of 'C' * 'R" * 'A' * 'N' * 'E'.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - probs (dict): a dictionary of word scores from their letter probability products

    Raises:
    - TypeError if words is not a list
    """
    prob_letter_dict = prob_of_letter(words)
    probs = {}
    for word in words:
        word_prob = 1
        for letter in word:
            word_prob *= prob_letter_dict[letter]
        
        probs.update({word: word_prob})
    return probs
        
def prob_of_position(words):
    """
    This function returns the probability of words from their letter positions. 

    It is calculated by dividing the number of words with the letter in a specified position by the total number of words.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - (dict): a dictionary of probability of a letter in a position

    Raises:
    - TypeError if words is not a list
    """
    pos_dict = frequency_of_letter_in_pos_total(words)
    return {pos : pos_dict[pos] / len(words) for pos in pos_dict}


def prob_of_position_score(words):
    """
    This function calculates the score of a word from is letter position probabilities.

    It is calculated by the product of the probability of each letter position. 

    For example, 'CRANE' would have a score equal to the product probability of:
    - 'C' in position 1
    - 'R' in position 2
    - 'A' in position 3
    - 'N' in position 4
    - 'E' in position 5

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - probs (dict): a dictionary of words and their scores from their letter position probabilities

    Raises:
    - TypeError if words is not a list
    """
    positions_dict = prob_of_position(words)
    probs = {}
    for word in words:
        word_prob = 1
        for pos, letter in enumerate(word):
            word_prob *= positions_dict[letter + str(pos + 1)]
        
        probs.update({word : word_prob})

    return probs

def prob_of_pairs(words):
    """
    This function returns the probability of consecutive letter pairs from 'words'.

    It is calculated by dividing the number of words with the pair included by the number of total pairs in 'words'.

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - (dict): a dictionary of pairs and their probabilities

    Raises:
    - TypeError if words is not a list
    """
    pair_dict = most_common_pairs_total(words)
    total_pairs = len(words) * 4
    return {pair: pair_dict[pair] / total_pairs for pair in pair_dict}

def prob_of_pairs_score(words):
    """
    This function returns the word score from the letter pair probailtiies.

    It is calculated by the product of the probability of each pair in the word.

    For example, 'CRANE' would have a score equal to the product probability of:
    - 'CR' 
    - 'RA'
    - 'AN'
    - 'NE'

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - prob_dict (dict): a dictionary with words and their letter pair probability scores

    Raises:
    - TypeError if words is not a list
    """
    pair_prob_dict = prob_of_pairs(words)
    prob_dict = {}
    for word in words:
        word_prob = 1
        for index in range(0, 4):
            word_prob *= pair_prob_dict[word[index: index + 2]]
        prob_dict.update({word: word_prob})

    return prob_dict

def word_score_method_weighted_proportional(words):
    """
    This function returns the best guess using the proportional approach to calculating word scores.

    It is calculated by the product of the following probabilities:
    - letter probability
    - letter position probability
    - consecutive letter pair probability
    - word structure probability
    - letter variety probability

    Parameters:
    - words (list): list of words which could be the answer to Wordle

    Returns:
    - suggested_word[0] (str): the first (most likely) answer for Wordle using the proportional data

    Raises:
    - TypeError if words is not a list
    - ZeroDivisionError if words is empty
    """
    letter_prob = prob_of_letter_score(words)
    position_prob = prob_of_position_score(words)
    pair_prob = prob_of_pairs_score(words)
    structure_prob = prob_of_structure_score(words)
    variety_prob = prob_of_letter_variety_score(words)
    collective_word_scores = {word: 1 * letter_prob[word] * position_prob[word] * pair_prob[word] * structure_prob[word] * variety_prob[word] for word in words}
    suggested_word = max(collective_word_scores.items(), key=lambda item : item[1])
    return suggested_word[0]


