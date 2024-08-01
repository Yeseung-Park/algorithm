# 미완성

import sys

sys.stdin = open('input.txt')

def binary_search_count(list, key):

    start = 0
    end = len(list)
    count = 0

    while start <= end:
        count += 1
        middle = (start+end)//2
        if list[middle] == key:
            return count
        elif list[middle] < key:
            start = middle+1
        else:
            end = middle-1

    return -1

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    P, Pa, Pb = map(int, input().split())

    page = [x for x in range(1, P+1)]

    resultA = binary_search_count(page, Pa)
    resultB = binary_search_count(page, Pb)

    if resultA < resultB:
        result = 'A'
    elif resultA == resultB:
        result = '0'
    else:
        result = 'B'

    print(f'#{tc} {result}')