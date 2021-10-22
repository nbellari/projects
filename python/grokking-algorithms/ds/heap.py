class Heap:
    """
    Heap data structure, that supports the following operations:
    heapify - convert an array of integers to heap
    insert - insert an element in the heap and shuffles the array to satisfy heap property
    deque - dequeues the top most element and shuffles the array to satisfy heap property
    """
    def __init__(self, list=[]):
        self.array = list
        self.cmp = None

        if (list):
            self.heapify()
    
    def insert(self, elem):
        if not self.cmp:
            return
        self.array.append(elem)
        self.heapUp() # Only the last element needs to find its place

    def deque(self):
        if not self.cmp:
            return        
        elem = self.array[0]
        self.array[0] = self.array.pop() #replace with last element
        self.heapDown() # Only the root needs to find its place

    def heapUp(self):
        pass

    def heapDown(self):
        pass

    def heapify(self):
        if not self.list or len(self.list) == 1:
            return
        

    def __print__(self):
        pass

class MinHeap(Heap):
    def __init__(self, list=[], cmp=None):
        self.cmp = cmp if cmp else min
        super().__init__(list)

class MaxHeap(Heap):
    def __init__(self, list=[], cmp=None):
        self.cmp = cmp if cmp else max
        super().__init__(list)
