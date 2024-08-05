import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    A, B = input().split()

    new_A = A.replace(B, 'a')

    print(f'#{tc} {len(new_A)}')