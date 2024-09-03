import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    count = 0

    # 부분집합을 만들기
    for i in range(1<<N):
        total = 0
        for j in range(N):
            if i & (1<<j):
                total += numbers[j]    # 부분집합에 포함되는 원소 하나씩 더해주고
                if total > K:    # 중간에 이미 넘어가버리면
                    break    # 빠져나가기
        if total == K:
            count += 1

    print(f'#{tc} {count}')
