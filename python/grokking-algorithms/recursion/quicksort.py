def qsort1(list):
    """
    This function does sorting the python way with list manipulation
    that is, new lists are created and merged, instead of in place
    sorting
    """
    if (len(list) < 2):
        # base case
        return list
    
    # pick a pivot and partition the elements
    pivot = list[0]
    left = [elem for elem in list[1:] if elem <= pivot]
    right = [elem for elem in list[1:] if elem > pivot]

    # sort the sub-lists recursively
    return qsort1(left) + [pivot] + qsort1(right)

def qsort_random_pivot(list, start, end):
    # For now always return start
    return (list[start], start)

def qsort2(list):
    """
    This function does sorting the standard C way
    that is, in place sorting is performed
    """
    def partition(list, start, end):
        pivot,idx = qsort_random_pivot(list, start, end)
        while (start < len(list) and start < end):
            while (start < len(list) and list[start] <= pivot):
                start = start + 1
            while (list[end] > pivot):
                end = end - 1
            if (start < end):
                list[start], list[end] = list[end], list[start]
        list[idx], list[end] = list[end], pivot
        return end

    def qsort_inplace(list, start, end):
        if (start >= end):
            # either an empty list or a list with single element
            return
        # partition and continue
        idx = partition(list, start, end)
        qsort_inplace(list, start, idx-1)
        qsort_inplace(list, idx+1, end)    

    qsort_inplace(list, 0, len(list)-1)
    return list 

if __name__ == "__main__":
    list = [2, 7, 1, 10, 4, 2]
    list = qsort2(list)
    print(list)