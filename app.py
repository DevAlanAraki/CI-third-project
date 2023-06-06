from words import words
import random

# Select the word


def select_word():
    word = random.choice(words)
    return word.upper()


def play(word):
    # Define variables
    word_to_be_discovered = "_" * len(word)  # _ _ _ _ _
    guessed = False
    letter_used = []
    words_used = []
    attempts = 6

    # Welcome player
    print("Let's play!")
    print(display_hangman(attempts))
    print("This is the word: %s" % word_to_be_discovered)

    # While the player don't discover the word and still has future attempts
    while not guessed and attempts > 0:
        attempts = input("Type a word or letter to continue: ").upper()

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

# Loading and starting the game


def start():
    word = select_word()
    play(word)


start()