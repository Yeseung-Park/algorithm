import sys

sys.stdin = open('input.txt')

def search(i, j, N, total):    # 완전 탐색을 위한 재귀 함수
    global minimum
    if total > minimum:    # 더한 값이 최소값보다 커지면
        return    # 이 방향으로 탐색 그만하고 돌아가기
    if i == N-1 and j == N-1:    # 도착지점에 도달하면
        minimum = total    # 최소값 갱신하고
        return    # 돌아가기
    if 0 <= i+di[0] < N and 0 <= j+dj[0] < N:    # 인덱스 안 이라면
        search(i+di[0], j+dj[0], N, total+arr[i+di[0]][j+dj[0]])    # 오른쪽 방향으로 먼저 가기
    if 0 <= i+di[1] < N and 0 <= j+dj[1] < N:    # 오른쪽 다 봤으면 인덱스 안 쪽에서
        search(i+di[1], j+dj[1], N, total+arr[i+di[1]][j+dj[1]])    # 아래 방향으로도 가보기
    else:
        return    # 둘 다 아니면 돌아가기


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0    # 합을 담을 변수
    minimum = 1e9    # 기본 최소값
    di = [0, 1]
    dj = [1, 0]    # 오른쪽 혹은 아래로 방향 전환을 위한 델타 배열

    search(0, 0, N, arr[0][0])
    print(f'#{tc} {minimum}')