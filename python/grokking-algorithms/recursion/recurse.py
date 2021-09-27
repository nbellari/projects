def sum_recurse(list):
    """
    Calculates the sum of the elements of a list recursively
    """
    if (len(list) == 0):
        return 0
    elif (len(list) == 1):
        return list[0]
    else:
        return list[0] + sum(list[1:])

def count_recurse(list):
    """
    counts the number of elements of a list recirsively
    """
    if (len(list) == 0):
        return 0
    elif (len(list) == 1):
        return 1
    else:
        return 1 + count_recurse(list[1:])

def max_recurse(list):
    """
    finds the maximum element in a list recursively
    """
    def max(a, b):
        if (a > b):
            return a
        else:
            return b

    # There can be no maximum in an empty list!!
    assert(len(list) != 0)

    if (len(list) == 1):
        return list[0]
    else:
        return max(list[0], max_recurse(list[1:]))

if __name__ == "__main__":
    list = [1, 2, 3, -1]
    print(sum_recurse(list))
    print(count_recurse(list))
    print(max_recurse(list))
