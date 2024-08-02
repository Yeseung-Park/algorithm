# [파이썬 S/W 문제해결 기본] 1일차 - min max

T=int(input())

for test_case in range(1, T+1):

    N=int(input())

    numbers=list(map(int, input().split()))

    for _ in range(N):
        for i in range(N-1):

            if numbers[i]<=numbers[i+1]:
                pass
            else:
                numbers[i], numbers[i+1]=numbers[i+1], numbers[i]

    result=numbers[N-1]-numbers[0]

    print(f'#{test_case} {result}')