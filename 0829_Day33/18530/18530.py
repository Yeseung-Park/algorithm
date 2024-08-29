import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = float(input())
    temp = 0
    result = ''
    is_it_overflow = True

    for i in range(1, 13):    # 13번 안에
        temp += 2**(-i)    # 일단 더하고
        if temp > N:    # 목표하는 값보다 커지면
            temp -= 2**(-i)    # 취소하고
            result += '0'    # 0
        elif temp == N:    # 목표하는 값이 되면
            is_it_overflow = False    # 오버플로우 아님
            result += '1'    # 1
            break    # 더 찾지 마
        else:    # 목표하는 값보다 작으면
            result += '1'    # 1

    if is_it_overflow:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')