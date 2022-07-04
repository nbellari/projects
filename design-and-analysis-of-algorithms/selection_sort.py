from typing import *

def selection_sort(array: List[int]) -> None:
    n = len(array)
    if n == 0 or n == 1:
        # an empty or a singleton list is already sorted
        return

    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]

list1 = [10, 4, 18, 28, 43, 6]
selection_sort(list1)
print (list1)
