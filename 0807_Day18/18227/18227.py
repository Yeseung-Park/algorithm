import sys

sys.stdin = open('input.txt')

def DFS(v):
    visited[v] = 1
    search.append(v)
    for next in adjL[v]:
        if visited[next] == 0:
            DFS(next)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    V, E = map(int, input().split())    # V: 노드의 수, E: 간선의 수
    arr = [list(map(int, input().split())) for _ in range(E)]    # 노드에 인접한 노드 쌍을 이중 리스트로 저장
    start, end = map(int, input().split())    # start: 시작하는 노드, end: 끝나는 노드
    adjL = [[] for _ in range(V+1)]    # 인접한 노드 저장하는 리스트

    for pair in arr:    # adjL 리스트 만들기
        adjL[pair[0]].append(pair[1])

    visited = [0]*(V+1)    # 재귀 함수를 위한 변수들
    search = []
    DFS(start)    # 주어진 시작점에서 DFS 시작

    if end in search:    # 경로상에 end가 있다면 갈 수 있는 경로가 있다는 것이므로
        result = 1    # 결과로 1
    else:    # 아니면
        result = 0    # 결과로 2

    print(f'#{tc} {result}')