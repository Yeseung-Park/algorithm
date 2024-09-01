import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 농장의 크기
    farm = [list(map(int, input())) for _ in range(N)]    # 농장

    i = 0; j = N//2; result = 0
    # 처음 시작할 위치의 행과 열 값, 수확한 농작물의 양을 담을 변수 result

    while i < N:
        for y in range(0+j, N-j):
            result += farm[i][y]
        if i >= N//2:    # 중간을 넘어가면
            j += 1    # 줄여가기
        else:    # 그 이전에는
            j -= 1    # 늘려가기
        i += 1

    print(f'#{tc} {result}')