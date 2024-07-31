import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for _ in range(1, 11):

    tc = int(input())    # 테스트 케이스의 번호
    arr = [list(map(int, input().split())) for _ in range(100)]    # 이차원 배열 생성

    max_row = 0
    max_col = 0
    max_diag = 0
    # 행별 합 중 최댓값, 열별 합 중 최댓값, 대각선별 합 중 최댓값을 담는 변수

    # 행별 합 중 최댓값을 구하고 지정하는 과정
    for i in range(100):
        sr = 0    # 각 행별 합을 담는 변수로 행이 새로 넘어갈 때마다 초기화가 되어야 한다.
        for j in range(100):
            sr += arr[i][j]
        if sr >= max_row:
            max_row = sr

    # 열별 합 중 최댓값을 구하고 지정하는 과정
    for j in range(100):
        sc = 0    # 각 열별 합을 담는 변수로 열이 새로 넘어갈 때마다 초기화가 되어야 한다.
        for i in range(100):
            sc += arr[i][j]
        if sc >= max_col:
            max_col = sc

    sd1 = 0    # 오른쪽 아래로 향하는 대각선의 합을 담는 변수
    sd2 = 0    # 왼쪽 아래로 향하는 대각선의 합을 담는 변수
    # 각 대각선의 합을 구하는 과정
    for i in range(100):
        for j in range(100):
            if i == j:
                sd1 += arr[i][j]
    for i in range(100):
        for j in range(100):
            if 99-i == j:
                sd2 += arr[i][j]

    # 두 대각선의 합 중 더 큰 값을 max_diag로 지정하는 과정
    if sd1 >= sd2:
        max_diag = sd1
    else:
        max_diag = sd2

    # 행, 열, 대각선 중 최댓값을 결과로 지정하는 과정
    maximum = [max_row, max_col, max_diag]    # 행 중 최댓값, 열 중 최댓값, 대각선 중 최댓값을 리스트로 만들기
    for i in range(len(maximum)-1, 0, -1):    # 정렬
        for j in range(0, i):
            if maximum[j] > maximum[j+1]:
                maximum[j], maximum[j+1] = maximum[j+1], maximum[j]

    result = maximum[-1]

    print(f'#{tc} {result}')
