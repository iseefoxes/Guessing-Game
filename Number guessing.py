import random

def play_game(max_number, halfway):
    """
    Play the number guessing game for a given difficulty.
    max_number: maximum number in the range
    halfway: number of guesses before asking if the player wants to give up
    """
    guesses = 0
    number_to_guess = random.randint(1, max_number)
    guess_history = []

    print(f"\nGuess the number between 1 and {max_number}!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > max_number:
            print(f"Your guess must be between 1 and {max_number}.")
            continue

        guesses += 1
        guess_history.append(guess)

        if guess == number_to_guess:
            print(f"Correct! You guessed it in {guesses} tries.")
            break
        else:
            print(f"{guess} is incorrect.")

        # Halfway give-up check
        if guesses == halfway:
            quitter = input("Do you want to give up? (yes/no): ").lower()
            if quitter == "yes":
                print(f"Game over! The number was {number_to_guess}.")
                break
            else:
                print(f"Keep trying! You have {max_number - guesses - 1} attempts left.")

        # End game automatically when reaching max_number - 1 guesses
        if guesses >= max_number - 1:
            print(f"Game over! Maximum attempts reached. The number was {number_to_guess}.")
            break

    print("Your guesses were:", guess_history)
    print("Thank you for playing!\n")


def main():
    """
    Main menu for the Number Guesser game.
    """
    while True:
        print("***********************************************************")
        print("       | Welcome to the Number Guesser |")
        print("***********************************************************")
        print("Menu options:")
        print("1 - Easy (1-10)")
        print("2 - Medium (1-50)")
        print("3 - Hard (1-100)")
        print("4 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game(max_number=10, halfway=5)
        elif choice == "2":
            play_game(max_number=50, halfway=25)
        elif choice == "3":
            play_game(max_number=100, halfway=50)
        elif choice == "4":
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid option, please choose 1-4.")

        # Replay option
        replay = input("Do you want to return to the main menu? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()