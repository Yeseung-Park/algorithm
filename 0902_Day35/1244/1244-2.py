import sys

sys.stdin = open('input.txt')

def change(n, change_count):    # n은 숫자열의 길이, change_count는 일단 처음은 0
    if change_count == change_num:
        result = 0
        for k in range(len(numbers)):
            result += numbers[k]*(10**(len(numbers)-1-k))
        return result

    state = tuple(numbers + [change_count])
    if state in memo:
        return memo[state]

    maximum = 0
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] != numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                maximum = max(maximum, change(n, change_count+1))
                numbers[i], numbers[j] = numbers[j], numbers[i]

    memo[state] = maximum
    return maximum

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    temp1, temp2 = input().split()
    numbers = list(map(int, temp1))
    change_num = int(temp2)
    change_count = 0
    maximum = 0
    memo = {}

    print(change(len(numbers), 0))