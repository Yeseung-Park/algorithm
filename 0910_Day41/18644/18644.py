import sys

sys.stdin = open('input.txt')

def make_set(n):
    p = [i for i in range(n+1)]
    r = [0]*(n+1)    # 인덱스 맞추기 위해 n+1
    return p, r

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return    # 이미 같은 집합

    if ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    elif ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y
        ranks[root_y] += 1

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    form = list(map(int, input().split()))

    parents, ranks = make_set(N)

    for i in range(M):
        x, y = form[i*2], form[i*2+1]
        union(x, y)

    result = set()    # 결과 담는 집합
    for i in range(1, N+1):
        temp = find_set(i)
        result.add(temp)

    print(f'#{tc} {len(result)}')