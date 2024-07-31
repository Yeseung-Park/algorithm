import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 이차원 리스트의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]    # 이차원 리스트 생성

    s = 0    # 합이 담길 변수

    for i in range(N):
        for j in range(N):
            if i == j or N-1-i == j:    # 대각선 방향의 요소들만 순회
                s += arr[i][j]    # 대각선 방향의 요소들을 더해주기

    # 정 가운데 요소가 중복되는 것을 고려해주지 않아도 되는 이유는
    # 위에서 i == j 또는 N-1-i == j라고 하였기 때문에
    # 이 둘을 모두 만족시키는 가운데 요소는 한 번만 고려가 된다.

    print(f'#{tc} {s}')