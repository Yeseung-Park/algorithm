import sys

sys.stdin = open('input.txt')

def charge(n, battery, count):    # n: 버스의 현재 위치, battery: 버스의 현재 배터리 양, count: 배터리 충전한 횟수
    global minimum
    if n >= len(busstop):
        if count < minimum:
            minimum = count
        return
    if count >= minimum:
        return
    for j in range(battery, 0, -1):
        if n+j >= len(busstop):
            charge(n+j, 0, count)    # 어차피 거기 가서 충전할 필요 없으니까 충전 고려 X
        else:    # 그 외에는 충전 고려
            charge(n+j, busstop[n+j], count+1)    # 충전지에 아직 남아있어도 그냥 아예 교환이기 때문에 바뀌는구나 더해지는게 아니라
    # return    # 다 돌았으면 또 돌아가서 다른 경우 생각해봐

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    temp = list(map(int, input().split()))

    N = temp[0]    # N: 버스 정류장 수
    busstop = temp[1:]    # 버스 정류장 별 배터리

    battery = busstop[0]    # 초기 배터리 상태
    minimum = 1e9

    charge(0, battery, 0)

    print(f'#{tc} {minimum}')