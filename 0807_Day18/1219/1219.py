import sys

sys.stdin = open('input.txt')


def DFS(s):    # s: 시작 노드의 번호
    visited = [0]*100    # 노드의 최대 번호가 99이므로 길이가 100인 visited 리스트 생성
    stack = []    # 빈 스택
    v = s    # 시작 노드의 번호가 곧 처음 현재 위치 v
    visited[v] = 1    # 시작 노드를 방문했다고 변경
    search = [v]    # search는 방문한 노드를 담는 리스트로 우선 v 먼저 담아두기

    while True:
        for w in adjL[v]:    # v에 인접한 노드 w에 대해
            if visited[w] == 0:    # 방문한 적이 없다면
                stack.append(v)    # 현재 위치(v)를 우선 스택에 넣고
                v = w    # 현재 위치를 w로 변경
                visited[v] = 1    # 방문했다고 변경하고
                search.append(v)    # search에 담아두기
                break
        else:    # 인접한 노드 w가 없다면
            if stack:    # 스택에 무언가 있을 경우
                v = stack.pop()    # 스택의 제일 맨 위 요소(가장 최근에 방문한 정점)을 v로 지정
            else:    # 스택에 없을 경우 다 돈 것이므로
                break    # 빠져나가기

    return search


# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for _ in range(1, 11):

    tc, E = map(int, input().split())    # tc: 테스트 케이스의 번호    # E: 간선의 개수
    arr = list(map(int, input().split()))    # 인접한 노드를 표현하는 리스트
    adjL = [[] for _ in range(100)]    # 존재할 수 있는 노드의 번호가 0부터 99까지이므로 100개의 빈 리스트를 요소로 가진 adjL 이중 리스트 생성

    # adjL을 만드는 과정
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)    # 단방향이기 때문에 adjL[v2].append(v1)은 쓰지 않는다.

    result = DFS(0)

    if 99 in result:    # 만약 단방향으로 탐색한 경로 안에 99가 포함되어 있다면 99로 갈 수 있는 길이 존재한다는 것이므로
        print(f'#{tc} 1')    # 결과로 1
    else:    # 그 외의 경우에는 99로 갈 수 있는 길이 없다는 것이므로
        print(f'#{tc} 0')    # 결과로 0