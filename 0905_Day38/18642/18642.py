import sys

sys.stdin = open('input.txt')

def find_minimum(i, total):
    global minimum
    if i == N:
        if total < minimum:
            minimum = total
        return
    if total >= minimum:
        return
    for j in range(N):
        if complete[i][j] == 1:    # 이미 한 일이면
            continue    # 넘어가기
        for k in range(N):
            complete[k][j] = 1
        find_minimum(i+1, total+coasts[i][j])
        for k in range(N):
            complete[k][j] = 0

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    coasts = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    minimum = 1e9
    complete = [[0]*N for _ in range(N)]

    find_minimum(0, total)

    print(f'#{tc} {minimum}')