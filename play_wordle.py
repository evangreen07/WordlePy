import word_collection
from wordle_solver import WordleSolver
import next_guess


def filter_words(words, guess, feedback):
    """
    Filters the list of possible words based on Wordle feedback.
    Feedback characters:
        B: Black (letter not in word)
        Y: Yellow (letter in word, wrong position)
        G: Green (letter in correct position)
    """
    filtered = []
    for word in words:
        if len(word) != 5:
            continue
            
        match = True
        for i in range(5):
            g_char = guess[i]
            f_char = feedback[i]
            
            if f_char == 'G':
                if word[i] != g_char:
                    match = False
                    break
            elif f_char == 'Y':
                if g_char not in word or word[i] == g_char:
                    match = False
                    break
            elif f_char == 'B':
                has_other_occurrence = False
                for j in range(5):
                    if i != j and guess[j] == g_char and feedback[j] in ('G', 'Y'):
                        has_other_occurrence = True
                        
                if has_other_occurrence:
                    if word[i] == g_char:
                        match = False
                        break
                else:
                    if g_char in word:
                        match = False
                        break
        
        if match:
            filtered.append(word)
            
    return filtered

print(filter_words(word_collection.word_collect(), 'crane', 'BYGBY'))


def main():  
    possible_words = word_collection.word_collect()
    solver = WordleSolver()
    attempts = 1
    max_attempts = 6
    
    while attempts <= max_attempts:
        
        feedback = input("Enter the feedback from Wordle (or 'Q' to quit): ").strip().upper()
        
        if feedback == 'Q':
            print("Exiting...")
            break
            
        if len(feedback) != 5 or not all(c in 'BYG' for c in feedback):
            print("Invalid input! Please enter exactly 5 characters using B, Y, and G.")
            continue
            
        if feedback == 'GGGGG':
            print(f"\nSuccess! The word was {suggested_word.upper()}. Found in {attempts} attempt(s).")
            break
            
        # Update state by filtering down our worldlist
        possible_words = next_guess.filter_words(possible_words, suggested_word, feedback)
        
        attempts += 1
        
    if attempts > max_attempts and feedback != 'GGGGG':
        print("\nBetter luck next time! Reached the maximum number of attempts.")

if __name__ == "__main__":
    main()


