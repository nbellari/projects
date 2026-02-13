import numpy

if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    arr = []
    for _ in range(0, n):
        arr.append(list(map(int, input().strip().split())))
    nxm = numpy.array(arr)
    print(numpy.mean(nxm, axis=1))
    print(numpy.var(nxm, axis=0))
    print(round(numpy.std(nxm), 11))
