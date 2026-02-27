import matplotlib.pyplot as plt
import itertools
import word_collection

def get_letter_dict():
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
    ----------
    List of words, 'words'

    Returns:
    -------
    Dictionary of letter (key) and number of total occurences (value), 'letter freq'
    """
    letter_freq = get_letter_dict()
    for word in words:
        for letter in word:
            letter_freq[letter] += 1
    
    return letter_freq

def graph_of_data(data):
    x_axis = [letter for letter in data]
    y_axis = [data[letter] for letter in data]
    fig, ax = plt.subplots()
    ax.bar(x_axis, y_axis, width=1, edgecolor="white", linewidth=0.7)
    plt.show()
    return 

number_of_instances = most_common_letter(all_words)
#graph_of_data(number_of_instances)

def most_common_vowels(words):
    vowels = ['a','e','i','o','u']
    vowel_freq = most_common_letter(words)
    return {vowel: vowel_freq[vowel] for vowel in vowels}
#graph_of_data(most_common_vowels(all_words))

def most_common_consonants(words):
    vowels = ['a','e','i','o','u']
    consonant_freq = most_common_letter(words)
    for vowel in vowels:
        consonant_freq.pop(vowel)
    return consonant_freq
#graph_of_data(most_common_consonants(all_words))

def most_common_pairs_with_letter_first(words, letter):
    letter_dict = get_letter_dict()
    condensed_words = [word for word in words if (letter in word) and (word.index(letter) != 4)]
    for word in condensed_words:
        for index in range(0, 4):
            if word[index] == letter:
                letter_dict[word[index + 1]] += 1
    
    return letter_dict


def most_common_pairs_with_letter_last(words, letter):
    letter_dict = get_letter_dict()
    condensed_words = [word for word in words if (letter in word) and (word.index(letter) != 0)]
    for word in condensed_words:
        for index in range(1, 5):
            if word[index] == letter:
                letter_dict[word[index - 1]] += 1
    
    return letter_dict

def most_common_pairs_total(words):
    letter_dict = get_letter_dict()
    pairs_with_letter_first = {letter : most_common_pairs_with_letter_first(words, letter) for letter in letter_dict}
    #pairs_with_letter_last = {letter : most_common_pairs_with_letter_last(words, letter) for letter in letter_dict}
    graph_form = {}
    for letter_frequency_first in pairs_with_letter_first:
        for letter in pairs_with_letter_first[letter_frequency_first]:
            graph_form.update({letter_frequency_first + letter : pairs_with_letter_first[letter_frequency_first][letter]})

    return graph_form

def most_common_pair_score(words):
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
    letter_dict = get_letter_dict()
    letter_positions = {letter : frequency_of_letter_in_pos(words, letter) for letter in letter_dict}
    graph_form = {}
    for letter_pos in letter_positions:
        for pos in letter_positions[letter_pos]:
            graph_form.update({letter_pos + pos: letter_positions[letter_pos][pos]})

    return graph_form

#graph_of_data(frequency_of_letter_in_pos_total(all_words))

def probability_of_letter_in_word(words, letter):
    return sum(1 for word in words if letter in word) / len(words)

def probability_of_letter_in_word_total(words):
    letter_dict = get_letter_dict()
    return {letter: probability_of_letter_in_word(words, letter) for letter in letter_dict}

#graph_of_data(probability_of_letter_in_word_total(all_words))

def probability_of_pair_in_word(words):
    condensed_pairs = {pair : most_common_pairs_total(words)[pair] / len(words) for pair in most_common_pairs_total(words) if most_common_pairs_total(words)[pair] != 0}
    return condensed_pairs

def frequency_of_same_letter_pair(words, letter):
    return most_common_pairs_total(words)[letter + letter]

def frequency_of_same_letter_total(words):
    letter_dict = get_letter_dict()
    frequency_dict = {letter: frequency_of_same_letter_pair(words, letter) for letter in letter_dict}
    return frequency_dict

#graph_of_data(frequency_of_same_letter_total(all_words))

def word_score_frequent_letters(words):
    letter_frequencies = most_common_letter(words)
    word_scores = {}
    for word in words:
        word_total = 0
        for letter in word:
            word_total += letter_frequencies[letter]
        
        word_scores.update({word: word_total})
    
    return word_scores

def word_score_position_of_letter(words):
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
    pairs_freq = most_common_pairs_total(words)
    word_scores = {}
    for word in words:
        word_total = 0
        for index in range(0, 4):
            word_total += pairs_freq[word[index: index + 2]]
        
        word_scores.update({word: word_total})

    
    return word_scores

def get_combos():
    combos = list(itertools.product(['v','c'], repeat=5))
    combo_dict = {}
    for combo in combos:
        combo_structure = '' 
        for value in combo:
            combo_structure += value

        combo_dict.update({combo_structure: 0})
    
    return combo_dict

def frequency_of_word_structure(words):
    vowels = ['a','e','i','o','u']
    combo_list = get_combos()
    for word in words:
        word_structure = ''
        for letter in word:
            if letter in vowels:
                word_structure += 'v'
            else:
                word_structure += 'c'

        combo_list[word_structure] += 1

    return combo_list

def get_word_structure(word):
    vowels = ['a','e','i','o','u']
    word_structure = ''
    for letter in word:
        if letter in vowels:
            word_structure += 'v'
        else:
            word_structure += 'c'

    return word_structure

def frequency_of_word_structure_score(words):
    structure_dict = frequency_of_word_structure(words)
    return {word: structure_dict[get_word_structure(word)] for word in words}

def get_letter_occurences(word):
    return {letter : word.count(letter) for letter in word}

def frequency_of_letter_variety(words):
    letter_variety_dict = {word: len(get_letter_occurences(word)) for word in words}
    return letter_variety_dict

def probability_of_letter_variety(words):
    instances = [1, 2, 3, 4, 5]
    letter_varieties = frequency_of_letter_variety(words)
    probability_of_variety = {}
    for instance in instances:
        condensed_words = [word for word in words if letter_varieties[word] == instance]
        probability_of_variety.update({instance: len(condensed_words) / len(words)})
    
    return probability_of_variety

def frequency_of_letter_variety_score(words):
    word_variety = frequency_of_letter_variety(words)
    return {word: word_variety[word] for word in words}


#graph_of_data(frequency_of_word_structure(all_words))


def word_score_method_weighted_linear(words):
    letter_freq = word_score_frequent_letters(words)
    position_freq = word_score_position_of_letter(words)
    pair_freq = most_common_pair_score(words)
    structure_freq = frequency_of_word_structure_score(words)
    variety_freq = frequency_of_letter_variety_score(words)
    collective_word_score = {word: letter_freq[word] + position_freq[word] + pair_freq[word] + structure_freq[word] + variety_freq[word] for word in words}

    return max(collective_word_score.items(), key=lambda item : item[1])



def prob_of_letter(words):
    letter_dict = get_letter_dict()
    total_letters = len(words) * 5
    letter_freq = {letter : most_common_letter(words)[letter] / total_letters for letter in letter_dict}
    return  letter_freq

def prob_of_letter_score(words):
    prob_letter_dict = prob_of_letter(words)
    probs = {}
    for word in words:
        word_prob = 1
        for letter in word:
            word_prob *= prob_letter_dict[letter]
        
        probs.update({word: word_prob})
    return probs
        
def prob_of_position(words):
    pos_dict = frequency_of_letter_in_pos_total(words)
    return {pos : pos_dict[pos] / len(words) for pos in pos_dict}


def prob_of_position_score(words):
    positions_dict = prob_of_position(words)
    probs = {}
    for word in words:
        word_prob = 1
        for pos, letter in enumerate(word):
            word_prob *= positions_dict[letter + str(pos + 1)]
        
        probs.update({word : word_prob})

    return probs

#print(prob_of_position_score(all_words))

def prob_of_pairs(words):
    pair_dict = most_common_pairs_total(words)
    total_pairs = len(words) * 4
    return {pair: pair_dict[pair] / total_pairs for pair in pair_dict}


def prob_of_pairs_score(words):


    
    return

#print(prob_of_pairs(all_words))

def word_score_method_weighted_proportial(words):

    return
    


#print(word_score_method_1(all_words))

