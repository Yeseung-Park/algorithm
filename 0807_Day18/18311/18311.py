import sys

sys.stdin = open('input.txt')

def DFS(v):    # 깊이 우선 탐색 함수
    visited[v] = 1
    result_int.append(v)
    for next in adjL[v]:    # 인접한 노드(다음 갈 곳)에 대해
        if visited[next] == 0:    # 다음 갈 곳이 방문하지 않았다면
            DFS(next)    # 계속 탐색
# 이렇게 될 경우 다음 갈 곳이 사라졌을 때 자동으로 함수가 종료되므로 탐색을 완료할 수 있다.

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 2):

    V, E = map(int, input().split())    # V: 노드의 수, E: 간선의 수
    arr = list(map(int, input().split()))    # 인접한 노드를 나타낸 리스트
    adjL = [[] for _ in range(V+1)]    # 인접 리스트 선언

    for i in range(E):    # 양방향 인접 리스트를 만드는 과정
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    visited = [0]*(V+1)
    result_int = []
    DFS(1)
    result_str = map(str, result_int)
    result = '-'.join(result_str)

    print(f'#{tc} {result}')



