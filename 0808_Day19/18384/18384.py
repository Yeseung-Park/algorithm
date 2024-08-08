import sys

sys.stdin = open('input.txt')

def find_route(start_i, start_j, N):    # 길 찾는 함수로 인자는 처음 시작점의 행과 열 그리고 전체 미로의 크기
    visited[start_i][start_j] = 1    # 방문한 곳에 방문했다는 것 표시
    if maze[start_i][start_j] == 3:
        return 1    # 만약 방문한 곳이 3일 경우 도착했다는 것이므로 1을 반환하고 종료
    else:    # 그 외의 경우 오른쪽 아래 왼쪽 위 방향 순서대로 인접탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = start_i + di, start_j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                # 인접 탐색한 위치가 허용 인덱스 안이고 벽이 아니며 가본 적이 없을 경우
                if find_route(ni, nj, N):    # 해당 인덱스 안에서 함수 다시 시행
                    return 1    # 얘는 도착을 해서 가장 최근에 함수를 종료했을 때 그때까지 쌓였던 함수들을 모두 종료시키고 완전히 재귀함수를 빠져나가는 역할
        return 0    # 만약 모든 인접 탐색한 위치가 이동 불가능한 곳이라면 0을 반환하고 가장 최근 불렀던 함수로 가기
        # 이 과정이 진짜 중요하다. 가장 최근에 반환한 함수로 가고 또 거기서는 다시 인접탐색을 하면서 결국 마지막으로 갈림길이 있던 곳으로 이동해 새로운 길을 찾는다는 것이 포인트


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i, start_j = i, j
                break

    visited = [[0]*N for _ in range(N)]

    result = find_route(start_i, start_j, N)

    print(f'#{tc} {result}')