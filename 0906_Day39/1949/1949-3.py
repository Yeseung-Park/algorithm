import sys

sys.stdin = open('input.txt')

def find(i, j, left):    # i, j: 현재 위치의 행과 열, left: 깎을 수 있는 횟수
    global maximum
    if len(path) > maximum:
        maximum = len(path)
    for k in range(4):
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < N and visited[i+di[k]][j+dj[k]] == 0:
            if land[i+di[k]][j+dj[k]] < land[i][j]:
                visited[i+di[k]][j+dj[k]] = 1
                path.append(land[i+di[k]][j+dj[k]])
                find(i+di[k], j+dj[k], left)
                visited[i+di[k]][j+dj[k]] = 0
                path.pop()
            elif left == 1:
                for depth in range(1, K+1):
                    if land[i+di[k]][j+dj[k]] - depth < land[i][j]:
                        land[i+di[k]][j+dj[k]] -= depth
                        path.append(land[i+di[k]][j+dj[k]])
                        visited[i+di[k]][j+dj[k]] = 1
                        find(i+di[k], j+dj[k], left-1)
                        land[i+di[k]][j+dj[k]] += depth
                        visited[i+di[k]][j+dj[k]] = 0
                        path.pop()

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, K = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]

    maximum_height = max(map(max, land))
    maximum = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):    # 시작점 찾기 -> 제일 높은 점이어야 한다.
            if land[i][j] == maximum_height:    # 시작점이 될 수 있으면
                path = []
                visited = [[0]*N for _ in range(N)]
                path.append(land[i][j])
                visited[i][j] = 1
                find(i, j, 1)

    print(f'#{tc} {maximum}')