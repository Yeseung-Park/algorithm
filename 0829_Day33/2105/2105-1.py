import sys

sys.stdin = open('input.txt')

def find_route(i, j, direction, visit, length):    # 시작 행, 열, 시작 방향(항상 0), visit, length를 변수로 받음
    # 기본적인 접근 방식은 한 방향으로 가다가 더 이상 가지 못하는 경우 방향을 틀고 모든 방향이 유망하지 않으면 재귀로 돌아오는 함수
    # 먹어봤던 디저트와 같은 종류의 디저트를 파는 카페인지 확인하는 것은 visit안에 존재하느냐로 판단
    global maximum
    if direction >= 4:    # 모든 방향을 봤다면
        return    # 돌아가기
    if [i+di[direction], j+dj[direction]] == start:    # 다음에 내가 갈 곳이 시작지점이라면
        length[direction] += 1    # 시작 지점까지 가긴 하야하니까 해당 방향으로 간 거리를 추가해주고
        if length[0] == length[2] and length[1] == length[3] and 0 not in length:    # 내가 이제까지 간 거리가 사각형을 이루는지 확인
            if len(visit) > maximum:
                maximum = len(visit)    # 사각형이 맞으면 최댓값 계산하고 갱신
    if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and dessert_cafe[i+di[direction]][j+dj[direction]] not in visit:    # 만약 내가 다음에 갈 곳이 갈 수 있는 곳이라면
        i += di[direction]
        j += dj[direction]    # 실제로 이동
        length[direction] += 1    # 그 방향으로 간 거리도 추가
        visit.append(dessert_cafe[i][j])    # visit에 append
        find_route(i, j, direction, visit, length)    # 현재 위치를 기준으로 또 함수
        length[direction] -= 1    # 갔던 걸 취소해야하므로 길이도 하나 없애주고
        visit.pop()    # 방문했다는 이력도 없애주고
        i -= di[direction]
        j -= dj[direction]    # 갔다는 사실도 없애주기
        # 이렇게 해야 이전 함수를 이전 상태 그대로 호출할 수 있더라구요....
    direction += 1    # 만약 갈 수 없는 곳이라면 방향 바꾸기
    find_route(i, j, direction, visit, length)    # 바꾼 방향으로 함수
    direction -= 1    # 모든 방향이 갈 수 없는 곳이라면 방향을 하나씩 돌려주기
    return    # 그러고 나서 돌아가기

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 길이
    dessert_cafe = [list(map(int, input().split())) for _ in range(N)]    # 디저트 카페 지도

    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]    # 방향 전환을 위한 델타 배열로 오른쪽 아래 대각선 방향부터 시계방향으로 이동한다.
    maximum = 0    # 방문할 수 있는 최대 디저트 가게를 담는 변수

    # 모든 디저트 카페를 시작점으로 하여 경로를 찾아본다.
    for i in range(N):
        for j in range(N):
            direction = 0    # 방향을 의미하는 변수로 0부터 3까지 증가할 수 있다.
            visit = []    # 방문한 디저트 가게(디저트 종류)를 담는 리스트
            length = [0, 0, 0, 0]    # 대각선 방향으로 이동한 거리를 담는 리스트로 direction을 인덱스로 하여 변화시킨다.
            start = [i, j]    # 처음 출발한 곳의 위치를 저장
            visit.append(dessert_cafe[i][j])    # 우선 출발한 곳을 visit에 append
            find_route(i, j, direction, visit, length)    # 경로 찾기

    if maximum == 0:    # maximum이 0이라는건 유망한 경로가 없다는 것
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {maximum}')