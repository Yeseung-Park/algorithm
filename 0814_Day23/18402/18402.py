import sys

sys.stdin = open('input.txt')

def BFS(s, e, V):    # s: 시작 정점    # e: 도착 정점    # V: 정점의 개수
    visited = [0] * (V+1)
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.pop(0)
        if adjL[t]:
            for w in adjL[t]:
                if visited[w] == 0:
                    queue.append(w)
                    visited[w] = visited[t] + 1

    if visited[e] == 0:    # 도착 정점이 한 번도 queue에 append된 적이 없다는 것은 가는 경로가 없다는 것이므로
        return 0    # 0 반환
    else:    # 그 외의 경우에는
        return visited[e]-1    # 도착점의 visited 값에서 1 뺀 값 반환
    # 1을 빼는 이유는 처음 시작점부터 1로 설정하고 시작했기 때문에 간선의 수는 1을 빼야 한다.

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    V, E = map(int, input().split())    # V: 노드의 수    # E: 간선의 수
    arr = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    adjL = [[] for _ in range(V+1)]    # 인접 배열

    # 인접 배열 만드는 과정
    for pair in arr:
        v1, v2 = pair[0], pair[1]
        adjL[v1].append(v2)    # 양방향
        adjL[v2].append(v1)

    result = BFS(start, end, V)

    print(f'#{tc} {result}')
