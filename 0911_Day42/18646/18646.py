import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')

def prim(start):
    heap = []
    sum_weight = 0
    heappush(heap, (0, start))

    while heap:
        weight, v = heappop(heap)
        if visited[v] == 1:    # 이미 방문한 정점이면
            continue
        visited[v] = 1
        sum_weight += weight
        for next in adjL[v]:
            if visited[next[0]] == 1:    # 이미 방문한 정점이면 사이클이 생기므로
                continue
            heappush(heap, (next[1], next[0]))

    return sum_weight

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    V, E = map(int, input().split())
    # 정점의 개수가 더 적어? 그러면 prim이다!
    adjL = [[] for _ in range(V+1)]
    visited = [0]*(V+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        adjL[s].append((e, w))    # 끝점, 가중치
        adjL[e].append((s, w))    # 시작점, 가중치
        # MST에서는 항상 무방향 그래프라는 것을 명심!

    print(f'#{tc} {prim(0)}')