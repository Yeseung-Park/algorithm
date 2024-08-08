import sys

sys.stdin = open('input.txt')

def find_route(start_i, start_j, N):
    visited[start_i][start_j] = 1
    while True:
        if maze[start_i][start_j] == 3:
            return 1
            break
        else:
            visited
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]
            for k in range(4):
                ni = start_i + di[k]
                nj = start_j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and maze[ni][nj] != 0:
                    start_i = ni
                    start_j = nj
                    start_i[start_i][start_j] = 1
                    visited[start_i][start_j] = 1
                    break
            # else:


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    stack = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i = i
                start_j = j

    print(maze)
    print(stack)