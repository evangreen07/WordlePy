import word_collection
import frequency

def initial_guess():
    selection = word_collection.word_collect()
    return frequency.word_score_method_weighted_linear(selection)




def wordle_result(previous_guess, code):
    words = ['apple', 'crane', 'pilot', 'hairy', 'kudzu']
    excluded = ['a', 'f', 'd']
    words_after = []
    for word in words:
        accept = True
        for letter in excluded:
            if letter in word:
                accept = False
                break

        if accept:
            words_after.append(word)

    return words_after

def reduce_dict(words, letter):
    return [word for word in words if letter not in word]

print(wordle_result('crane', 'BBYGG'))
    
