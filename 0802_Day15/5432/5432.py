import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    arr = list(input())
    stack = []    # 하나씩 넣어보며 비교하기 위한 stack
    top = -1
    lazer_num = 0
    cut_num = 0
    iron_num = 0

    # 레이저로 자른 막대의 수와 기존 막대의 수를 더하면 잘려진 막대의 수가 나온다.

    for iron in arr:
        if not stack:
            top += 1
            stack.append(iron)
        else:
            if iron == '(':
                top += 1
                stack.append(iron)
            else:
                if stack[top] == '(':
                    top += 1
                    stack.append(iron)
                    lazer_num += 1
                    cut_num += len(stack)-lazer_num*2-iron_num*2
                else:
                    top += 1
                    stack.append(iron)
                    iron_num += 1

    result = cut_num + iron_num
    print(f'#{tc} {result}')