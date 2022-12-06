import itertools

l1 = [1, 2, 3, 4, 5, 6]
l2 = [7, 8, 9, 10, 11, 12]

product = list(itertools.product(l1, l2))
print (product)