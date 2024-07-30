import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    real_chargers = [0, *chargers, 10]    # 시적점과 종점까지 충전소에 포함
    result = 0    # 충전 횟수
    bus = 0    # 버스의 위치
    charge_okay = True

    # 인접한 충전기 사이의 거리가 K보다 클 경우 도착하지 못하므로 결과는 0
    for i in range(1, len(real_chargers)):
       if real_chargers[i]-real_chargers[i-1] > K:
           print(f'#{tc} {result}')
           charge_okay = False    # 충전 횟수 계산도 못하므로 charge_okay를 False로 변경
           break

    if charge_okay == True:    # charge_okay가 True일 때만 필요 충전 횟수 구하기
        while bus+K < N:
            for i in range(K, 0, -1):
                if bus+i in chargers:
                    bus += i
                    result += 1
                    break

        print(f'#{tc} {result}')