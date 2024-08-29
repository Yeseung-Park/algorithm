import sys

sys.stdin = open('input.txt')

def find_route(i, j, direction=0):    # 시작 행, 열, 방향(항상 0)
    if direction >= 4:
        return
    if [i+di[direction], j+dj[direction]] == start:
        length[direction] += 1
        return
    if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and dessert_cafe[i+di[direction]][j+dj[direction]] not in visit:
        i += di[direction]
        j += dj[direction]
        length[direction] += 1
        visit.append(dessert_cafe[i][j])
        find_route(i, j, direction)
        length[direction] -= 1
        visit.pop()
    direction += 1
    find_route(i, j, direction)
    direction -= 1
    return

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,2):

    N = int(input())
    dessert_cafe = [list(map(int, input().split())) for _ in range(N)]

    di = [1, -1, -1, 1]
    dj = [1, 1, -1, -1]

    for i in range(N):
        for j in range(N):
            direction = 0
            visit = []
            length = [0, 0, 0, 0]
            start = [i, j]
            visit.append(dessert_cafe[i][j])
            find_route(i, j)
            print(visit)
            print(length)

    print(dessert_cafe)