def binary_search(list, item):
    """
    Binary search: given a sorted 'list' and an item, look
    for the item.
    returns:
        index of the item, if present
        None, otherwise
    """
    low = 0
    high = len(list) - 1
    while (low <= high):
        guess = (low + high)//2
        if (item == list[guess]):
            return guess
        elif (list[guess] > item):
            high = guess - 1
        else:
            low = guess + 1
    return None

if __name__ == "__main__":
    list = [1, 2, 5, 6, 7, 8, 10, 12, 28]
    index = binary_search(list, 7)
    print(index)
