from chances import Chance


def check_guess(guess, number):
    if guess == number:
        return True
    else:
        return False


def Play(label, number):
    total_attempt = 0
    try:
        chance = Chance(label)
    except ValueError as e:
        print(e)
    else:
        while total_attempt < chance:
            print(f"Number of attempt made: {total_attempt}")
            print(f"Attempt left: {chance-total_attempt}")

            guess = input("Make your guess -> ")
            total_attempt += 1
            try:
                guess = int(guess)
            except TypeError:
                print("Please enter a integer digit")
            else:
                guesses = check_guess(guess, number)
                if guesses == True:
                    print("Congrulation you guessed it right")
                else:
                    print("You made a wrong guess")

    return guesses


if __name__ == "__main__":
    Play(3, 61)
