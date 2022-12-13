if __name__ == '__main__':
    s = input()
    print(any(map(lambda x: x.isalnum(), s)))
    print(any(map(lambda x: x.isalpha(), s)))
    print(any(map(lambda x: x.isdigit(), s)))
    print(any(map(lambda x: x.islower(), s)))
    print(any(map(lambda x: x.isupper(), s)))