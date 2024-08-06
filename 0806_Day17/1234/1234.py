import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):
    n, text = input().split()
    N = int(n)
    arr = list(text)    # 받은 변수를 원하는 형태로 형변환

    stack = []    # 빈 stack 준비

    for char in arr:
        if stack == []:    # stack에 기존에 넣은 변수가 없다면
            stack.append(char)    # 무조건 집어넣기
        else:    # 그 외의 경우
            if stack[-1] == char:    # stack의 제일 위쪽의 변수가 char랑 동일하다면
                stack.pop()    # 제일 위쪽의 변수를 제거
            else:    # 그 외의 경우
                stack.append(char)    # char를 stack에 집어넣기

    result = ''.join(stack)    # stack 리스트를 string으로 형변환
    print(f'#{tc} {result}')