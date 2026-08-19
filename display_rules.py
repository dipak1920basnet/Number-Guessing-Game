def rules(path):
    print()
    with open(path,'r') as file:
        for line in file:
            print(line)
    print()
if __name__ == "__main__":
    rules("rules.txt")