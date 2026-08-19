def Chance(label:int):
    if label == 3:
        return 3
    elif label == 2:
        return 5
    elif label == 3:
        return 10
    else:
        raise ValueError("Label must be in range of 1 to 3")