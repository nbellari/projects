def print_formatted(number):
    num = int(number)
    cwidth = len(bin(num)[2:])+1
    for i in range(1, num+1):
        print(str(i).rjust(cwidth-1)+oct(i)[2:].rjust(cwidth)+hex(i)[2:].upper().rjust(cwidth)+bin(i)[2:].rjust(cwidth))

if __name__ == '__main__':
    n = input().strip()
    print_formatted(n)