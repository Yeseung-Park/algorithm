import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):

    _ = int(input())
    arr = [list(input()) for _ in range(100)]

    maximum = 0

    # 행 별 길이에 따른 회문 찾기
    for i in range(100):
        str_row = arr[i]
        for j in range(100, 0, -1):    # 가질 수 있는 모든 문자열의 길이에 대해 찾아보기
            for k in range(0, 100-j+1):
                str_list = str_row[k:k+j]
                str = ''.join(str_list)
                print(str)
                # if str == str[::-1]:
                #     result = len(str)
                #     if result > maximum:
                #         maximum = result

    # 열 별 길이에 따른 회문 찾기를 위한 전치 행렬 만들기
    # for i in range(100):
    #     for j in range(100):
    #         if i < j:
    #             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    #
    # # 열 별 길이에 따른 회문 찾기
    # for i in range(100):    # 행 별 길이에 따른 회문 찾기와 동일
    #     str_col = arr[i]
    #     for j in range(100, 0, -1):
    #         for k in range(0, 100-j+1):
    #             str_list = str_row[k:k+j]
    #             str = ''.join(str_list)
    #             if str == str[::-1]:
    #                 result = len(str)
    #                 if result > maximum:
    #                     maximum = result
    #
    # print(f'#{tc} {maximum}')