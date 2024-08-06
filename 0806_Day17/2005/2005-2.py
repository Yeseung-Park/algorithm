# 처음 코드 수정

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    pascal = [[0]*i for i in range(1, N+1)]    # 파스칼의 삼각형을 담을 리스트

    for i in range(N):
        if i == 0:    # 첫 번째 줄은 무조건 1
            pascal[i][i] = 1
        else:
            for j in range(i+1):    # 나머지 줄에 대해
                if j == 0 or j == i:    # 맨 왼쪽과 오른쪽은 1
                    pascal[i][j] = 1
                else:    # 그 외의 경우는 위쪽 줄의 이웃한 두 값을 더한 값
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print(f'#{tc}')
    for i in range(N):
        print(*pascal[i])    # 원하는대로 출력하기