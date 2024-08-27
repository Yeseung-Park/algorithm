import sys

sys.stdin = open('input.txt')

def inorder(node):    # 왼쪽->루트->오른쪽
    global i
    if node == 0:
        return
    inorder(left[node])
    result[node] = i
    i += 1
    inorder(right[node])

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):
    # 중위순회로 돌면서 값을 넣으면 될 것 같은데...?
    # 생각만 쉽지

    N = int(input())
    numbers = [num for num in range(1, N+1)]
    left = [0]*(N+1)
    right = [0]*(N+1)

    # 우선 완전 이진 트리 만들기
    for i in range(1, N+1):
        if left[i] == 0:
            if i*2 <= N:
                left[i] = i*2
        else:
            if i*2+1 <= N:
                right[i] = i*2+1
    for i in range(1, N+1):
        if left[i] == 0:
            if i*2 <= N:
                left[i] = i*2
        else:
            if i*2+1 <= N:
                right[i] = i*2+1
    # 두 번 돌려야 하는 이유는 그래야 왼쪽 오른쪽을 다 고려해줄 수 있더라구요.
    # 이걸 하나로 어떻게 합쳐야 할 지는 아직 머리가 안 돌아간다.

    # 이제 중위순회로 하나씩 숫자 넣어주자.
    result = [0]*(N+1)
    i = 1    # 얘를 하나씩 늘려주면서 1, 2, 3, ... 이렇게 넣어줄거다.

    inorder(1)
    result1 = result[1]
    result2 = result[N//2]

    print(f'#{tc} {result1} {result2}')