from collections import OrderedDict

def merge_the_tools(string, k):
    start = 0
    nSlices = int(len(string)/k)
    for i in range(0, nSlices):
        slice = string[start:start+k]
        nodupSlice = ''
        for j in slice:
            if j not in nodupSlice:
                nodupSlice += j
        print(nodupSlice)
        start += k

if __name__ == "__main__":
    testString = input()
    sliceLen = int(input())
    merge_the_tools(testString, sliceLen)