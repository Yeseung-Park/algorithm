import sys

sys.stdin = open('input.txt')

def binary_search(start, end, key, list):
    mid = (start+end)//2
    if list[mid] > key:    # 중앙값이

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A 정렬
    A.sort()


    print(A)
    print(B)