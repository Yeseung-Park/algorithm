import sys

sys.stdin = open('input.txt')


def operators(num1, num2, token):    # 연산자를 만났을 때 계산을 나타내는 함수
    if token == '+':
        return num1 + num2
    elif token == '-':
        return num1 - num2
    elif token == '*':
        return num1 * num2
    elif token == '/':
        return num1 // num2


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    postfix = list(input().split())
    stack = []

    for token in postfix:
        if token.isdecimal():    # 숫자면 stack에 push
            stack.append(int(token))
        elif token == '.':    # .을 만났는데
            if len(stack) == 1:
                result = stack.pop()    # 일반적인 경우 stack을 pop한 값을 결과로
            else:    # 만약 stack에 2개 이상의 요소가 있으면
                result = 'error'    # 형식이 잘못되었다는 것이므로 error가 결과
                break
        else:    # 나머지 연산자를 만났을 때
            if len(stack) < 2:    # 만난 시점의 stack의 길이가 2보다 작으면
                result = 'error'    # 형식이 잘못되었다는 것이므로 error가 결과
                break
            else:    # 그 외의 정상적인 경우에는
                num2 = stack.pop()
                num1 = stack.pop()
                temp = operators(num1, num2, token)    # 잘 계산해주고
                stack.append(temp)    # stack에 push

    print(f'#{tc} {result}')