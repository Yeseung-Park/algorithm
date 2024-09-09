import sys

sys.stdin = open('input.txt')

def shoot(level, remains, now_boards):    # 공을 쏜 횟수, 남아있는 블록의 수, 현재 블록의 상태
    global min_block

    if level == N or remains == 0:    # 주어진 공을 다 썼거나 남아있는 블록이 없을 경우
        min_block = min(min_block, remains)
        return

    for j in range(W):
        copy_board = [row[:] for row in now_boards]
        i = -1
        for row in range(H):
            if copy_board[row][j] != 0:
                i = row
                break
        if i == -1:
            continue
        remains = pop(i, j, remains, copy_board)
        for col in range(W):
            idx = H-1
            for row in range(H-1, -1, -1):
                if copy_board[row][col] != 0:
                    copy_board[row][col], copy_board[idx][col] = copy_board[idx][col], copy_board[row][col]
                    idx -= 1

        shoot(level+1, remains, copy_board)


def pop(i, j, remains, boards):
    boards[i][j] = 0
    remains -= 1
    for p in range(1, boards[i][j]):
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < H and 0 <= nj < W and boards[ni][nj] != 0:
                pop(ni, nj, remains, boards)
    return remains

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, W, H = map(int, input().split())
    boards = [list(map(int, input().split())) for _ in range(H)]
    min_block = 1e9
    blocks = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(H):
        for j in range(W):
            if boards[i][j] != 0:
                blocks += 1

    shoot(0, blocks, boards)

    print(min_block)