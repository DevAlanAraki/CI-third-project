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
            else:
                print("You did it! The letter %s it is in the word" % attempt)
                letter_used.append(attempt)
                # Transform the word in a list
                word_list = list(word_to_be_discovered)

                # Verification where the letter is located in the word
                indexes = [i for i, letter in enumerate(word) if letter == attempt]
                for index in indexes:
                    word_list[index] = attempt

                word_to_be_discovered = "".join(word_list)

                if "_" not in word_to_be_discovered:
                    guessed = True
        
        # FULL WORD ATTEMPT
        # When the user attempt to predict the fully word
        elif len(attempt) == len(word) and attempt.isalpha():
            
            # Word already used
            if attempt in words_used:
                print("You already used this word %s." % attempt)
            # Word is incorrect
            elif attempt != word:
                print("The word %s is incorrect!" % attempt)
                attempts -= 1
                words_used.append(attempt)
            # Correct word
            else:
                guessed = True
                word_to_be_discovered = word
        
        # Invalid attempt
        else:
            print("Invalid attempt. Try again!")
        # Display the game status
        print(display_hangman(attempts))
        print(word_to_be_discovered)
    
    # End the game if the player discovered the word or if the attempts is 0
    if guessed:
        print("Congratulations! You discovered the word.")
    else:
        print("You have no more attempts to guess the word. The word was: %s" % word)

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
    # WHen the game ends, check if the user would like to play a new game
    while input("Would like to play again? (S/N)").upper() == 'Sf':
        word = select_word()
        play(word)

start()