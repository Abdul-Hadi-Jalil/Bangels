NUM_GUESSES = 10
NUM_DIGITS = 3


def display_rules():
    print(
        """
    Bagels, a deductive logic game.
    by Abdul Hadi Jalil
    
    I am thinking of a {}-digit number. Try to guess what it is.
    Here some clues:
    When I say:     That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position.
        Bangels     No digit is correct.
    
    I have thought up a number.
      You have {} guesses to get it.""".format(NUM_DIGITS, NUM_GUESSES)
    )

def play_bangels():
    


def main(): ...


if __name__ == "__main__":
    main()
