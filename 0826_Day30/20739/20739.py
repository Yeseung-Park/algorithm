import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    picture = [list(input().split()) for _ in range(N)]

    maximum_i = 0
    maximum_j = 0

    # 행으로 먼저 검색
    for i in range(N):
        string = ''.join(picture[i])
        temp = string.split('0')
        for check in temp:
            if len(check) > 2:
                if len(check) > maximum_i:
                    maximum_i = len(check)

    # 열로 검색하는데 살짝 다르게 해야한다.
    for j in range(M):
        temp1 = []
        for i in range(N):
            temp1.append(picture[i][j])
        string = ''.join(temp1)
        temp2 = string.split('0')
        for check in temp2:
            if len(check) > 2:
                if len(check) > maximum_j:
                    maximum_j = len(check)

    if maximum_i > maximum_j:
        print(f'#{tc} {maximum_i}')
    else:
        print(f'#{tc} {maximum_j}')