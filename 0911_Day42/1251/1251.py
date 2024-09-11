import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')

def prim(start):
    heap = []
    visited = [0]*N
    heappush(heap, (0, start))
    sum_weight = 0

    while heap:
        weight, v = heappop(heap)
        if visited[v] == 1:
            continue
        visited[v] = 1
        sum_weight += E*(weight**2)
        for next in adjL[v]:
            if visited[next[0]] == 1:
                continue
            heappush(heap, (next[1], next[0]))

    return sum_weight

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    islands =[]    # 각 섬의 좌표를 모아두는 리스트
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))    # 각 섬들의 x좌표와 y좌표가 모아져있다.
    for i in range(N):
        islands.append((x[i], y[i]))
    E = float(input())    # 환경부담금

    # 거리 구하는 공식 = ((x1-x2)**2+(y1-y2)**2)**0.5
    # 거리가 곧 가중치
    # 간선은 다 존재한다고 생각하고 그 중 선택하는걸로 하자.
    adjL = [[] for _ in range(N)]    # 0번부터 시작
    # 존재하는 간선의 개수는 N각형의 대각선의 개수+선분의 개수와 동일

    # 인접리스트 만들기
    for i in range(N-1):
        for j in range(i+1, N):
            weight = ((islands[i][0]-islands[j][0])**2+(islands[i][1]-islands[j][1])**2)**0.5
            adjL[i].append((j, weight))
            adjL[j].append((i, weight))

    result = prim(0)
    print(f'#{tc} {round(result)}')