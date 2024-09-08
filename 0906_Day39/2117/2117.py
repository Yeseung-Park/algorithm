import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    # 영역의 가운데 위치를 하나씩 옮겨가면서 찾아볼까
    # K가 어느정도로 커지면 손해인지 생각해야 되는데 일단 K = N일 때 손해라고 생각하고 코드를 짜보자.
    # 근데 3중 for문 너무 오래 걸릴 것 같은데
    # 거꾸로 가서 중간에 빠져나오면 좀 덜 걸리지 않을까

    N, M = map(int, input().split())    # 동네의 크기, 한 집 당 지불할 수 있는 금액의 값
    village = [list(map(int, input().split())) for _ in range(N)]

    print(village)