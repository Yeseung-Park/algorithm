import sys

sys.stdin = open('input.txt')

def find(i, j, direction, left):    # i, j: 현재 위치의 행과 열, left: 깎을 수 있는 횟수
    global maximum
    if len(path) > maximum:
        maximum = len(path)
    if direction > 3:
        return
    if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and land[i+di[direction]][j+dj[direction]] < land[i][j] and visited[i+di[direction]][j+dj[direction]] == 0:
        visited[i+di[direction]][j+dj[direction]] = 1
        path.append(land[i+di[direction]][j+dj[direction]])
        find(i+di[direction], j+dj[direction], 0, left)
        visited[i+di[direction]][j+dj[direction]] = 0
        path.pop()
    elif 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and left != 0 and visited[i+di[direction]][j+dj[direction]] == 0:
            number = K
            while number != 0:
                if land[i+di[direction]][j+dj[direction]] - number < land[i][j]:
                    land[i+di[direction]][j+dj[direction]] -= number
                    path.append(land[i+di[direction]][j+dj[direction]])
                    visited[i+di[direction]][j+dj[direction]] = 1
                    find(i+di[direction], j+dj[direction], 0, left-1)
                    land[i+di[direction]][j+dj[direction]] += number
                    visited[i+di[direction]][j+dj[direction]] = 0
                    path.pop()
                number -= 1
    find(i, j, direction+1, left)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, K = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    maximum_height = max(map(max, land))
    maximum = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):    # 시작점 찾기 -> 제일 높은 점이어야 한다.
            if land[i][j] == maximum_height:    # 시작점이 될 수 있으면
                path = []
                path_list = []
                path.append(land[i][j])
                find(i, j, 0, 1)

    print(f'#{tc} {maximum}')