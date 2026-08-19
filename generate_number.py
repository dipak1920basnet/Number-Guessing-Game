from random import randint

def Generate_number(low, high):
    number= randint(low, high)
    return number

if __name__ == "__main__":
    print(Generate_number(1,100))