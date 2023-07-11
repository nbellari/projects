import re

if __name__ == "__main__":
    str = input().strip()
    substr = input().strip()

    last = len(substr)-1
    found = False
    matches = re.finditer(re.escape(substr[0:last])+r'(?='+re.escape(substr[last])+r')', re.escape(str))
    for m in matches:
            found = True
            range = (m.start(), m.end())
            print(range)
    if not found:
        print((-1, -1))