import numpy

if __name__ == "__main__":
    A = numpy.array(list(map(int, input().strip().split())))
    B = numpy.array(list(map(int, input().strip().split())))
    print(numpy.inner(A,B))
    print(numpy.outer(A,B))