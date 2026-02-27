def word_collect():
    """
    This function reads the text file called 'all_words.txt' which stores all possible wordle answers,
    Its purpose it to read the text file and create a list with each element being a new word.
    
    Paramters:
    ---------
    None

    Returns:
    -------
    List of all the possible wordle answers.
    
    """
    filename = 'all_words.txt'
    f = open(filename, 'r')
    all_words = [word.strip() for word in f]
    f.close()
    return all_words
