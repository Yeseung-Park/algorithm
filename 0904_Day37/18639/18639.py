import sys

sys.stdin = open('input.txt')

def merge_sort(list):
    global count

    if len(list) == 1:
        return list

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        count += 1

    return merge(left, right)

def merge(left, right):
    result = [0]*(len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1
    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    numbers = list(map(int, input().split()))
    count = 0    # 오른쪽 원소가 먼저 복사되는 경우의 수를 담는 변수

    result = merge_sort(numbers)

    print(f'#{tc} {result[N//2]} {count}')