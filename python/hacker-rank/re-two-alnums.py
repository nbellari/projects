import re

if __name__ == "__main__":
    string = input().strip()
    match = re.search(r'([a-zA-Z0-9])\1+', string)
    if match:
        print(match.group(1))
    else:
        print(-1)