# 처음 코드

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    pascal = [[] for _ in range(N)]    # 파스칼의 삼각형을 담을 빈 리스트 N개

    for i in range(N):
        if i == 0:    # 첫 번째 줄은 무조건 1
            pascal[i].append(1)
        else:
            for j in range(i+1):    # 나머지 줄에 대해
                if j == 0:    # 맨 왼쪽은 1
                    pascal[i].append(1)
                elif j == i:    # 맨 오른쪽도 1
                    pascal[i].append(1)
                else:    # 그 외의 경우는 위쪽 줄의 이웃한 두 값을 더한 값
                    pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])

    print(f'#{tc}')
    for i in range(N):
        print(*pascal[i])    # 원하는대로 출력하기