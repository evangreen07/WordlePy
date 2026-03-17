import word_collection
from wordle_solver import WordleSolver

def main():  
    """
    This function runs the interactive Wordle loop between the code and the user.
    
    It enters a while loop which begins by displaying:
    - The attempt number (starts at 1)
    - The number of possible words left after any given feedback
    - The next best word to prompt Wordle with, based on data collected in wordle_word_data.py
    Parameters: 
    - None

    Returns:
    - No specific return value as the game is contained in a while loop.
    """
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


def auto_wordle(answer):
    possible_words = word_collection.word_collect()
    solver = WordleSolver(possible_words)
    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        suggested_word = solver.suggest_word()
        feedback = solver._generate_feedback(suggested_word, answer)
          
        if feedback == 'GGGGG':
            return attempts
            
        possible_words = solver.process_feedback(suggested_word, feedback)

        attempts += 1
        
    if attempts > max_attempts and feedback != 'GGGGG':
        return

