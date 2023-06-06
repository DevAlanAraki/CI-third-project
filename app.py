from words import words
import random

# Select the word


def select_word():
    word = random.choice(words)
    return word.upper()

# Start the game
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
        
        attempt = input("Type a word or letter to continue: ").upper()

        print(attempt)

        # ATTEMPT OF USE ONE LETTER ONLY
        # Verifying if the attempt is a single letter
        if len(attempt) == 1 and attempt.isalpha():
            # verify if the letter was already used
            if attempt in letter_used:
                print("You already used this letter before: %s" % attempt)
            
            # verify if the letter it is not in the word
            elif attempt not in word:
                print("The letter %s is not in the word" % attempt)
                attempts -= 1
                words_used.append(attempt)

        # Invalid attempt
        else:
            print("Invalid attempt. Try again!")


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