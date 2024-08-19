import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    busline = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())

    print(busline)