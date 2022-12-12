import itertools

l0 = [-1, -2]
l1 = [1, 2, 3, 4, 5, 6]
l2 = [7, 8, 9, 10, 11, 12]


product = list(itertools.product(l0, l1, l2))
for p in product:
    print(p)