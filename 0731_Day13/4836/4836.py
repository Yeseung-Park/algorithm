import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [0]*N
    for i in range(N):    # 색칠되는 영역 하나에 대한 정보를 하나에 리스트로 만들고 이를 종합하여 이중 리스트로 만들기
        arr[i] = list(map(int, input().split()))

    # 기본적인 접근 방식은 빨강색과 파랑색이 칠해지는 영역을 별개로 나누어
    # 빨강색으로 칠할 경우 빨강색 영역에 1을, 파랑색으로 칠할 경우 파랑색 영역에 2를 기록하는 것이다.
    # 빨강색과 파랑색이 겹친 부분은 빨강색 영역에서도 파랑색 영역에서도 칠해졌을 것이므로 이를 이용한다.

    # lattice = [[0]*10 for _ in range(10)]    #전체 격자에 해당하는 2차원 배열 생성

    red = [[0]*10 for _ in range(10)]    # 빨강색이 칠해질 영역을 기록할 2차원 배열 생성
    blue = [[0]*10 for _ in range(10)]    # 파랑색이 칠해질 영역을 기록할 2차원 배열 생성

    for k in range(N):    # N개의 영역에 대해서
        if arr[k][4] == 1:    # 영역의 color가 1(빨강)일 경우
            for i in range(arr[k][0], arr[k][2]+1):    # 영역의 시작점 행 부터 끝점 행 까지
                for j in range(arr[k][1], arr[k][3]+1):    # 영역의 시작점 열 부터 끝점 열 까지
                    red[i][j] = 1    # 해당하는 red 원소에 1 할당
        elif arr[k][4] == 2:    # 영역의 color가 2(파랑)일 경우
            for i in range(arr[k][0], arr[k][2]+1):    # 영역의 시작점 행 부터 끝점 행 까지
                for j in range(arr[k][1], arr[k][3]+1):    # 영역의 시작점 열 부터 끝점 열 까지
                    blue[i][j] = 1    # 해당하는 blue 원소에 1 할당

    num = 0    # 겹친 부분의 개수를 담는 변수

    for i in range(10):
        for j in range(10):
            if red[i][j] == blue[i][j] == 1:
                num += 1    # red랑 blue 격자를 순회하면서 둘 다 동일하게 1의 값인 원소가 나올 경우 num에 1 추가

    print(f'#{tc} {num}')