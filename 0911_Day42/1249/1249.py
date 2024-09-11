import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')

def dijkstra(start):
    heap = []
    distance[start] = 0
    heappush(heap, (0, start))

    while heap:
        dist, v = heappop(heap)
        if dist > distance[v]:    # 이미 본 적 있는 정점이면
            continue
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
    arr = [list(map(int, input())) for _ in range(N)]
    adjL = [[] for _ in range(N**2)]
    distance = [1e9]*(N**2)    # 각 지점 별 최단 거리 담는 리스트
    '''
    N = 3 이면
    0 1 2
    3 4 5
    6 7 8    이런 식으로 번호 부여
    '''

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]    # 상하좌우

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:    # 인덱스 안에 위치 해 있으면
                    adjL[N*i+j].append((N*ni+nj, arr[ni][nj]))    # (정점 번호, 가중치)

    dijkstra(0)

    print(f'#{tc} {distance[-1]}')