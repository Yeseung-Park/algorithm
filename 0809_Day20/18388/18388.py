import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    total_number = []

    available_col = [n for n in range(N)]

    while count < N:
        available_col = [n for n in range(N)]
        for i in range(N):
            for j in range(N):

    print(arr)