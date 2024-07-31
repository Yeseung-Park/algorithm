import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0    # 최댓값을 담기 위한 변수

    # 델타를 사용한 인접한 요소 순회
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(M):
            num_sum = arr[i][j]    # 원소 자기 자신과 그 상하좌우의 원소의 합을 담을 변수로 원소가 변할 때마다 자기 자신으로 초기화된다.
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    num_sum += arr[ni][nj]
            if num_sum > maximum:
                maximum = num_sum

    print(f'#{tc} {maximum}')
