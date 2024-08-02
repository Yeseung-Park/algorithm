import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr1 = [list(input()) for _ in range(N)]
    arr2 = [[0]*N for _ in range(N)]

    # 열 별 순회한 값을 담은 arr2
    for j in range(N):
        for i in range(N):
            arr2[j][i] = arr1[i][j]

    # 행 별 순회하면서 회문 찾기
    for i in range(N):
        str_row_all = ''.join(arr1[i])
        for j in range(0, N-M+1):
            str_row = str_row_all[j:j+M]    # M만큼의 길이를 가진 연속된 str만 떼어주기
            for k in range(0, M//2):
                if str_row[k] != str_row[M-1-k]:
                    palindrom = False
                    break
                else:
                    palindrom = True
            if palindrom == True:    # 회문이 맞다면
                result = str_row    # 결과로 등록
                break

    # 열 별 순회하면서 회문 찾기 (행에서 못 찾았을 때)
    if palindrom == False:
        for i in range(N):
            str_col_all = ''.join(arr2[i])
            for j in range(0, N-M+1):
                str_col = str_col_all[j:j+M]
                for k in range(0, M//2):
                    if str_col[k] != str_col[M-k-1]:
                        palindrom = False
                        break
                    else:
                        palindrom = True
                if palindrom == True:
                    result = str_col
                    break

    print(f'#{tc} {result}')