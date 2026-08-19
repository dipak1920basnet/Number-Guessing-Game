def get_choice():
    while True:
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except TypeError:
            print("Please enter a integer number: ")
        else:
            if choice in range(1,4):
                return choice
            else:
                print("Enter a number in range of 1 to 3")