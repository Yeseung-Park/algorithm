import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())    # 문자열의 계산식의 길이
    arr = list(input())    # 계산식의 문자열 요소로 각각을 담는 리스트
    stack = []    # 후위표기를 위한 스택
    postfix = []    # 후위 표기된 계산식을 담을 리스트
    cal_stack = []    # 후위표기 계산식의 계산을 위한 스택

    # 후위 표기법으로 나타내는 과정
    for token in arr:    # 주어진 계산식의 token에 대해
        if token.isdecimal():    # token이 숫자면
            postfix.append(int(token))    # int형식으로 postfix에 append
        else:    # 숫자가 아닐 경우
            if not stack:    # 스택에 뭐가 한 번도 안 들어갔을 경우
                stack.append(token)    # 그냥 push
            else:    # 그 외의 경우에는
                temp = stack.pop()
                postfix.append(temp)    # pop하고 그 값을 postfix에 append
                stack.append(token)    # 해당 토큰 push
    while stack:    # 스택에 빌 때가지
        temp = stack.pop()
        postfix.append(temp)    # pop하고 그 결과 postfix에 append

    # 원래 후위표기법은 top도 설정해주고 다양한 경우를 고려해야하지만
    # 해당 문제에서는 문자열 계산식을 구성하는 연산자가 + 하나뿐이라고 했으므로
    # 이런 식으로 간단하게 적어봤다.

    # 계산하는 과정
    for token in postfix:    # 나타낸 후위 표기법 계산식의 요소에 대해서
        if type(token) == int:    # 숫자면
            cal_stack.append(token)    # 스택에 push
        else:    # 연산자면
            num2 = cal_stack.pop()
            num1 = cal_stack.pop()
            temp = num1 + num2    # 스택에서 2개 pop해서 계산
            cal_stack.append(int(temp))    # 계산한 결과 다시 스택에 push

    # 이것도 일반적인 경우에는 연산자에 따른 경우를 각각 고려해야하지만
    # 해당 문제에서는 연산자가 +밖에 없으므로 간단하게 적었다.

    result = cal_stack.pop()    # 마지막으로 스택에 남은 값 결과로 지정

    print(f'#{tc} {result}')
