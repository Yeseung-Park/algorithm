import sys

sys.stdin = open('input.txt')

def find_subset_sum(i, n, s, g):
    global count
    if s > g:    # 고려한 원소의 합이 찾는 합보다 큰 경우
        return    # 만족하지 않는다는 것이므로 이전 함수 호출
    elif s == g:    # 고려한 원소의 합이 찾는 합일 경우
        count += 1    # count에 1 추가하고
        return    # 다른 경우를 둘러보기 위해 return
    elif i == n:    # 모든 원소를 돌았을 경우
        return    # 다른 부분집합을 만들 수 있도록 이전 호출했던 함수로 되돌아가기
    else:    # 그 외의 경우 (모든 원소를 돌지도 않고 원소의 합이 찾는 합보다 작은 경우)
        bit[i] = 1    # 부분집합 만들기
        find_subset_sum(i+1, n, s+num_set[i], g)    # num_set[i] 포함    # 해당 부분집합의 합을 다시 넣어서 돌리기
        bit[i] = 0
        find_subset_sum(i+1, n, s, g)    # num_set[i] 미포함

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 2):

    num_set = list(map(int, input().split()))    # 집합
    N = len(num_set)    # 집합의 길이
    bit = [0] * N    # bit
    key = 10    # 찾고자 하는 합
    count = 0    # 합을 만족하는 부분집합의 개수를 세는 변수

    find_subset_sum(0, N, 0, key)    # 함수 돌리기

    print(f'#{tc} {count}')