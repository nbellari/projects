import itertools

nElems = int(input())
elems = input().split()
k = int(input())

print(nElems)
print(elems)
print(k)

# find the probabality of seeing 'a' when k elements are chosen randomly from the list
nCk = list(itertools.combinations(elems, k))
nOccurances = 0
for combo in nCk:
    if 'a' in combo:
        nOccurances += 1

print("%.3f" % (1.0 * nOccurances)/nElems)
