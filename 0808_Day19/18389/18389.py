import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    infix = list(input())
    stack = []
    postfix = []

    for token in infix:
        if token.isdecimal():
            postfix.append(token)
        else:
            stack.append(token)

    while stack:
        temp = stack.pop()
        postfix.append(temp)

    result = ''.join(postfix)

    print(f'#{tc} {result}')