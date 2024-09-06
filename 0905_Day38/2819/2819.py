import sys

sys.stdin = open('input.txt')

def find(n, i, j, direction, path):    # n: 탐색한 횟수(시작은 1), i, j: 탐색을 시작한 행과 열, direction: 탐색할 방향
    if n == 7:
        temp = ''.join(path)
        total.add(temp)
        return
    if direction > 3:
        return
    if 0 <= i+di[direction] < 4 and 0 <= j+dj[direction] < 4:    # 인덱스 안에 있다면
        path.append(board[i+di[direction]][j+dj[direction]])
        find(n+1, i+di[direction], j+dj[direction], 0, path)
        path.pop()
    find(n, i, j, direction+1, path)    # path.pop()까지 했으면 무조건 다른 방향으로 봐야 하기 때문에
    # if-else로 하면 안 되고 그냥 혼자 빼놔야 한다. 무조건 돌아갈 수 있게.

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    board = [list(input().split()) for _ in range(4)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total = set()

    for i in range(4):
        for j in range(4):
            path = []
            path.append(board[i][j])
            find(1, i, j, 0, path)

    print(f'#{tc} {len(total)}')