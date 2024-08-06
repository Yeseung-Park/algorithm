import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    arr = list(input())
    stack = []    # arr의 요소 하나하나를 비교하기 위해 만드는 stack
    top = -1    # top 선언

    for char in arr:
        if stack == []:    # stack에 아무것도 넣지 않았을 경우
            stack.append(char)
            top += 1
        else:
            if stack[top] != char:    # top에 있는 요소가 char랑 같을 경우
                stack.append(char)
                top += 1    # push
            else:    # 아닐 경우 중복된 문자라는 것이므로
                top -= 1    # top을 하나 뒤로 보내고
                stack.pop()    # pop

    result = len(stack)

    print(f'#{tc} {result}')
