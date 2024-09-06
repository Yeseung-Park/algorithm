# 강사님이 풀어주신 코드
# 이걸 완전탐색으로 구현할 수 있구나...

import sys

sys.stdin = open('input.txt')

# 시작점: 1월
# 끝점: 12월

def find(i, total):
    global minimum
    if i >= 12:    # 12월까지 고려했다면
        if total < minimum:
            minimum = total
        return
    # 1일권을 사용하는 경우
    find(i+1, total+cost[0]*days[i])
    # 한달권을 사용하는 경우
    find(i+1, total+cost[1])
    # 세달권을 사용하는 경우
    find(i+3, total+cost[2])
    # 1년권을 사용하는 경우는 사실 마지막에 고려해도 될 것 같다. 함수에 안 넣어도 될 듯.

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    cost = list(map(int, input().split()))
    days = list(map(int, input().split()))
    minimum = 1e9
    total = 0
    find(0, total)
    # 이제 여기서 1년권을 끊는 경우와 앞의 최솟값을 비교
    if cost[3] < minimum:
        minimum = cost[3]

    print(f'#{tc} {minimum}')