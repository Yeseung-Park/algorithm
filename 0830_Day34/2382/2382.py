import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, 2):

    N, M, K = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    locations = [0]*K
    for k in range(K):
        i, j, num, direc = map(int, input().split())
        board[i][j] = [num, direc]
        locations[k] = [i, j]
    di = [0, -1, 1, 0, 0]    # 상 하 좌 우
    dj = [0, 0, 0, -1, 1]    # 값을 맞춰주기 위해 처음은 0, 0
    t = 0
    while t < M:
        for location in locations:
            micro = board[location[0]][location[1]][0]
            direction = board[location[0]][location[1]][1]
            ni, nj = location[0]+di[direction], location[1]+dj[direction]
            board[location[0]][location[1]] = 0
            location[0], location[1] = ni, nj
            if ni == 0 or nj == 0 or ni == N-1 or nj == N-1:    # 가생이에 있는 경우
                micro //= 2    # 미생물 절반 사망하고
                if direction == 1:
                    direction = 2
                elif direction == 2:
                    direction = 1
                elif direction == 3:
                    direction = 4
                else:
                    direction = 3    # 방향 전환
                board[ni][nj] = [micro, direction]
            else:
                if board[ni][nj] == 0:
                    board[ni][nj] = [micro, direction]
                else:
                    if micro > board[ni][nj][0]:    # 현재 내 값이 더 크면
                        pass
                    else:
                        direction = board[ni][nj][1]
                    micro += board[ni][nj][0]
                    board[ni][nj] = [micro, direction]
        t += 1

    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                result += board[i][j][0]

    print(result)