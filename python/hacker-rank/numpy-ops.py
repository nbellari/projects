import numpy

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    arrA = []
    for _ in range(0, n):
        arrA.append(list(map(int, input().strip().split())))

    arrB = []
    for _ in range(0, n):
        arrB.append(list(map(int, input().strip().split())))

    A = numpy.array(arrA, int)
    B = numpy.array(arrB, int)

    print(A + B)
    print(A - B)
    print(A * B)
    print(A // B)
    print(A % B)
    print(A ** B)