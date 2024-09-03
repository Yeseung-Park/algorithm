import sys

sys.stdin = open('input.txt')

def find(i, j, direction):    # i와 j는 시작하는 행과 열
    global count
    if direction > 3:
        return
    if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and arr[i][j]+1 == arr[i+di[direction]][j+dj[direction]]:
        count += 1
        find(i+di[direction], j+dj[direction], 0)
    else:
        find(i, j, direction+1)
        return

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]    # 오른쪽 아래쪽 왼쪽 위쪽
    maximum = 0
    result_list = []

    for i in range(N):
        for j in range(N):
            count = 1
            direction = 0
            find(i, j, direction)
            if count > maximum:
                maximum = count
                result_list = []
                result_list.append([arr[i][j], maximum])
            elif count == maximum:
                result_list.append([arr[i][j], maximum])

    result = min(result_list, key=lambda x: x[0])
    print(f'#{tc}', *result)