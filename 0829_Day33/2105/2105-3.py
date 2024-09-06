import sys

sys.stdin = open('input.txt')

def find(i, j, direction):    # i, j는 출발 지점의 행과 열, direction은 탐색 방향
    global maximum
    if direction > 3:
        return
    if direction == 3 and (i+di[direction], j+dj[direction]) == start:    # 다음에 갈 곳이 출발점이라면
        length[direction] += 1    # 일단 그쪽으로 가야하니까 length에 추가하고
        if length[0] == length[2] and length[1] == length[3] and 0 not in length:    # 가 본 경로가 직사각형이면
            if len(visit) > maximum:
                maximum = len(visit)    # 최댓값 비교하고 갱신
                #  돌아갈 필요는 없다 이미 찾은거니까 해당 출발점에서는
    else:
        if 0 <= i+di[direction] < N and 0 <= j+dj[direction] < N and cafe[i+di[direction]][j+dj[direction]] not in visit:    # 방문하지도 않았고 인덱스 안에도 존재하면
            length[direction] += 1    # 그 쪽 방향으로 간 거 추가하고
            visit.append(cafe[i+di[direction]][j+dj[direction]])    # 방문했다고 표시하고
            find(i+di[direction], j+dj[direction], direction)    # 다음 지점을 출발점으로 하고 해당 방향으로 계속 탐색
            length[direction] -= 1
            visit.pop()    # 돌아왔다는건 그 방향은 안 된다는 의미이므로 다 없애주기 해줬던거
        find(i, j, direction+1)    # 여기까지 왔다는건 해당 방향은 안 된다는 의미이므로 방향 바꿔주기
        return
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0    # 탐색 가능한 디저트 가게의 최댓값을 저장하는 변수

    # 모든 곳을 출발점으로 해서 완전 탐색
    # 탐색 방향은 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    for i in range(N):
        for j in range(N):
            visit = []
            length = [0, 0, 0, 0]
            visit.append(cafe[i][j])
            start = (i, j)    # 시작 지점 저장해주기
            find(i, j, 0)

    if maximum == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {maximum}')