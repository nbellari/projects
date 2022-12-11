if __name__ == "__main__":
    n, elems = int(input()), input().split()
    result = all(map(lambda x: int(x)>0, elems)) and any(map(lambda x: x == x[::-1], elems))
    print(result)