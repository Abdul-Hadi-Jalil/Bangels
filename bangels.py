import random

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
    You have {} guesses to get it.\n\n""".format(NUM_DIGITS, NUM_GUESSES)
    )


def play_bangels():
    clues = []

    # generating the random three digit number
    secret_num = str(random.randint(000, 999))

    for i in range(NUM_GUESSES):
        print(f"Guess # {i + 1}:")
        guess_num = input("> ")

        # check if user enters only a three digit number.
        if len(guess_num) == 3 and guess_num.isdecimal():
            for n in range(len(guess_num)):
                for m in range(len(secret_num)):
                    if guess_num[n] == secret_num[m]:
                        if n == m:
                            clues.append("Fermi")
                        else:
                            clues.append("Pico")
            if len(clues) == 0:
                clues.append("Bangles")

            if len(clues) > 1:
                clues.sort()
                print(",".join(clues))  # sort them so the player does not get any hint.
            else:
                print(clues[0])

            clues.clear()

        else:
            print("Enter only a three digit number. You have wasted your guess.\n")
            continue

        if guess_num == secret_num:
            print("Congratulations you guess right and won the game\n\n")
            return

    print("You ran out of guesses.")
    print(f"The answer was {secret_num}\n\n")


def main():
    display_rules()

    while True:
        play_bangels()

        print("Do you want to play again (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for Playing")


if __name__ == "__main__":
    main()
