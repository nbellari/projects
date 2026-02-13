def print_rangoli(size):
    alphabet="abcdefghijklmnopqrstuvwxyz"

    # construct the longest row first
    right = '-'.join(list(alphabet[0:size]))
    left = right[:0:-1]
    mid_line = left + right
    width = len(mid_line)

    lines = [mid_line]

    # construct the top rows
    start = 1
    for _ in range(1, size):
        right = '-'.join(list(alphabet[start:size]))
        left = right[:0:-1]
        line = (left+right).center(width, '-')
        lines.insert(0, line)
        start += 1
    
    # construct the bottom rows
    lines = lines + list(reversed(lines))[1:]

    print(*lines, sep='\n')


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)