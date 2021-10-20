import random

def rIntList(size, bound=0, negatives=False):
    """
    Function that returns a random integer list within the
    given bounds and optionally skip negatives
    """
    if bound == 0:
        bound = 2 ** 32 - 1

    min = -bound
    max = bound
    
    if not negatives:
        min = 0
    
    list = []
    for i in range(0, size):
        list.append(random.randint(min, max))
    
    return list

if __name__ == "__main__":
    list1 = rIntList(5)
    print(list1)
    list2 = rIntList(10, 100, True)
    print(list2)