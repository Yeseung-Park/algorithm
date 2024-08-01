import sys

sys.stdin = open('input.txt')

def binary_search_count(list, key):    # 이진탐색을 시행하는 함수에 한 번 탐색할 때마다 횟수를 세는 count 변수 추가

    start = 0
    end = len(list)-1
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

    page = [x for x in range(1, P+1)]    # 책의 전체 쪽을 리스트로 표현

    resultA = binary_search_count(page, Pa)
    resultB = binary_search_count(page, Pb)

    if resultA < resultB:    # A와 B의 이진 탐색 시행 횟수를 비교하여 결과를 결정하는 조건문
        result = 'A'
    elif resultA == resultB:
        result = '0'
    else:
        result = 'B'

    print(f'#{tc} {result}')