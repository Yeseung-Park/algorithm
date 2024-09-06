# 이건 DP를 활용하는 것!
# 나는 DP에 약하니까 잘 들어보자

# 3월 기준으로 생각: 2월까지의 최소 금액 + 본인의 금액 중 최소금액
# 이전의 최소 금액들을 활용해서 내 최소금액을 구할 수 있다!
# DP 활용하기
# 왜 DP로 활용 가능한가?
# 1. 작은 문제로 분할 가능해야한다.
#   - 전체 문제의 합 = 각 달까지의 최소 금액들이 쌓여서 완성
#   -> 각 달까지의 최소 금액 문제로 생각
# 2. 뒤에 결과를 구할 때, 앞에서 구했던 결과가 변하면 안 된다.

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    cost = list(map(int, input().split()))
    days = list(map(int, input().split()))
    dp = [0]*13    # 1~12월 최소 금액들을 저장    # 맨 앞은 인덱스도 맞추고 뭐 필요해...
    dp[1] = min(days[0]*cost[0], cost[1])

    for i in range(2, 13):
        # 현재 달의 최소 비용을 계산
        # 기본적으로 이전 달 + 1일 권 구입 / 이전 달 + 1달 권 / 3달 전에 3달권 구입 중 최소
        dp[i] = min(dp[i-1]+days[i-1]*cost[0], dp[i-1]+cost[1])

        if i >= 3:    # 3월 이후부터는 3달권도 고려
            dp[i] = min(dp[i], dp[i-3]+cost[2])

    # 1년권도 고려
    if dp[12] > cost[3]:
        print(f'#{tc} {cost[3]}')
    else:
        print(f'#{tc} {dp[12]}')

