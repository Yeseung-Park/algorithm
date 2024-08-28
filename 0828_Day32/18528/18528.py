import sys

sys.stdin = open('input.txt')

def postorder(node):
    if node == 0:
        return
    postorder()
# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, M, L = map(int, input().split())
    leaves = [list(map(int, input().split())) for _ in range(M)]
    tree = [0]*(N+1)
    # [키 값, 왼쪽 자식노드 번호, 오른쪽 자식노드 번호]

    for leaf in leaves:
        node_num = leaf[0]
        key = leaf[1]
        tree[node_num] = key

    # 뭔가 후위순회하면 될 것 같은데... 아닌가

    if N % 2 == 0:    # 노드의 개수가 짝수일 때는 마지막 리프노드가 혼자 있음
        tree[N//2] = tree[N]
        for i in range(N-1, 0, -2):
            tree[i//2] = tree[i] + tree[i-1]
    else:    # 노드의 개수가 홀수 일 때는 마지막 리프노드가 짝을 지음
        for i in range(N, 0, -2):
            tree[i//2] = tree[i] + tree[i-1]

    result = tree[L]
    print(f'#{tc} {result}')