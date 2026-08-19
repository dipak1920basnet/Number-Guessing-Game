from display_rules import rules
from choice import get_choice
from generate_number import Generate_number
from play import Play


def main():
    rule = "rules.txt"

    while True:
        rules(rule)
        label = get_choice(1, 3)
        number = Generate_number(1, 100)
        Play(label, number)
        print("Enter 1 to play again")
        print("Enter 2 to exit")
        again = get_choice(1, 2)
        if again == 1:
            continue
        else:
            break


if __name__ == "__main__":
    main()
