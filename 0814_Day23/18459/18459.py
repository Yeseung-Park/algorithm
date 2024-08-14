import sys

sys.stdin = open('input.txt')


def BFS(s, V):    # s: 시작 정점, V: 정점의 개수
    visited = [0] * (V+1)
    queue = []
    queue.append(s)
    visited[s] = 1    # enqueue 했다는 표시

    while queue:
        t = queue.pop(0)
        result.append(t)
        for w in adjL[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)]

# 인접 노드 리스트 만들기
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)

result = []    # 방문한 정점을 차례대로 담을 리스트
BFS(1, V)
print(f'#1', *result)