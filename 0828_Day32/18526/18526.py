import sys

sys.stdin = open('input.txt')

def insert(n):
    global last
    last += 1    # 마지막 노드 추가
    h[last] = n    # 값 배정
    c = last    # 자식 노드의 노드 번호
    p = c//2    # 부모 노드의 노드 번호
    while p >= 1 and h[p] > h[c]:    # 최소 힙이므로 부모의 값이 자식의 값보다 작아질 때까지
        h[p], h[c] = h[c], h[p]    # 자리 바꿈
        c = p
        p = c//2    # 인덱스 번호도 바꿔주기


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    arr = list(map(int, input().split()))

    h = [0]*(N+1)    # 최소 힙의 뼈대
    last = 0    # 힙의 마지막 노드 번호

    for num in arr:
        insert(num)

    # 마지막 노드의 모든 조상 찾기
    i = N
    result = []
    while i >= 1:
        i //= 2
        result.append(h[i])

    print(f'#{tc} {sum(result)}')
