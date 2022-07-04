from collections import deque

def prefix(postfix):
    stack = deque()

    for s in postfix:
        if s.isalpha():
            stack.append(s)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(s+operand1+operand2)

    return stack.pop()

if __name__ == "__main__":
    print(prefix("AB*"))
    print(prefix("ABC/-AK/L-*"))
    print(prefix("AB+CD-*"))
