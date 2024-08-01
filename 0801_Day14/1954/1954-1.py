import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [[0]*N for _ in range(N)]
    i, j = 0, 0
    arr[0][0] = 1
    num = 1
    move = 1

    while move < N**2:

        right = True
        left = True
        up = True
        down = True

        while right:
            j += 1
            if 0 <= j < N and arr[i][j] == 0:
                num += 1
                arr[i][j] = num
                move += 1
            else:
                j -= 1
                right = False

        while down:
            i += 1
            if 0 <= i < N and arr[i][j] == 0:
                num += 1
                arr[i][j] = num
                move += 1
            else:
                i -= 1
                down = False

        while left:
            j -= 1
            if 0 <= j < N and arr[i][j] == 0:
                num += 1
                arr[i][j] = num
                move += 1
            else:
                j += 1
                left = False

        while up:
            i -= 1
            if 0 <= i < N and arr[i][j] == 0:
                num += 1
                arr[i][j] = num
                move += 1
            else:
                i += 1
                up = False

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
