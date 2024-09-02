import sys

sys.stdin = open('input.txt')

def find_min(n, start, total):
    global minimum
    if total > minimum:
        return
    if n == len(manage):
        result = total
        result += arr[path[-1]-1][0]    # 마지막 사무실로 돌아올 때 사용되는 배터리는 따로 계산
        if result < minimum:
            minimum = result    # 비교하고 최솟값 갱신
        return
    for i in manage:    # 관리구역으로 순열 만들기
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        find_min(n+1, start+1, total+arr[path[start]-1][path[start+1]-1])
        path.pop()
        used[i] = False

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    manage = [x for x in range(2, N+1)]    # 관리해야 할 구역
    path = [1]    # 처음에는 무조건 사무실
    minimum = 1e9
    total = 0    # 배터리 값을 누적하는 변수로 초기 값은 0
    used = [False]*(N+1)    # 인덱스와 관리구역 번호를 일치시킬 것이기 때문에 N+1

    find_min(0, 0, total)

    print(f'#{tc} {minimum}')