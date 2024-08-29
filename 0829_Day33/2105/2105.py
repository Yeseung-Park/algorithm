# import sys
#
# sys.stdin = open('input.txt')

def find_route(i, j, direction):    # 시작 지점의 행과 열, 초기 방향
    if direction >= 4:
        return
    if [i+di[direction], j+dj[direction]] == start:
        length[direction] += 1
        return
    else:
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and desserts[i+di[direction]][j+dj[direction]] not in visited:
            i += di[direction]
            j += dj[direction]
            length[direction] += 1
            visited.append(desserts[i][j])
            find_route(i, j, direction)
        direction += 1
        find_route(i, j, direction)
# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 2):

    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]

    # 트리로 접근할 수 있을까?
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]
    maximum = 0

    for i in range(N):
        for j in range(N):
            visited = []
            length = [0, 0, 0, 0]
            direction = 0
            start = [i, j]
            visited.append(desserts[i][j])
            find_route(i, j, direction)
            print(visited)
            print(length)
            # k, l = i, j
            # visited.append(desserts[k][l])
            # while direction < 4:
            #     if [k+di[direction], l+dj[direction]] == start:
            #         length[direction] += 1
            #         break
            #     else:
            #         if 0 <= k+di[direction] < N and 0 <= l+dj[direction] < N and desserts[k+di[direction]][l+dj[direction]] not in visited:
            #             k += di[direction]
            #             l += dj[direction]
            #             length[direction] += 1
            #             visited.append(desserts[k][l])
            #         else:
            #             direction += 1
            if length[0] == length[2] and length[1] == length[3] and 0 not in length:    # 사각형을 그린 것이 맞음
                temp = len(visited)
                if temp > maximum:
                    maximum = temp

    if maximum == 0:
        print(-1)
    else:
        print(maximum)