def count_substring(string, sub_string):
    c = 0
    start = 0
    while (True):
        idx = string[start:].find(sub_string)
        if (idx != -1):
            c += 1
            start += idx+1
        else:
            break
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)