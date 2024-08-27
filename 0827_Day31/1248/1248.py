import sys

sys.stdin = open('input.txt')

# 부모 찾기 함수
def find_ancestor(node, parent):
    if node in left:
        parent.append(node)
        find_ancestor(left.index(node), parent)
    elif node in right:
        parent.append(node)
        find_ancestor(right.index(node), parent)
    else:
        parent.append(node)
        return

# 서브트리 개수 찾기
def preorder(node):
    global count
    if node == 0:
        return
    count += 1
    preorder(left[node])
    preorder(right[node])

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    # V: 정점의 개수, E: 간선의 개수, 공통 조상을 찾는 두 개의 정점 번호
    V, E, node1, node2 = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0]*(V+1)
    right = [0]*(V+1)

    # 왼쪽 오른쪽 리스트 만들기
    for i in range(E):
        parent, child = arr[i*2], arr[i*2+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    # node1, node2의 모든 부모를 모아보자.
    parents1 = []
    find_ancestor(node1, parents1)
    parents2 = []
    find_ancestor(node2, parents2)

    # 가장 가까운 공통 조상 찾기
    # 짧은걸 기준으로
    if len(parents1) < len(parents2):
        for parent in parents1:
            if parent in parents2:
                same_parent = parent
                break
    else:
        for parent in parents2:
            if parent in parents1:
                same_parent = parent
                break

    count = 0
    preorder(same_parent)

    print(f'#{tc} {same_parent} {count}')