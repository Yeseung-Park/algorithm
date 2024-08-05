import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    A, B = input().split()

    N = len(A)
    M = len(B)
    i = 0
    j = 0

    new_A = A.replace(B, 'a')

    print(len(new_A))


    # while i < N and j < M:
    #     if A[i] == B[j]:
    #         i += 1
    #         j += 1
    #     else:
    #         i = i-j+1
    #         j = 0
    # if j == M:
    #     start_idx = i-M
    #
    # print(start_idx)
    #
    # for i in range(start_idx, start_idx+M):


    # print(A)
    # print(B)