import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 전선의 개수
    wired = [list(map(int, input().split())) for _ in range(N)]
    cross = 0

    for i in range(N-1):
        for j in range(i+1, N):
            if wired[i][0] < wired[j][0] and wired[i][1] > wired[j][1]:
                cross += 1
            elif wired[i][0] > wired[j][0] and wired[i][1] < wired[j][1]:
                cross += 1

    print(f'#{tc} {cross}')