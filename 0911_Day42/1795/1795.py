import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')

def dijkstra(start):
    heap = []
    distance = [1e9]*(N+1)    # 인덱스 번호 맞춰주기 위해 N+1
    distance[start] = 0
    heappush(heap, (0, start))

    while heap:
        dist, v = heappop(heap)
        if dist > distance[v]:    # 이미 방문한 정점
            continue
        for next in adjL[v]:
            new_dist = dist + next[1]
            if new_dist >= distance[next[0]]:    # 가려는 경로가 더 긴 경로라면
                continue    # 무시
            distance[next[0]] = new_dist
            heappush(heap, (new_dist, next[0]))

    return distance

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, M, X = map(int, input().split())    # N: 집의 개수, M: 간선의 개수, X: 인수 집
    adjL = [[] for _ in range(N+1)]    # 인덱스 번호 맞춰주기 위해 N+1
    maximum = 0    # 최댓값 담는 변수

    for _ in range(M):
        s, e, w = map(int, input().split())    # 시작점, 끝점, 걸리는 시간
        adjL[s].append((e, w))    # 단방향 그래프

    # 갈 때는 모든 시작점에 대해서 찾아봐야 하나....? 시간이 너무 오래 걸리려나?
    # 일단 돌아올 때 최단거리를 저장하자.
    back = dijkstra(X)

    for i in range(1, N+1):    # 1번부터 N번까지의 집에 대해서
        if i == X:    # 인수의 집은 넘어가기
            continue
        go_time = dijkstra(i)[X]    # 가는데에 걸리는 시간
        back_time = back[i]    # 오는데에 걸리는 시간
        temp = go_time + back_time    # 왕복 시간
        if temp > maximum:
            maximum = temp    # 최댓값 갱신

    print(f'#{tc} {maximum}')