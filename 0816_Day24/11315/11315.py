import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # N: 판의 크기
    board = [list(input()) for _ in range(N)]    # 판 만들기

    omok = False    # 오목이 있는지 확인하는 변수
    diag_right = [[0, i] for i in range(N-1, 0, -1)]    # 오른쪽 아래 대각선을 찾기 위해 시작하는 요소
    diag_right2 = [[i, 0] for i in range(N)]
    diag_right.extend(diag_right2)
    diag_left = [[0, i] for i in range(N)]    # 왼쪽 아래 대각선을 찾기 위해 시작하는 요소
    diag_left2 = [[i, N-1] for i in range(1, N)]
    diag_left.extend(diag_left2)

    # 행을 하나씩 탐색하면서 해당 행이 오목인지 확인
    for i in range(N):
        row_omok = 0    # 한 줄에 연속해서 놓여져 있는 돌을 세는 변수
        for j in range(N):
            if board[i][j] == 'o':    # 돌이 놓여져 있으면
                row_omok += 1
            else:    # 중간에 끊기면
                row_omok = 0    # 다시 초기화
                continue
            if row_omok == 5:    # 다섯개 연속인 돌이 있다면
                omok = True
                break

    if omok == False:    # 행을 탐색했는데 없을 경우
        # 이번에는 열을 탐색하자
        for j in range(N):
            col_omok = 0
            for i in range(N):
                if board[i][j] == 'o':
                    col_omok += 1
                else:
                    col_omok = 0
                    continue
                if col_omok == 5:
                    omok = True
                    break

    if omok == False:    # 열도 탐색했는데 없을 경우
        # 이번에는 왼쪽 아래 대각선을 탐색하자
        for i, j in diag_left:
            diag_left_omok = 0
            while 0 <= i < N and 0 <= j < N:    # i와 j과 허용 인덱스 안에 있는 동안
                if board[i][j] == 'o':
                    diag_left_omok += 1
                    i, j = i+1, j-1
                else:
                    diag_left_omok = 0
                    i, j = i+1, j-1
                    continue
                if diag_left_omok == 5:
                    omok = True
                    break

    if omok == False:    # 왼쪽 아래 대각선을 탐색했는데 없을 경우
        # 이번에는 오른쪽 아래 대각선을 탐색하자
        for i, j in diag_right:
            diag_right_omok = 0
            while 0 <= i < N and 0 <= j < N:
                if board[i][j] == 'o':
                    diag_right_omok += 1
                    i, j = i+1, j+1
                else:
                    diag_right_omok = 0
                    i, j = i+1, j+1
                    continue
                if diag_right_omok == 5:
                    omok = True
                    break

    if omok == True:    # 오목이 있을 경우
        print(f'#{tc} YES')
    else:    # 오목이 없을 경우
        print(f'#{tc} NO')