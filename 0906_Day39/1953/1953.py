import sys

sys.stdin = open('input.txt')

def find(n, i, j, direction, visit):    # i, j는 현재 위치의 행과 열
    global count
    if n == L-1:
        return
    if direction > 3:
        return
    # 7가지 경우를 다 고려해볼까 가능하려나 너무 하드코딩인가
    if tunnel[i][j] == 1:    # 상하좌우 이동 가능
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]    # 우, 하, 좌, 상
        ban = [[0, 2, 4, 5], [0, 3, 5, 6], [0, 2, 6, 7], [0, 3, 4, 7]]
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < M and visit[i+di[direction]][j+dj[direction]] == 0 and tunnel[i+di[direction]][j+dj[direction]] not in ban[direction]:    # 이동할 수 있다면
            visit[i+di[direction]][j+dj[direction]] = 1
            if count_list[i+di[direction]][j+dj[direction]] == 0:
                count += 1
                count_list[i+di[direction]][j+dj[direction]] = 1
            find(n+1, i+di[direction], j+dj[direction], 0, visit)    # 방향도 초기화 해야지...
            visit[i+di[direction]][j+dj[direction]] = 0
        find(n, i, j, direction+1, visit)
    elif tunnel[i][j] == 2:    # 상하 이동 가능
        di = [1, -1, 0, 0]
        dj = [0, 0, 0, 0]    # 하, 상
        ban = [[0, 3, 5, 6], [0, 3, 4, 7]]
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < M and visit[i+di[direction]][j+dj[direction]] == 0 and tunnel[i+di[direction]][j+dj[direction]] not in ban[direction]:
            visit[i+di[direction]][j+dj[direction]] = 1
            if count_list[i+di[direction]][j+dj[direction]] == 0:
                count += 1
                count_list[i+di[direction]][j+dj[direction]] = 1
            find(n+1, i+di[direction], j+dj[direction], 0, visit)
            visit[i+di[direction]][j+dj[direction]] = 0
        find(n, i, j, direction+1, visit)
    elif tunnel[i][j] == 3:    # 좌우 이동 가능
        di = [0, 0, 0, 0]
        dj = [1, -1, 0, 0]    # 우 좌
        ban = [[0, 2, 4, 5], [0, 2, 6, 7]]
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < M and visit[i+di[direction]][j+dj[direction]] == 0 and tunnel[i+di[direction]][j+dj[direction]] not in ban[direction]:
            visit[i+di[direction]][j+dj[direction]] = 1
            if count_list[i+di[direction]][j+dj[direction]] == 0:
                count += 1
                count_list[i+di[direction]][j+dj[direction]] = 1
            find(n+1, i+di[direction], j+dj[direction], 0, visit)
            visit[i+di[direction]][j+dj[direction]] = 0
        find(n, i, j, direction+1, visit)
    elif tunnel[i][j] == 4:    # 상우 이동 가능
        di = [-1, 0, 0, 0]
        dj = [0, 1, 0, 0]    # 상, 우
        ban = [[0, 3, 4, 7], [0, 2, 4, 5]]
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < M and visit[i+di[direction]][j+dj[direction]] == 0 and tunnel[i+di[direction]][j+dj[direction]] not in ban[direction]:
            visit[i+di[direction]][j+dj[direction]] = 1
            if count_list[i+di[direction]][j+dj[direction]] == 0:
                count += 1
                count_list[i+di[direction]][j+dj[direction]] = 1
            find(n+1, i+di[direction], j+dj[direction], 0, visit)
            visit[i+di[direction]][j+dj[direction]] = 0
        find(n, i, j, direction+1, visit)
    elif tunnel[i][j] == 5:    # 하우 이동 가능
        di = [1, 0, 0, 0]
        dj = [0, 1, 0, 0]    # 하, 우
        ban = [[0, 3, 5, 6], [0, 2, 4, 5]]
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < M and visit[i+di[direction]][j+dj[direction]] == 0 and tunnel[i+di[direction]][j+dj[direction]] not in ban[direction]:
            visit[i+di[direction]][j+dj[direction]] = 1
            if count_list[i+di[direction]][j+dj[direction]] == 0:
                count += 1
                count_list[i+di[direction]][j+dj[direction]] = 1
            find(n+1, i+di[direction], j+dj[direction], 0, visit)
            visit[i+di[direction]][j+dj[direction]] = 0
        find(n, i, j, direction+1, visit)
    elif tunnel[i][j] == 6:    # 하좌 이동 가능
        di = [1, 0, 0, 0]
        dj = [0, -1, 0, 0]    # 하, 좌
        ban = [[0, 3, 5, 6], [0, 2, 6, 7]]
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < M and visit[i+di[direction]][j+dj[direction]] == 0 and tunnel[i+di[direction]][j+dj[direction]] not in ban[direction]:
            visit[i+di[direction]][j+dj[direction]] = 1
            if count_list[i+di[direction]][j+dj[direction]] == 0:
                count += 1
                count_list[i+di[direction]][j+dj[direction]] = 1
            find(n+1, i+di[direction], j+dj[direction], 0, visit)
            visit[i+di[direction]][j+dj[direction]] = 0
        find(n, i, j, direction+1, visit)
    elif tunnel[i][j] == 7:    # 상좌 이동 가능
        di = [-1, 0, 0, 0]
        dj = [0, -1, 0, 0]    # 상, 좌
        ban = [[0, 3, 4, 7], [0, 2, 6, 7]]
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < M and visit[i+di[direction]][j+dj[direction]] == 0 and tunnel[i+di[direction]][j+dj[direction]] not in ban[direction]:
            visit[i+di[direction]][j+dj[direction]] = 1
            if count_list[i+di[direction]][j+dj[direction]] == 0:
                count += 1
                count_list[i+di[direction]][j+dj[direction]] = 1
            find(n+1, i+di[direction], j+dj[direction], 0, visit)
            visit[i+di[direction]][j+dj[direction]] = 0
        find(n, i, j, direction+1, visit)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    manhole = [R, C]
    count = 1
    visit = [[0]*M for _ in range(N)]
    count_list = [[0]*M for _ in range(N)]

    visit[R][C] = 1

    find(0, R, C, 0, visit)

    print(f'#{tc} {count}')