import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    test_case, N = input().split()
    length = int(N)

    arr = list(input().split())

    for i in range(length):
        if arr[i] == "ZRO":
            arr[i] = 0
        elif arr[i] == "ONE":
            arr[i] = 1
        elif arr[i] == "TWO":
            arr[i] = 2
        elif arr[i] == "THR":
            arr[i] = 3
        elif arr[i] == "FOR":
            arr[i] = 4
        elif arr[i] == "FIV":
            arr[i] = 5
        elif arr[i] == "SIX":
            arr[i] = 6
        elif arr[i] == "SVN":
            arr[i] = 7
        elif arr[i] == "EGT":
            arr[i] = 8
        elif arr[i] == "NIN":
            arr[i] = 9

    count = [0]*10
    temp = [0]*length

    for num in arr:
        count[num] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(length-1, 0, -1):
        count[arr[i]] -= 1
        temp[count[arr[i]]] = arr[i]

    for i in range(length):
        if temp[i] == 0:
            temp[i] = "ZRO"
        elif temp[i] == 1:
            temp[i] = "ONE"
        elif temp[i] == 2:
            temp[i] = "TWO"
        elif temp[i] == 3:
            temp[i] = "THR"
        elif temp[i] == 4:
            temp[i] = "FOR"
        elif temp[i] == 5:
            temp[i] = "FIV"
        elif temp[i] == 6:
            temp[i] = "SIX"
        elif temp[i] == 7:
            temp[i] = "SVN"
        elif temp[i] == 8:
            temp[i] = "EGT"
        elif temp[i] == 9:
            temp[i] = "NIN"

    print(test_case)
    print(*temp)