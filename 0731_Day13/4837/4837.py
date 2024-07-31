import sys

sys.stdin = open('input.txt')

def sumup(list):    # 리스트 내의 요소의 합을 구하는 함수 정의
    sumup = 0
    for number in list:
        sumup += number
    return sumup

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]    # 기본 집합 정의 (집합이 클 때는 for문을 사용해도 좋을 듯)
    N, K = map(int, input().split())

    subset_list = []    # arr의 모든 부분 집합을 요소로 담는 리스트

    # 모든 부분집합 구하기
    for i in range(1<<12):
        subset=[]
        for j in range(12):
            if i & (1<<j):
                subset.append(arr[j])
        subset_list.append(subset)

    result = 0    # 결과 변수

    for i in range(1<<12):    # 모든 부분집합 1<<12 개에 대해
        if len(subset_list[i]) == N and sumup(subset_list[i]) == K:    # 해당 부분 집합의 개수가 N이고 합이 K일 경우
            result += 1    # 결과에 1 추가

    print(f'#{tc} {result}')

