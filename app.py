from words import words
import random

# Select the word


def select_word():
    word = random.choice(words)
    return word.upper()

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

