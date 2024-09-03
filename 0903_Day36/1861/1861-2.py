import sys

sys.stdin = open('input.txt')

# 처음에는 재귀로 풀었다가 22번 케이스에서 너무 재귀호출이 많이 되어서 stack을 이용
# 사실 이건 내가 온전히 생각해낸 것은 아님...
def find(i, j):    # i와 j는 시작하는 행과 열
    global count
    stack = [(i, j, 0)]    # 현재 내가 위치한 행과 열, 그리고 방향이 stack의 가장 위에 위치한다.
    while stack:    # 스택이 비었다는 것은 모든 경로를 다 보았다는 것
        current_i, current_j, direction = stack.pop()    # 현재 내가 위치한 행과 열, 방향을 꺼내오기
        if direction < 4:    # direction이 4 이상이라면 모든 방향을 다 본 것이므로 밑에 진행하지 않고 while문 반복
            ni, nj = current_i+di[direction], current_j+dj[direction]    # 내가 가려는 곳 보기
            if 0 <= ni < N and 0 <= nj < N and arr[current_i][current_j]+1 == arr[ni][nj]:    # 조건에 맞다면
                count += 1    # 카운트 하나 추가하고
                stack.append((ni, nj, 0))    # 이동한 위치가 다시 현재 위치이며 새로운 방향으로 다시 시작해야하므로 (ni, nj, 0) 넣기
            else:    # 그 외의 경우에는
                stack.append((current_i, current_j, direction+1))    # 방향 바꾸기

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]    # 오른쪽 아래쪽 왼쪽 위쪽
    maximum = 0    # 최댓값 담는 변수
    result_list = []    # 최댓값을 갖는 경우와 그때의 시작한 방 번호를 담은 리스트    # [방 번호, 최댓값]

    for i in range(N):
        for j in range(N):
            count = 1    # 개수 세는 변수
            find(i, j)    # 함수 돌리기
            if count > maximum:    # 최댓값이 갱신 되었다면
                maximum = count
                result_list = []    # result_list도 초기화 해주고
                result_list.append([arr[i][j], maximum])    # 새로운 최댓값과 시작 방 번호를 담기
            elif count == maximum:    # 최댓값이랑 동일한 값이 나왔다면
                result_list.append([arr[i][j], maximum])    # 그것도 담아주기

    result = min(result_list, key=lambda x: x[0])    # result_list에서 방 번호를 기준으로 최솟값을 찾기
    print(f'#{tc}', *result)    # 결과 출력