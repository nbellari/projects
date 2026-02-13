import re

if __name__ == "__main__":
    n_lines = int(input().strip())
    lines = []
    for _ in range(0, n_lines):
        lines.append(input())
    for line in lines:
        m = re.sub(r'(?<=[ ])\&\&(?=[ ])', r'and', line)
        m = re.sub(r'(?<=[ ])\|\|(?=[ ])', r'or', m)
        print(m)