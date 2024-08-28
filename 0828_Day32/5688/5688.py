import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())
    temp = round(N**(1/3))

    if int(temp)**3 == N:
        print(f'#{tc} {int(temp)}')
    else:
        print(f'#{tc} -1')