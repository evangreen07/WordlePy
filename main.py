import next_guess
import word_collection
import frequency

def initial_guess_linear():
    selection = word_collection.word_collect()
    return frequency.word_score_method_weighted_linear(selection)

def initial_guess_weighted_porportional():
    selection = word_collection.word_collect()
    return frequency.word_score_method_weighted_proportional(selection)


def wordle_solver():
    possible_words = next_guess.wordle_result()
    return