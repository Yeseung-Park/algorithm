import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    charge = list(map(int, input().split()))
    usage = list(map(int, input().split()))
    cost = 0    # 총 비용

    # 이 순서대로 고려한다.
    # 1. 한 달에 한달권//일일권 이하로 가면 일일권이 유리
    # 2. 연속 3달 동안 가는 경우 세달권이 유리
    # 3. 연속 9달 이상 가는 경우 1년권이 유리
    # 아 못해먹겠다

    # 일일권이 유리한 경우 먼저 고려
    for i in range(12):
        if 0 < usage[i] <= charge[1]//charge[0]:    # 일일권이 유리한 경우
            cost += usage[i]*charge[0]
            usage[i] = 0    # 고려해줬으니 넘어가기

    did_you_buy_year = False

    for i in range(0, 5):
        temp = usage[i:i+9]
        if 0 not in temp:    # 9달동안 연속으로 간다면
            cost += charge[3]
            did_you_buy_year = True
            break    # 1년치 사버렸기 때문에 더 고려 X

    if not did_you_buy_year:
        for i in range(0, 11):
            temp = usage[i:i+3]
            if 0 not in temp:
                cost += charge[2]
                usage[i:i+3] = [0]*3

    if not did_you_buy_year:
        for i in range(12):
            if usage[i] != 0:
                cost += charge[1]

    print(cost)