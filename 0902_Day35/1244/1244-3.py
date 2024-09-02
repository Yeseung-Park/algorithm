import sys

sys.stdin = open('input.txt')

def find_index_reverse(key, list):
    for i in range(len(list)-1, -1, -1):
        if list[i] == key:
            return i

def change(i, change_count):
    global result
    if change_count == change_num:
        for k in range(len(numbers)):
            result += numbers[k]*(10**(len(numbers)-1-k))
        return result
    if i < len(numbers):
        maximum_index = find_index_reverse(max(numbers[i:]), numbers[i:])
        if maximum_index != i:
            numbers[maximum_index], numbers[i] = numbers[i], numbers[maximum_index]
        else:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        change(i+1, change_count+1)
    else:
        numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        change(i+1, change_count+1)


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    temp1, temp2 = input().split()
    numbers = list(map(int, temp1))
    change_num = int(temp2)
    change_count = 0
    result = 0

    change(0, change_count)
    print(result)
