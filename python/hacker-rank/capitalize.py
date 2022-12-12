# Complete the solve function below.
def solve(s):
    capitalizedString = ''
    prev = ' '

    for c in s:
        if (prev == ' ' and c.isalpha()):
            capitalizedString += c.upper()
        else:
            capitalizedString += c
        prev = c
    return capitalizedString


if __name__ == '__main__':
    print(solve("charles   wheelan"))
    print(solve("Amit Kale  shapoorji"))
    print(solve("Bob banerjee 420"))
    print(solve("kind  123"))
    print(solve("123 nath swamy"))
