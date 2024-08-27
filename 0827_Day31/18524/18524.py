import sys

sys.stdin = open('input.txt')

def preorder(node):    # 루트->왼쪽->오른쪽
    global count
    if node == 0:
        return
    count += 1
    preorder(left[node])
    preorder(right[node])

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    E, N = map(int, input().split())    # E: 간선의 개수, N: 루트 노드의 번호
    arr = list(map(int, input().split()))    # 부모 자식 노드 번호 쌍
    left = [0]*(E+2)
    right = [0]*(E+2)

    for i in range(E):
        parent, child = arr[i*2], arr[i*2+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    # 주어진 루트 노드의 서브 트리에 있는 노드의 개수 구하기
    # 아무 순회나 이용해도 될 것 같은데?
    count = 0
    preorder(N)

    print(f'#{tc} {count}')