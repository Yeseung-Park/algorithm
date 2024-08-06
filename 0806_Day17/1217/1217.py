import sys

sys.stdin = open('input.txt')

def exponential(base, exp):    # 거듭제곱을 하는 함수를 정의
    if exp == 0:    # exp가 0이 되면
        return 1    # 1 반환
    else:
        return base*exponential(base, exp-1)    # exp의 값을 하나씩 줄이며 계속 곱하기

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for _ in range(1, 11):

    tc = int(input())
    base, exp = map(int, input().split())    # 밑과 지수의 값을 각각 변수로 받기

    result = exponential(base, exp)

    print(f'#{tc} {result}')