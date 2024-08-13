import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cq = [0] * (N+1)    # 원형큐 만들어주기    # N+1은 여유공간을 하나 만들어줘야 하기 때문에    # front는 항상 비운다
    front = rear = 0    # 원형큐의 front와 rear

    for num in arr:    # 원형큐에 주어진 숫자 담기
        rear = (rear + 1) % len(cq)
        cq[rear] = num

    for _ in range(M):    # M번 작업
        front = (front + 1) % len(cq)
        rear = (rear + 1) % len(cq)
        cq[rear] = cq[front]
        cq[front] = 0    # front는 삭제한 것이나 다름 없기 때문에 0으로 지워주기

    result = cq[(front+1) % len(cq)]    # 원형큐의 제일 앞에 있는 요소가 결과
    # front가 큐의 마지막을 가리키고 있을 경우 front+1은 인덱스를 벗어나게 되므로 나머지 값을 인덱스로 해야한다.

    print(f'#{tc} {result}')
