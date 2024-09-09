import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())    # 원자의 개수
    elements = [list(map(int, input().split())) for _ in range(N)]    # 원자별 특성을 담은 리스트
    # [원자의 x좌표, 원자의 y좌표, 원자의 이동 방향, 원자의 에너지]
    energy = 0
    position_dict = {}

    # 0: 상, 1: 하, 2: 좌, 3: 우
    # 시간이 너무 오래 걸리니까 딕셔너리에 넣어두자 그냥... 뭐...

    di = [-0.5, 0.5, 0, 0]
    dj = [0, 0, -0.5, 0.5]

    while elements:
        for element in elements:
            if abs(element[0]) > 1000 or abs(element[1]) > 1000:    # 범위를 벗어나면
                continue
            element[0] += di[element[2]]
            element[1] += dj[element[2]]
            if (element[0], element[1]) in position_dict.keys():    # 안에 있으면
                position_dict[(element[0], element[1])].append(element[3])    # 파워 추가

    print(f'#{tc} {energy}')