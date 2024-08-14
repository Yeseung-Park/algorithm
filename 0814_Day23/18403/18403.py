import sys

sys.stdin = open('input.txt')

def BFS(i, j, N):    # i, j: 시작 정점의 행과 열    # N: 미로의 크기
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        ti, tj = queue.pop(0)
        if maze[ti][tj] == 3:
            return visited[ti][tj] - 2
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti+di, tj+dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                # wi, wj가 인덱스 안에 있고 벽이 아니며 방문한 적이 없을 경우
                queue.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    return 0


def find_start(maze, N):    # maze: 미로    # N: 미로의 크기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:    # 시작점이면
                return i, j    # 시작점의 행과 열 반환

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # N: 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = find_start(maze, N)
    result = BFS(sti, stj, N)

    print(f'#{tc} {result}')