if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    pattern = '.|.'
    n_lines = n // 2
    middle_line = 'WELCOME'.center(m, '-')

    # print top lines
    i = 1
    for _ in range(0, n_lines):
        print((pattern*i).center(m, '-'))
        i += 2
    # print middle line
    print(middle_line)

    # print bottom lines
    i -= 2
    for _ in range(0, n_lines):
        print((pattern*i).center(m, '-'))
        i -= 2
