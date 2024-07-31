import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 2차원 정사각 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]    # 2차원 배열 생성

    # 오른쪽을 기준으로 시계방향으로 탐색
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total_sum = 0    # 전체 합을 담을 변수

    for i in range(N):
        for j in range(N):
            element_sum = 0    # 각 요소별 합을 담을 변수로 요소가 달라질 때마다 초기화가 되어야 한다.
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:    # 순회할 인덱스가 존재할 경우에만 시행
                    difference = abs(arr[ni][nj]-arr[i][j])
                    element_sum += difference    # 차의 절댓값을 더해주기
            total_sum += element_sum    # 각 요소별로 계산한 절댓값의 합을 전체 합에 더해주기

    print(f'#{tc} {total_sum}')