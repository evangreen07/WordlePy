import word_collection
from wordle_solver import WordleSolver

def main():  
    possible_words = word_collection.word_collect()
    solver = WordleSolver(possible_words)
    attempts = 1
    max_attempts = 6
    
    while attempts <= max_attempts:
        print(f'Attempt {attempts} / {max_attempts}')
        print(f'Words remaining: {len(solver.possible_words)}')
        suggested_word = solver.suggest_word()
        print(f'Most likely guess: {suggested_word}')

        feedback = input('Enter feedback or Q to quit: ').strip().upper()
        if feedback == 'Q':
            break
            
        if len(feedback) != 5 or not all(feedback_char in 'GYB' for feedback_char in feedback):
            print('Invalid')
            continue
            
        if feedback == 'GGGGG':
            print(f'{suggested_word} is correct: {attempts} attempt(s)')
            break
            
        possible_words = solver.process_feedback(suggested_word, feedback)

        attempts += 1
        
    if attempts > max_attempts and feedback != 'GGGGG':
        print('Fail')

if __name__ == "__main__":
    main()


