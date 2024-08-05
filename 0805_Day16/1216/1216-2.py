import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):
    _ = int(input())
    arr = [list(input()) for _ in range(100)]

    maximum = 0    # 최대 길이를 구해주기 위한 기본 값

    # 행 별 검색
    for i in range(100):    # 각 행에 대해서
        for j in range(100, 0, -1):    # 가장 긴 길이의 문자열부터
            for k in range(0, 100-j+1):    # 문자열의 첫 시작점
                str_list = arr[i][k:k+j]
                if str_list == str_list[::-1]:    # 회문이라면
                    result = len(str_list)    # 결과로 지정하고
                    if result > maximum:    # maximum보다 크면
                        maximum = result    # 새로운 maximum으로 지정
                        break

    # 열 별 검색을 위한 전치 행렬 만들기
    for i in range(100):
        for j in range(100):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 열 별 검색
    for i in range(100):    # 각 행에 대해서
        for j in range(100, 0, -1):    # 가장 긴 길이의 문자열부터
            for k in range(0, 100-j+1):    # 문자열의 첫 시작점
                str_list = arr[i][k:k+j]
                if str_list == str_list[::-1]:    # 회문이라면
                    result = len(str_list)    # 결과로 지정하고
                    if result > maximum:    # maximum보다 크면
                        maximum = result    # 새로운 maximum으로 지정
                        break

    print(f'#{tc} {maximum}')