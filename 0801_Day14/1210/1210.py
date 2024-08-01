import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    test_case = int(input())    # 테스트 케이스의 번호

    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 기본적인 접근 방식은 도착 지점에서 거꾸로 올라가는 것

    # 가장 마지막줄에서 값이 2(도착)인 요소의 인덱스 찾기
    for i in range(0, 100):
        if ladder[99][i] == 2:
            end = i
            break

    # 현재 위치를 시작점으로 매번 재설정을 해주고 시작점에서 탐색을 진행하는 방식
    start_row = 99    # 첫 시작점의 row
    start_col = end    # 첫 시작점의 column

    # 인접한 네 방향 중 오른쪽, 왼쪽, 위쪽 방향의 순서로 확인하기
    # 이동할 위치를 찾으면 현재 위치는 0으로 바꿔 다시 그쪽으로 이동하지 않도록 하기
    di = [0, 0, -1]
    dj = [1, -1, 0]

    while start_row > 0:    # 현재 위치의 행이 0이 될 때까지

        for k in range(3):    # 오른쪽, 왼쪽, 위쪽 순서대로 탐색
            ni = start_row + di[k]
            nj = start_col + dj[k]
            if 0 <= ni < 100 and 0 <= nj < 100:    # 범위 안에 있는 요소에 대해서
                if ladder[ni][nj] == 1:    # 만약 해당 요소의 값이 1이라면
                    ladder[start_row][start_col] = 0    # 현재 위치한 요소의 값은 0으로 바꾸고
                    start_row = ni
                    start_col = nj    # 현재 위치를 해당 요소로 새롭게 정의
                    break

    print(f'#{test_case} {start_col}')