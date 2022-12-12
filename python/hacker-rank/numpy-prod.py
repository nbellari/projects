import numpy

if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    inArr = []
    for _ in range(0, n):
        inArr.append(list(map(int, input().strip().split())))

    array = numpy.array(inArr)
    sum_array = numpy.sum(inArr, axis=0)
    prod_array = numpy.prod(sum_array)
    print(prod_array)