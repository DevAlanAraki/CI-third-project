from words import words
import random

# Select the word


def select_word():
    word = random.choice(words)
    return word.upper()

def play(word):
    #Define variables
    word_to_be_discovered = "_" * len(word) # _ _ _ _ _
    guessed = False
    letter_used = []
    words_used = []
    attempts = 6
    
    print(word)
    print(word_to_be_discovered)

word = select_word()
play(word)

# Game status (body)
def display_hangman(attempts):
    stages = [  # Game Over
        """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
        # Last attempt
        """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
        # Remain 2 attempts
        """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
        # Remain 3 attempts
        """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
        # Remain 4 attempts
        """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
        # Remain 5 attempts
        """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
        # First attempt
        """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
    ]
    
    return stages[attempts]

test = select_word()
print(test)

test_stages = display_hangman(4)
print(test_stages)