def format_words_excluded(guess, code):
    letter_values = [[letter, status] for letter, status in zip(guess, code)]
    return [letter[0] for letter in letter_values if letter[1] == 'B']

def format_words_wrong_place(guess, code):
    letter_values = [[letter, status] for letter, status in zip(guess, code)]
    yellow_letters = [letter[0] + str(pos + 1) for pos, letter in enumerate(letter_values) if letter[1] == 'Y']
    return yellow_letters

def format_words_correct(guess, code):
    letter_values = [[letter, status] for letter, status in zip(guess, code)]
    green_letters = [letter[0] + str(pos + 1) for pos, letter in enumerate(letter_values) if letter[1] == 'G']
    return green_letters

def wordle_result(previous_guess, code, words):
    excluded = format_words_excluded(previous_guess, code)
    wrong_place = format_words_wrong_place(previous_guess, code)
    correct = format_words_correct(previous_guess, code)
    removed_words = []
    for word in words:
        for letter in excluded:
            if letter in word:
                removed_words.append(word)
                break

    words_after_1 = [word for word in words if word not in removed_words]

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
    return words_after_3


print(wordle_result('crane', 'BBYGG'))
    
