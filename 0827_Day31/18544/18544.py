import sys

sys.stdin = open('input.txt')

def preorder(node):    # 루트->왼쪽->오른쪽
    if node == 0:
        return

    print(node, end=' ')
    preorder(left[node])
    preorder(right[node])


# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1,2):

    V = int(input())
    arr = list(map(int, input().split()))
    left = [0]*(V+1)
    right = [0]*(V+1)

    # 왼쪽 오른쪽 리스트 만들기
    for i in range(V-1):
        parent, child = arr[i*2], arr[i*2+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    preorder(1)