import sys

sys.stdin = open('input.txt')

def connect(n, now_processor, line_count, connected_core):    # 몇 개의 core를 연결했는지, 그 때의 processor의 상태와 전선의 개수, 현재 연결된 코어의 개수
    global minimum, max_connected_core

    if n == len(cores):    # 모든 core를 다 봤다면
        if connected_core > max_connected_core:    # 실제로 연결된 코어의 개수 확인하고
            max_connected_core = connected_core
            minimum = line_count    # 맞춰서 바꿔주기
        elif connected_core == max_connected_core:
            minimum = min(minimum, line_count)    # 최솟값 갱신
        return

    i, j = cores[n]    # 현재 집중하고 있는 core의 행과 열 변수 지정

    connect(n+1, now_processor, line_count, connected_core)
    # 우선 모든 애들을 다 무시한 후 뒤로 돌아오면서 하나씩 연결해보기

    # 사방 봐주기
    for k in range(4):
        possible_lines = []    # 전선 놓을 수 있는 위치 담는 변수
        depth = 1    # 얼마나 멀리까지 볼 것인지 담는 변수
        is_this_direc_okay = False    # 이 방향으로 전선 놓을 수 있는지 확인하는 변수
        while True:
            if i+di[k]*depth >= N or i+di[k]*depth < 0 or j+dj[k]*depth >= N or j+dj[k]*depth < 0:    # 끝까지 갔다는건 전선을 끝까지 연결할 수 있다는 것
                is_this_direc_okay = True    # 전선 놓을 수 있다고 하고
                break    # 빠져나오기
            if now_processor[i+di[k]*depth][j+dj[k]*depth] == 0:    # 전선을 놓을 수 있는 곳이라면
                possible_lines.append([i+di[k]*depth, j+dj[k]*depth])    # 전선 놓을 수 있는 위치 저장하고
                depth += 1    # 한 칸씩 더 보기
            else:    # 막혔을 경우
                break    # 그냥 빠져나오기
        if is_this_direc_okay:    # 전선 놓을 수 있으면
            for line in possible_lines:    # 전선 놓을 수 있는 자리에
                now_processor[line[0]][line[1]] = 2    # 전선 놓기
            connect(n+1, now_processor, line_count+len(possible_lines), connected_core+1)    # 전선 놓았으면 다음 core에 대해 살펴보기
            for line in possible_lines:
                now_processor[line[0]][line[1]] = 0    # 전선 되돌리기 (백트래킹)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    processor = [list(map(int, input().split())) for _ in range(N)]
    minimum = 1e9    # 전선의 개수의 최솟값을 담는 변수
    max_connected_core = 0    # 연결된 코어의 개수를 담는 변수

    # 가장자리에 있는 core를 제외한 나머지 core들의 행과 열을 담은 이중리스트를 하나 만들어보자.
    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if processor[i][j] == 1:
                cores.append([i, j])

    # 상하좌우 확인 위한 델타배열
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]    # 상하좌우 순서

    # 전선은 2로 표현할 것이다.
    # 우선적으로 고려되는 것은 최대한 많은 애들을 연결하는 것이다.

    connect(0, processor, 0, 0)


    print(f'#{tc} {minimum}')