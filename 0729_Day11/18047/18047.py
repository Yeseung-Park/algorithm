# [파이썬 S/W 문제해결 기본] 1일차 - 구간합

T=int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())

    numbers=list(map(int, input().split()))

    numbers_sum=[]

    for i in range(0, N-M+1):
        s=0
        for j in range(i, i+M):
            s+=numbers[j]

        numbers_sum.append(s)
    
    for _ in range(N-M+1):

        for i in range(N-M):

            if numbers_sum[i]<=numbers_sum[i+1]:
                pass
            else:
                numbers_sum[i], numbers_sum[i+1]=numbers_sum[i+1], numbers_sum[i]
    
    result=numbers_sum[N-M]-numbers_sum[0]

    print(f'#{test_case} {result}')
        

    