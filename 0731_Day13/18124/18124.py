import sys

sys.stdin = open('input.txt')

def sumup(list):
    sumup = 0
    for number in list:
        sumup += number
    return sumup    # 리스트 내 요소의 합을 구하는 함수 정의

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    num_set = list(map(int, input().split()))

    N = len(num_set)    # 주어진 집합의 원소의 개수

    subset_list = []    # 모든 부분집합을 각 요소로 갖는 리스트

    for i in range(1<<N):
        subset = []    # 부분집합 리스트
        for j in range(N):
            if i & (1<<j):
                subset.append(num_set[j])
        subset_list.append((subset))    # 모든 부분집합을 생성하는 반복문

    for subset in subset_list:
        if subset == []:
            subset_list.remove(subset)    # 공집합을 제거하는 부분

    result = 0    # 기본 결과를 0으로 설정

    for subset in subset_list:
        if sumup(subset) == 0:
            result = 1
            break    # 만약 원소의 합이 0인 부분집합이 존재할 경우 결과를 1로 변경

    print(f'#{tc} {result}')