from collections import deque

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())    # N: 자연수의 개수    # M: 작업 횟수
    # arr = list(map(int, input().split()))
    arr = deque(map(int, input().split()))
    count = 0    # 작업을 시행한 횟수

    while count < M:    # 주어진 작업 횟수만큼
        count += 1    # 작업 횟수 +1
        arr.append(arr[0])    # 맨 앞의 원소 뒤로 빼기
        arr.popleft()    # 맨 앞의 원소는 삭제

    result = arr[0]    # 가장 처음에 오는 원소가 결과
    print(f'#{tc} {result}')
