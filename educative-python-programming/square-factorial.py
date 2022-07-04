def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def square_factorial(n):
    return [factorial(i)**2 for i in range (0, n)]

if __name__ == "__main__":
    print(square_factorial(3))
