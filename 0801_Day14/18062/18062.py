import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):    # 선택 정렬을 기본으로 하되
        if i%2 == 0:    # 짝수 번째 인덱스를 시작으로 할 경우
            max_idx = i    # 최댓값을 찾아 맨 앞으로 보내주고
            for j in range(i+1, N):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:    # 홀수 번째 인덱스를 시작으로 할 경우
            min_idx = i    # 최솟값을 찾아 맨 앞으로 보내준다.
            for j in range(i+1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    result = [0]*10

    for i in range(0, 10):
        result[i] = arr[i]    # 전체 배열 중 앞에 10개만 꺼내서 결과로 지정

    print(f'#{tc}', *result)

