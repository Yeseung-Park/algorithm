import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [[0]*N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    direction = 0

    num = 0
    i = 0
    j = 0

    while num < N*N:
        num += 1
        arr[i][j] = num
        ni = i + di[direction]
        nj = j + dj[direction]

        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != 0:
            direction = (direction+1) % 4

        i += di[direction]
        j += dj[direction]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()