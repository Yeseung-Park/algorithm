import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0    # 회문인 것의 개수를 세는 변수

    # 전체적인 내용은 지난 시간에 했던 회문 찾기와 동일

    # 행 별 회문 찾기
    for i in range(8):
        str_row = ''.join(arr[i])    # 한 행을 문자열로 만들기
        for j in range(0, 8-N+1):
            str_list = []
            for k in range(j, j+N):    # 앞에서부터 N개씩 묶어가기
                str_list.append(str_row[k])
            str = ''.join(str_list)    # 묶은 애들을 문자열로 변환
            if str == str[::-1]:    # 회문일 경우
                count += 1    # count에 1 추가

    # 열 별 회문 찾기를 위해 전치 행렬 만들기
    for i in range(8):
        for j in range(8):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 열 별 회문 찾기
    for i in range(8):    # 행 별 회문 찾기와 동일한 코드
        str_col = ''.join(arr[i])
        for j in range(0, 8-N+1):
            str_list = []
            for k in range(j, j+N):
                str_list.append(str_col[k])
            str = ''.join(str_list)
            if str == str[::-1]:
                count += 1

    print(f'#{tc} {count}')