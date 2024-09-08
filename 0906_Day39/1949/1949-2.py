import sys

sys.stdin = open('input.txt')

# 방문 전에 상태를 변화시키기 않고 방문 후에 상태를 변화시켜 보았다.
# 그리고 추가로 막혔을 때만 깎는게 아니라 그냥 일반적인 상황에서도 깎을 수 있게 하였다.
def find(i, j, k, left):  # i, j: 현재 위치의 행과 열, left: 깎을 수 있는 횟수
    global maximum
    if visited[i][j] == 0:    # 방문한 적이 없다고 하면
        visited[i][j] = 1
        path.append(land[i][j])    # 방문 처리
    if k > 3:
        if len(path) > maximum:
            maximum = len(path)
        return
    if left == 1:
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < N and visited[i+di[k]][j+dj[k]] == 0:
            for number in range(1, K+1):
                land[i+di[k]][j+dj[k]] -= number
                find(i+di[k], j+dj[k], 0, left-1)
                land[i+di[k]][j+dj[k]] += number
                visited[i+di[k]][j+dj[k]] = 0
                path.pop()
    if 0 <= i+di[k] < N and 0 <= j+dj[k] < N and land[i+di[k]][j+dj[k]] < land[i][j] and visited[i+di[k]][j+dj[k]] == 0:
        find(i+di[k], j+dj[k], 0, left)
        visited[i+di[k]][j+dj[k]] = 0
        path.pop()
    find(i, j, k+1, left)


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):

    N, K = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]

    maximum_height = max(map(max, land))
    maximum = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):  # 시작점 찾기 -> 제일 높은 점이어야 한다.
            if land[i][j] == maximum_height:  # 시작점이 될 수 있으면
                path = []
                visited = [[0] * N for _ in range(N)]
                find(i, j, 0, 1)

    print(f'#{tc} {maximum}')