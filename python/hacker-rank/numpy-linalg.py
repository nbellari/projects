import numpy

if __name__ == "__main__":
    n = int(input().strip())
    nByn = [list(map(float, input().strip().split())) for _ in range(0, n)]

    print(round(numpy.linalg.det(nByn), 2))