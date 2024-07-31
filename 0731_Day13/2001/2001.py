import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0    # 죽인 파리의 최댓값으로 초기값은 0으로 지정

    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            s = 0
            for k in range(M):
                for l in range(M):
                    if 0 <= i+k < N and 0 <= j+k < N:
                        s += arr[i+k][j+k]
            if maximum < s:
                maximum = s

    print(f'#{tc} {maximum}')
    # print(arr)