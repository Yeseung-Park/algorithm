import sys

sys.stdin = open('input.txt')

def icp(oper):    # 스택 밖에 있을 때 우선순위를 지정하는 함수
    if oper == '(':
        return 3
    elif oper in ('*', '/'):
        return 2
    elif oper in ('+', '-'):
        return 1

def isp(oper):    # 스택 안에 있을 때 우선순위를 지정하는 함수
    if oper == '(':
        return 0
    elif oper in ('*', '/'):
        return 2
    elif oper in ('+', '-'):
        return 1

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
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())
    infix = list(input())
    stack = []
    top = -1
    postfix = []

    # 후위표기법 변환
    for token in infix:
        if token.isdecimal():    # 숫자면
            postfix.append(token)    # postfix에 append
        else:
            if not stack:    # 스택이 비어있으면
                top += 1
                stack.append(token)    # 무조건 push
            else:    # 스택이 채워져 있는데
                if token != ')':    # 닫는 괄호가 아니면
                    if isp(stack[top]) < icp(token):    # top에 있는 것보다 내 우선순위가 더 높으면
                        top += 1
                        stack.append(token)    # push
                    else:    # 그렇지 않으면
                        while isp(stack[top]) >= icp(token):    # 내 우선순위가 더 높아질 때까지
                            top -= 1
                            temp = stack.pop()
                            postfix.append(temp)    # top을 pop하고 pop한 걸 postfix에 append
                        top += 1
                        stack.append(token)    # 내 우선순위가 높아지면 push
                else:    # 닫는 괄호의 경우에는
                    while stack[top] != '(':    # 여는 괄호를 만날 때까지
                        top -= 1
                        temp = stack.pop()
                        postfix.append(temp)    # top을 pop하고 postfix에 append
                    top -= 1
                    stack.pop()    # 여는 괄호를 만나면 여는 괄호 pop만 하기

    while stack:    # 스택이 비어질 때까지
        temp = stack.pop()
        postfix.append(temp)    # 남아있는 애들을 모두 pop하고 postfix에 append


    # 계산하기
    for token in postfix:
        if token.isdecimal():  # 숫자면 stack에 push
            stack.append(int(token))
        else:  # 나머지 연산자를 만났을 때
            num2 = stack.pop()
            num1 = stack.pop()
            temp = operators(num1, num2, token)  # 잘 계산해주고
            stack.append(temp)  # stack에 push

    result = stack.pop()
    print(f'#{tc} {result}')