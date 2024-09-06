import sys

sys.stdin = open('input.txt')

def find_route(i, j, direction, visit, dessert, length):    # 시작 행, 열, 방향(항상 0)
    global maximum
    if direction >= 4:
        return
    if [i+di[direction], j+dj[direction]] == start:
        length[direction] += 1
        if length[0] == length[2] and length[1] == length[3] and 0 not in length:
            if len(dessert) > maximum:
                maximum = len(dessert)
    if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and visit[i+di[direction]][j+dj[direction]] == 0 and dessert_cafe[i+di[direction]][j+dj[direction]] not in dessert:
        i += di[direction]
        j += dj[direction]
        length[direction] += 1
        dessert.append(dessert_cafe[i][j])
        visit[i][j] = 1
        find_route(i, j, direction, visit, dessert, length)
        visit[i][j] = 0
        length[direction] -= 1
        dessert.pop()
        i -= di[direction]
        j -= dj[direction]
    direction += 1
    find_route(i, j, direction, visit, dessert, length)
    direction -= 1
    return

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    dessert_cafe = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]
    maximum = 0

    for i in range(N):
        for j in range(N):
            direction = 0
            visit = [[0]*N for _ in range(N)]
            dessert = []
            length = [0, 0, 0, 0]
            start = [i, j]
            dessert.append(dessert_cafe[i][j])
            visit[i][j] = 1
            find_route(i, j, direction, visit, dessert, length)

    if maximum == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {maximum}')