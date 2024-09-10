import sys

sys.stdin = open('input.txt')

from collections import deque

def find(n, count):
    global result
    find_result = False
    q.append((n, count))

    # 일반적인 BFS는 append를 한 후 append를 했다는 의미에서 visited를 체크해준다.
    # 하지만 이건 순회할 트리가 만들어져 있을 때고.
    # 이건 그런게 아니라 그냥 하나씩 해보면서 그 결과를 저장하는 것이기 때문에
    # append를 하고 visited를 바로 변화하면 다음에 이미 방문했던 숫자를 확인할 때 걸러진다.
    # 그러니까 일단 append하고 popleft한 다음에 그걸 확인했다는 의미에서 그걸 visited에 넣어준다.

    while q:
        num, count = q.popleft()
        if num == M:    # 목표하는 숫자에 도달했다면
            return count
        if num in visited:    # 이미 방문했던 숫자라면
            continue    # 다른 숫자 보기

        visited.add(num)

        # 모든 중간 결과는 백만 이하의 자연수여야 한다.
        if num+1 <= 1000000:
            q.append((num+1, count+1))
        if num-1 >= 0:
            q.append((num-1, count+1))
        if num*2 <= 1000000:
            q.append((num*2, count+1))
        if num-10 >= 0:
            q.append((num-10, count+1))

    return -1

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):
    # 넓게 퍼져야 하므로 BFS 사용하기!
    N, M = map(int, input().split())
    q = deque()
    visited = set()
    result = 0

    result = find(N, 0)

    print(f'#{tc} {result}')