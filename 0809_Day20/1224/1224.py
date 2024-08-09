import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())
    infix = list(input())
    stack = []
    postfix = []
    top = -1

    print(infix)

    for token in infix:
        if token.isdecimal():
            postfix.append(token)
        else:
            if not stack:
                top += 1
                stack.append(token)
            else:
                if token == '(':
                    top += 1
                    stack.append(token)
                elif token == '+':
                    if not stack:
                        top += 1
                        stack.append(token)
                    elif stack[top] == '(':
                        top += 1
                        stack.append(token)
                    else:
                        while stack[top] != '(':
                            top -= 1
                            temp = stack.pop()
                            postfix.append(temp)
                        top += 1
                        stack.append(token)
                elif token == '*':
                    top += 1
                    stack.append(token)
                else:
                    while stack[top] != '(':
                        top -= 1
                        temp = stack.pop()
                        postfix.append(temp)
                    stack.pop()

    while stack:
        temp = stack.pop()
        postfix.append(temp)

    print(postfix)