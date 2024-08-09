import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())    # 문자열의 길이
    infix = list(input())    # 후위표기법으로 변환할 문자열
    stack = []    # 후위표기법으로 변환할 때와 계산할 때 동시에 사용될 스택
    top = -1
    postfix = []    # 후위표기법으로 변환한 문자열을 담는 리스트

    # 후위표기법으로 변환하는 과정
    for token in infix:
        if token.isdecimal():    # 숫자의 경우
            postfix.append(token)    # 바로 postfix에 append
        else:    # 연산자의 경우
            if not stack:    # 스택이 비었을 경우
                top += 1
                stack.append(token)    # 무조건 push
            else:    # 그 외의 경우
                if token == '+':    # 연산자가 +의 경우 우선순위가 낮아 무조건 스택을 비울때까지 pop한다.
                    while stack:
                        top -= 1
                        temp = stack.pop()
                        postfix.append(temp)
                    top += 1
                    stack.append(token)    # 다 비웠으면 append
                else:    # 그 외의 연산자 *는 우선순위가 높아 무조건 push 한다.
                    top += 1
                    stack.append(token)

    while stack:    # 스택이 비워질 때까지
        temp = stack.pop()
        postfix.append(temp)    # 계속 pop하고 postfix에 append

    # 계산하는 과정
    for token in postfix:
        if token.isdecimal():    # 숫자의 경우
            stack.append(int(token))    # 무조건 push
        else:    # 문자열의 경우
            if token == '+':    # 종류에 따라 다른 연산
                num2 = stack.pop()
                num1 = stack.pop()
                temp = num1 + num2
                stack.append(temp)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                temp = num1 * num2
                stack.append(temp)

    result = stack.pop()
    print(f'#{tc} {result}')