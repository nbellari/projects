from collections import OrderedDict

testString = input()
sliceLen = int(input())

def getSlices(str, k):
    nSlices = int(len(str)/k)
    start = 0
    for i in range(0, nSlices):
        yield str[start:start+k]
        start += k

def noDupSequence(slice):
    d = OrderedDict()
    for c in slice:
        d[c] = True
    return ''.join(d.keys())

for slice in getSlices(testString, sliceLen):
    print(noDupSequence(slice))