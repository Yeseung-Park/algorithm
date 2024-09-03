import sys

sys.stdin = open('input.txt')

def find(i, j):
    count = 1
    stack = [(i, j, 0)]  # 스택을 사용하여 반복적으로 방향 탐색
    while stack:
        x, y, direction = stack.pop()
        if direction < 4:
            ni, nj = x + di[direction], y + dj[direction]
            if 0 <= ni < N and 0 <= nj < N and arr[x][y] + 1 == arr[ni][nj]:
                count += 1
                stack.append((ni, nj, 0))  # 방향을 다시 0으로 초기화
            else:
                stack.append((x, y, direction + 1))  # 다음 방향으로 이동
    return count

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]    # 오른쪽 아래쪽 왼쪽 위쪽
    maximum = 0
    result_list = []

    for i in range(N):
        for j in range(N):
            count = find(i, j)  # 재귀 대신 반복문을 사용한 함수 호출
            if count > maximum:
                maximum = count
                result_list = []
                result_list.append([arr[i][j], maximum])
            elif count == maximum:
                result_list.append([arr[i][j], maximum])

    result = min(result_list, key=lambda x: x[0])
    print(f'#{tc}', *result)