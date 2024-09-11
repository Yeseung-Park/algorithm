import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, v = heappop(heap)

        if distance[v] < dist:    # 이미 고려한 정점
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

    N, E = map(int, input().split())    # N: 마지막 연결지점, E: 간선의 개수
    adjL = [[] for _ in range(N+1)]
    distance = [1e9]*(N+1)    # 각 정점 별 최단거리를 담는 리스트

    # 인접리스트 만들기
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjL[s].append((e, w))

    dijkstra(0)

    print(f'#{tc} {distance[-1]}')

