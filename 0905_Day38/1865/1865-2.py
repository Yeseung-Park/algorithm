import sys

sys.stdin = open('input.txt')


def find(i):
    global maximum
    if i == N:
        total = 1
        for k in range(N):
            total *= probability[k][path[k]] * 0.01
        if total > maximum:
            maximum = total
        return

    for j in range(N):
        if used[j] == 1:
            continue
        used[j] = 1
        path.append(choice[j])
        find(i+1)
        used[j] = 0
        path.pop()


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    N = int(input())  # 직원들의 번호 및 해야할 일의 번호
    probability = [list(map(int, input().split())) for _ in range(N)]
    choice = [x for x in range(N)]
    path = []
    used = [0]*N
    maximum = 0

    find(0)

    print(maximum)