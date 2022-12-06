import itertools

# Get K and M from the input - which contains K and M as space separated strings
(k, m) = [int(a) for a in input().split()]

# Get the lists now
xLists = []
for i in range(0, k):
    inputItems = input().split()
    nElems = int(inputItems[0])
    list_i = [int(x) for x in inputItems[1:]]
    xLists.append(list_i)
    
print(xLists)