import numpy

if __name__ == "__main__":
    p = list(map(float, input().strip().split()))
    val = float(input())

    print(numpy.polyval(p, val))
    