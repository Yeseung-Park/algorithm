import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, M = map(int, input().split())    # N: 컨테이너 수, M: 트럭 수
    weight = list(map(int, input().split()))    # N개의 컨테이너에 각각 담긴 화물의 무게
    load = list(map(int, input().split()))    # M개의 트럭의 적재 용량
    result = 0

    # 컨테이너 중에 가장 큰 거 찾고 트럭 중에 가장 큰 거 찾기
    # 만약 가장 큰 트럭이 가장 큰 컨테이너를 수용할 수 없다면 그 컨테이너는 0으로 만들고 넘기기
    # 수용할 수 있다면 해당 컨테이너 0, 트럭도 0으로 만들고 결과 반영
    # 컨테이너가 모두 0이 되거나 트럭이 모두 0이 될 때까지 반복

    while max(weight) != 0 and max(load) != 0:
        temp_weight = max(weight)
        temp_load = max(load)
        if temp_weight > temp_load:    # 가장 큰 컨테이너 수용 불가능
            weight[weight.index(temp_weight)] = 0    # 0으로 만들기
        else:    # 수용할 수 있으면
            result += temp_weight    # 결과 반영하고
            weight[weight.index(temp_weight)] = 0
            load[load.index(temp_load)] = 0    # 둘 다 0으로 만들기

    print(f'#{tc} {result}')