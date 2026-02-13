def mutate_string(string, position, character):
    return string[0:position-1] + character + string[position+1:]

if __name__ == '__main__':
    string = input().strip()
    line2 = input().strip().split()
    position, character = int(line2[0]), line2[1]
    print(mutate_string(string, position, character))