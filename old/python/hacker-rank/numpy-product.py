import numpy

if __name__ == "__main__":
    n = int(input().strip())

    A = numpy.array([list(map(int, input().strip().split())) for _ in range(0, n)])
    B = numpy.array([list(map(int, input().strip().split())) for _ in range(0, n)])
    print(numpy.dot(A, B))