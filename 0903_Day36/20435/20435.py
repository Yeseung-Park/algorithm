import sys

sys.stdin = open('input.txt')


# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 2):

    numbers = list(map(int, input().strip().split()))
    count = 0
    n = len(numbers)

    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(numbers[j])
        if sum(subset) == 0:
            count += 1

    print(f'#{tc} {count}')