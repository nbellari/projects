from typing import *

def bubble_sort(array: List[int]) -> None:
    n = len(array)

    if n == 0 or n == 1:
        # empty or singleton list is already sorted
        return None

    for i in range(n-1, 0, -1):
        swap = False
        for j in range(0, i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if swap == False:
            break

list1 = [10, 4, 18, 28, 43, 6]
bubble_sort(list1)
print (list1)
