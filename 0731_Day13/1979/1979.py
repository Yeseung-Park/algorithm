import sys

sys.stdin = open('input.txt')

def count_x(str, x):
    count = 0
    for i in range(len(str)):
        if str[i] == x:
            count += 1
    return count    # str안에 x의 개수를 세는 함수

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, K = map(int, input().split())    # 변수 받아오기
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr에 퍼즐의 모양을 2차원 리스트로 받아오기

    # 기본적인 접근 방식은 각 행별로, 각 열별로 순회를 해서 해당 행과 열에 K개의 글자가 들어갈 수 있는지 알아보는 것이다.
    # 연속된 1과 그것의 개수를 알아보기 위해서 .split('0')을 쓸 것이다.
    # 그러나 .split은 str 메서드이므로 순회한 행이나 열을 str으로 바꿔서 생각해주는 과정을 거칠 것이다.

    # 행 별 결과 찾기
    result_row = 0    # 행 별 순회하여 나온 K글자가 들어갈 수 있는 공간의 수
    for i in range(N):
        row = ''    # str으로 형변환될 행을 담는 변수로 다음 행으로 넘어갈 때마다 초기화가 되어야 한다.
        for j in range(N):
            row += str(arr[i][j])
        row_list = row.split('0')    # 0을 기준으로 split하면 리스트가 되는데 이를 담는 변수
        for k in range(len(row_list)):    # row_list의 요소들 중
            if count_x(row_list[k], '1') == K:    # 1의 개수가 K개인 요소가 존재한다면
                result_row += 1    # 결과에 1 추가

    # 열 별 결과 찾기 (열 방향으로 순회하기 위해 i와 j의 위치가 바뀐 것 말고는 위와 동일)
    result_col = 0
    for j in range(N):
        col = ''
        for i in range(N):
            col += str(arr[i][j])
        col_list = col.split('0')
        for k in range(len(col_list)):
            if count_x(col_list[k], '1') == K:
                result_col += 1

    result = result_row + result_col    # 최종 결과는 둘을 합한 것

    print(f'#{tc} {result}')