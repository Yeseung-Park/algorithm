import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())    # 신청서의 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    accept = []
    available = 0    # 작업 시작 가능한 시간을 담는 변수

    # 작업 시작 가능한 시간 이후에 시작하는 작업 중 제일 빨리 끝나는 것을 매번 선택

    while min(arr) != [25, 25]:    # 모두 다 확인하기 전까지 반복
        min_value = min(arr, key=lambda x: x[1])    # 가장 빨리 끝나는 것 체크
        if min_value[0] >= available:    # 시작 가능하다면
            accept.append(min_value)    # 결과 반영하고
            available = min_value[1]
            arr[arr.index(min_value)] = [25, 25]    # 없애기
        else:    # 시작 불가능하다면
            arr[arr.index(min_value)] = [25, 25]    # 없애기

    print(f'#{tc} {len(accept)}')