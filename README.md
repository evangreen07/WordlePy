# WordlePy

A python library for minimising the number of attempts to guess the answer to Wordle 

## Tutorial

Wordle is a free game in which you have 6 attempts to guess a 5 letter word. After each submitted guess, the game will hint towards the correct word based on the letters in your latest guess. 

Let's play a game of Wordle, if the answer (which is normally unknown) is **SHADE**, and your first guess is **SPIED**, the game would return:

- A green tile for 'S' as both your answer and guess share it as their first letter
- A black tile for 'P' as it is not in the answer at all
- A black tile for 'I'
- A yellow tile for 'E' as the answer contains an 'E', yet the position of 'E' in your guess is not the same as in the answer. 
- A yellow tile for 'D'

Thus, are feedback from Wordle is **GBBYY**, ('G', 'Y' and 'B' are shorthand for 'green tile', 'yellow tile' and 'black tile' respectively). Let's try another word which satisfies these conditions, such as **SHAME**. This is a good second guess as:

- It satisfies the condition of an 'S' as the first letter
- It does not contain either 'P' or 'I' 
- It contains both 'A' and 'E', but not in the same positions as our previous guess
- It tries letters 'H' and 'M' which we currently have no knowledge about

This returned a feedback of **GGGBG**, which implies were are only wrong by one letter. Next, let's try **SHADE**, which returned **GGGGG**, meaning our guess and the answer are the same, so we have won the game. 

This process can repeat for a maximum of 6 times, if a user guesses the correct word at any point, the game ends and they are rewarded with a number of points to their Wordle account based on the number of attempts it took for the user to guess the answer. 

If the user fails to guess the correct word in 6 or fewer attempts, the game ends, and the user is awarded no points. 

The point system is a feature of the online Wordle game  and is not a feature of this library. 

## How to Guide

Use this library when playing a game of Wordle. 

### How to use WordlePy
Import the library
```
>>> from wordlepy import WordleSolver, word_collect
```
- `WordleSolver` is a class encapsulating several probabilistic functions 
- `word_collect` is a list containing all possible Wordle answers 

Instantiate the `WordleSolver` class with a list of possible words.
```
>>> words = word_collect()
>>> solver = WordleSolver(words)
```
Retrieve the best guess using `suggest_word()`
```
>>> best_guess = solver.suggest_word()
```
Feed `best_guess` into Wordle

Call `process_feedback(best_guess, feedback)` where `feedback` is the response from Wordle in the format described in the Tutorial section.

Change `feedback` according to the response from Wordle and call `suggest_word`.


## Discussion
The algorithms used to calculate word probability use a combination of ideas stemming from information theory, markov decisions and probabilistic modelling. 
### Information Theory
Founded by Claude Shannon in the 1940s, information theory is the mutual unity of statistical mathematics and computer science. It uses in mathematics are prevalent in fields such as electrical engineering and telecommunications, whereas in computing, its uses are more foundational. Computers utilise information theory for simple tasks such as compressing files and error correction[1]. 

The most intuitive concept of information theory is information maximisation. For example, in this library, maximising information obtained from one guess by trying all unqiue letters is the most optimal way to gather the most data which leads to subsequent guesses being well founded. 

### Probabilistic Modelling
The two main areas of modelling with probability is conditional probability and pattern likelihood. Pattern likelihood is the core concept behind how each word is assessed. When a guess includes the most probable combination of letter frequencies and word compositions, the data suggests this would give the most informative feedback from Wordle. 

Conditional probability is used to account for the bias found in some words that force certain letters so either preceed or succeed them. 

In this library, conditional probabilty works by calculating the probability of any given letters position using:

$$ P(\text{letter } | \text{ letter in position x}) = \frac{P(\text{letter} \cap \text{letter in position x})}{P(\text{letter in position x})}$$

In linear tests, we assume the letter and its repsective position are independent, however, in further tests we account for the bias in certain conventions of the English language. 

### Markov Chains
A Markov Chain is defined as a chain of events in which the probability of each event occuring is solely dependent on the outcome of the previous event. 

In particular, frequency of letter pairs reflects the sequential dependency associated with markov chains, as each letter has a most probable complimentary letter, whose probability of occuring is solely dependent on the first letter in the pair. 

Let $X$ be the event that a given letter occurs in any word.

$$ P(\text{X}_{1} | \text{ Position 3}) \to P(\text{X}_{2} | \text{ Position 4} ) \to ...$$

This is the same situation which Markov chains base their conditional logic on [2].



## References

### List of functionality

- `suggest_word()` returns the most likely word from a given word list
- `word_collect()` returns all 2315 words which could be the Wordle answer
- `WordleSolver` class contains the probability function and algorithms to calculate the most likely word 
- `process_feedback()` updates the word list given a guess and its respective feedback



### Bibliography
[1] https://en.wikipedia.org/wiki/Information_theory#Quantities_of_information

[2] https://en.wikipedia.org/wiki/Markov_chain
