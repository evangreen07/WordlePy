import word_collection
from wordle_solver import WordleSolver

def main():  
    possible_words = word_collection.word_collect()
    solver = WordleSolver(possible_words)
    attempts = 1
    max_attempts = 6
    
    while attempts <= max_attempts:
        print(f'\n--- Attempt {attempts} / {max_attempts} ---')
        print(f'Possible words remaining: {len(solver.possible_words)}')
        
        suggested_word = solver.suggest_word()

        print(f'Next best guess: {suggested_word}')

        feedback = input('Enter the feedback from Wordle (or Q to quit): ').strip().upper()

        
        if feedback == 'Q':

            break
            
        if len(feedback) != 5 or not all(c in 'BYG' for c in feedback):
            print('Invalid input')
            continue
            
        if feedback == 'GGGGG':
            print(f'\nSuccess! The word was {suggested_word}. Found in {attempts} attempt(s).')
            break
            
        possible_words = solver.process_feedback(suggested_word, feedback)
        
        attempts += 1
        
    if attempts > max_attempts and feedback != 'GGGGG':
        print('\n Fail')

if __name__ == "__main__":
    main()


