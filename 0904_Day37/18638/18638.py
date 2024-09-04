import sys

sys.stdin = open('input.txt')

def define_pivot(left, right):
    pivot = numbers[right]
    i = left - 1

    for j in range(left, right):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i+1], numbers[right] = numbers[right], numbers[i+1]
    return i+1

def quick_sort(left, right):
    if left < right:
        pivot = define_pivot(left, right)
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(0, N-1)

    print(f'#{tc} {numbers[N//2]}')