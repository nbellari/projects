def checkNumbers(strElems, elems):
    for i in elems:
        if i < 0:
            print(False)
            return
    for i in strElems:
        if (i == i[::-1]):
            print(True)
            return
    print(False)

if __name__ == "__main__":
    nElems = int(input().strip())
    strElems = input().strip().split()
    elems = map(int, strElems)
    checkNumbers(strElems, elems)