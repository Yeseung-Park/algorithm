import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    test_case, N = input().split()
    n = int(N)
    arr = list(input().split())

    num_count = {"ZRO": 0,
                 "ONE": 0,
                 "TWO": 0,
                 "THR": 0,
                 "FOR": 0,
                 "FIV": 0,
                 "SIX": 0,
                 "SVN": 0,
                 "EGT": 0,
                 "NIN": 0}

    for number in arr:
        num_count[number] += 1

    count = list(num_count.values())
    num = list(num_count.keys())
    temp = [0] * n

    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(10):
        num_count[num[i]] = count[i]

    for i in range(n-1, -1, -1):
        num_count[arr[i]] -= 1
        temp[num_count[arr[i]]] = arr[i]

    print(test_case)
    print(*temp)