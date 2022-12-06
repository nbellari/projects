import itertools

# Get K and M from the input - which contains K and M as space separated strings
(k, m) = [int(a) for a in input().split()]

# Get the lists now
xLists = []
for i in range(0, k):
    inputItems = input().split()
    # First element is the size of the list
    nElems = int(inputItems[0])
    # list is from second elemnt till end
    list_i = [int(x) for x in inputItems[1:]]
    xLists.append(list_i)
    
# Get the cartesian product generator for all the lists
# Pass *xLists to expand the list to arguments
cartesianProduct = itertools.product(*xLists)

result = list(cartesianProduct)
print(result)