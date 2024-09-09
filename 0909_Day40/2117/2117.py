import sys

sys.stdin = open('input.txt')

def find(i, j):
    global maximum

    K = 1

    while K <= N*2:    # 그냥 넉넉히 봐줌...
        line = 0    # 몇 번째 줄인지 세는 변수
        lines = 2*K-1    # 생기는 총 줄 수
        budget = 0    # 서비스 제공에 필요한 돈
        money = 0    # 지불할 수 있는 돈
        house = 0    # 서비스 받은 집의 수

        # 마름모 모양으로 볼까요
        for r in range(i-K+1, i+K):
            line += 1
            if line <= K:
                for c in range(j-line+1, j+line):
                    budget += 1
                    if r < 0 or r >= N or c < 0 or c >= N:    # 범위를 벗어나면
                        continue
                    if village[r][c] == 1:
                        house += 1
                        money += M
            else:
                for c in range(j-(lines-line), j+(lines-line)+1):
                    budget += 1
                    if r < 0 or r >= N or c < 0 or c >= N:    # 범위를 벗어나면
                        continue
                    if village[r][c] == 1:
                        house += 1
                        money += M
        if budget <= money:    # 지불할 수 있는 돈이 더 크거나 같다면
            if house > maximum:
                maximum = house

        K += 1

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, M = map(int, input().split())
    village = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0    # 최대로 지원할 수 있는 집의 수를 담는 변수

    for i in range(N):
        for j in range(N):
            find(i, j)

    print(f'#{tc} {maximum}')
