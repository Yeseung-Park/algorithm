import sys

sys.stdin = open('my_output.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1):
    arr1 = [input() for _ in range(1000)]
    arr2 = [input() for _ in range(1000)]

    for i in range(1000):
        if arr1[i] != arr2[i]:
            print(arr1[i], arr2[i])