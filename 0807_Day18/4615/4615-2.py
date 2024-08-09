import sys

sys.stdin = open('input.txt')


def change_stone_black(start_i, start_j):
    board[start_i][start_j] = 'B'
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, 1, -1]    # 오른쪽 아래 왼쪽 위 오른쪽아래 왼쪽아래 왼쪽위 오른쪽위
    for k in range(8):
        change_stones = []
        for l in range(1, N):
            ni = start_i + di[k]*l
            nj = start_j + dj[k]*l
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 'W':
                    change_stones.append([ni, nj])
                elif board[ni][nj] == 'B':
                    for pair in change_stones:
                        board[pair[0]][pair[1]] = 'B'
                    break
                else:
                    break
            else:
                break

def change_stone_white(start_i, start_j):
    board[start_i][start_j] = 'W'
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, 1, -1]
    for k in range(8):
        change_stones = []
        for l in range(1, N):
            ni = start_i + di[k]*l
            nj = start_j + dj[k]*l
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 'B':
                    change_stones.append([ni, nj])
                elif board[ni][nj] == 'W':
                    for pair in change_stones:
                        board[pair[0]][pair[1]] = 'W'
                    break
                else:
                    break
            else:
                break


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]   # 놓을 바둑판 만들기
    arr = [list(map(int, input().split())) for _ in range(M)]
    result_B = 0    # 경기 후 흑돌의 개수를 담는 변수
    result_W = 0    # 경기 후 백돌의 개수를 담는 변수

    # 바둑판 기본 배치 설정하기
    di = [N//2-1, N//2, N//2, N//2-1]
    dj = [N//2-1, N//2-1, N//2, N//2]
    for i in range(4):
        if i%2 == 0:
            board[di[i]][dj[i]] = 'W'
        else:
            board[di[i]][dj[i]] = 'B'

    for turn in arr:
        if turn[2] == 1:
            start_i = turn[1]-1
            start_j = turn[0]-1
            change_stone_black(start_i, start_j)
        else:
            start_i = turn[1]-1
            start_j = turn[0]-1
            change_stone_white(start_i,start_j)

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'B':
                result_B += 1
            elif board[i][j] == 'W':
                result_W += 1
            else:
                pass

    print(f'#{tc} {result_B} {result_W}')