import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    A, B, C = map(int, input().split())
    result = 0

    while True:
        # 뒤에서부터 비교하자
        if C < 3 or B < 2:    # 계속 먹어도 X
            result = -1
            break
        if A < B < C:
            break
        if B >= C:
            result += B-C+1
            B -= B-C+1
            if A < B < C:
                break
        if A >= B:
            result += A-B+1
            A -= A-B+1
            if A < B < C:
                break

    print(f'#{tc} {result}')