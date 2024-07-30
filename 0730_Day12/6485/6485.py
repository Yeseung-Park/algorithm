import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    busline = [0]*N    # 각각의 버스 노선을 요소 하나로 담을 리스트
    for i in range(N):    # 각각의 버스 노선이 요구하는 버스의 번호 범위(A, B)를 리스트로 지정하여 busline 리스트에 삽입
        busline[i] = list(map(int, input().split()))
    P = int(input())
    bus = [0]*P    # 각각의 버스 정류장 번호를 담을 리스트
    for j in range(P):
        bus[j] = int(input())

    bus_count = [0]*P    # 각각의 버스 정류장에 버스가 지나치는 횟수를 담을 리스트

    for i in range(N):    # N개의 버스 노선에 대해서
        for j in range(P):    # P개의 버스 정류장이
            if busline[i][0] <= bus[j] <= busline[i][1]:    # 버스 번호가 버스 노선에서 요구된 번호의 최대와 최소 사이일 경우
                bus_count[j] += 1    # 버스 노선이 지나는 것이므로 bus_count가 1 증가한다.
            else:
                pass

    print(f'#{tc}', *bus_count)
