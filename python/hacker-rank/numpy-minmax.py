import numpy

if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    arr = []
    for _ in range(0, n):
        arr.append(list(map(int, input().strip().split())))
    min_max_array = numpy.array(arr)
    min_axis_1 = numpy.min(min_max_array, axis=1)
    max_all = numpy.max(min_axis_1)
    print(max_all)
