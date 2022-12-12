def typeCompare(x):
    value = ord(x)
    if (x.islower()):
        value += 100
    elif (x.isupper()):
        value += 200
    elif (int(x) % 2 == 1):
        value += 300
    else:
        value += 400

    return value

if __name__ == "__main__":
    str = input().strip()
    sortedStr = sorted(str, key=typeCompare, reverse=False)
    print(''.join(sortedStr))