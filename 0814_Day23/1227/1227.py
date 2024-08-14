import sys

sys.stdin = open('input.txt')

def BFS(i, j, N=100):    # i, j: 시작 정점의 행과 열    # N: 전체 미로의 크기로 여기서는 100으로 고정
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        ti, tj = queue.pop(0)    # ti, tj는 현재 방문한 정점
        if maze[ti][tj] == 3:    # 현재 방문한 정점이 3이면
            return 1    # 도착했으므로 1 반환
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:    # 오른쪽, 아래, 왼쪽, 위의 인접 방향에 대해서
            wi, wj = ti+di, tj+dj    # wi, wj는 인접한 정점
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                # 인접한 정점이 인덱스를 초과하지 않고 벽이 아니며 방문한 적이 없으면
                queue.append([wi, wj])    # queue에 append
                visited[wi][wj] = 1    # append 처리

    return 0

def find_start(maze):    # 시작 정점을 찾는 함수
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    sti, stj = find_start(maze)    # 시작 정점 찾아서 행과 열을 각각 sti, stj로 할당

    result = BFS(sti, stj)
    print(f'#{test_case} {result}')