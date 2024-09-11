import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')

def dijkstra(start):
    heap = []
    distance[start] = 0
    heappush(heap, (0, start))

    while heap:
        dist, v = heappop(heap)
        if dist > distance[v]:    # 이미 고려한 정점이면
            continue    # 넘어가기
        # visited[v] = 1
        for next in adjL[v]:
            new_dist = dist + next[1]
            if new_dist >= distance[next[0]]:
                continue
            distance[next[0]] = new_dist
            heappush(heap, (new_dist, next[0]))

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    adjL = [[] for _ in range(N**2)]    # 각 지역을 인덱스로 가지는 인접 리스트
    distance = [1e9]*(N**2)    # 각 정점별 최단거리를 저장하는 리스트

    '''
    번호 표현은
    0 1 2
    3 4 5
    6 7 8    이런 식으로 할 생각이다.
    '''
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]    # 상하좌우 방향
    # 그냥 차라리 이동 방향을 우 하 로 고정할까?

    # 인접리스트 (그래프) 만들기
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:    # 인덱스 안에 존재한다면
                    # 높이차가 더 높을 경우 그만큼이 가중치
                    # (번호, 가중치)로 append
                    # 기본적으로 한 칸 갈 때마다 1씩은 더해줘야 하므로 기본 가중치는 1이다.
                    if arr[ni][nj] > arr[i][j]:    # 높이가 더 높을 경우
                        weight = arr[ni][nj] - arr[i][j]
                        adjL[N*i+j].append((N*ni+nj, weight+1))
                    else:    # 높이가 같거나 낮을 경우
                        adjL[N*i+j].append((N*ni+nj, 1))    # 가중치는 1

    dijkstra(0)

    print(f'#{tc} {distance[-1]}')