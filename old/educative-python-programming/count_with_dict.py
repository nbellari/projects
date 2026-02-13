from collections import defaultdict
from collections import OrderedDict

def count_letters(message):
    d = defaultdict(int)

    for m in message:
        d[m] += 1

    return OrderedDict(sorted(d.items(), key=lambda x: x[1]))

if __name__ == "__main__":
    print(count_letters('Welcome to Educative'))
