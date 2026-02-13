def getMinIdx(array, start):
    min_idx = start
    for i in range(start+1, len(array)):
        if (array[i] < array[min_idx]):
            min_idx = i
    return min_idx

def ssort(array):
    """
    sorts the elements of the array from smallest to largest
    using selection sort method:
    """
    for i in range(0, len(array)-1):
        idx = getMinIdx(array, i)
        array[i], array[idx] = array[idx], array[i]

if __name__ == "__main__":
    list = [10, 2, 19, 4, 27, 43]
    ssort(list)
    print(list)
    list = [10, 2]
    ssort(list)
    print(list)
   