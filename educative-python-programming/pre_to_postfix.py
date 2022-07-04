from collections import deque

def postfix(prefix):
    stack = deque()

    postfix = ""
    for c in prefix:
        if not c.isalpha():
            stack.append([c, 0])
        else:
            postfix += c
            stack[-1][1] += 1
            while (stack and stack[-1][1] == 2):
                # Two operands have been printed
                postfix += stack.pop()[0]
                if (stack):
                    stack[-1][1] += 1
    while (stack):
        postfix += stack.pop()[0]

    return postfix

if __name__ == "__main__":
    print(postfix("*AB"))
    print(postfix("*-A/BC-/AKL"))
    print(postfix("*+AB-CD"))
