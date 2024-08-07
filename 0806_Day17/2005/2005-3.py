import sys

sys.stdin = open('input.txt')

# top down 방식 / 메모이제이션
def pascal(row, col):

    # 가장 바깥 요소이기 때문에 무조건 1 (파스칼 삼각형이니 바깥요소 1맞아)
    if col == 0 or col == row:
        memo[row][col] = 1
        return 1

    # 중복 계산을 하지 않기 위해
    if memo[row][col] != -1:  #이미 계산된 값이 있다면
        return memo[row][col] # 계산된 값을 사용한다.


    # 이전요소의 값을 더한값이 현재 위치의 값이됨.
    memo[row][col] = pascal(row-1, col-1) + pascal(row-1, col)    #  = 현재위치의 갓,
    return memo[row][col] # 현재코드는 중복값을 계속 계산하고있음.


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input()) # N: 파스칼 삼각형 높이
    # 값을 저장하기 위해 memo라는 2차원 리스트 생성
    memo = [[-1] * i for i in range(1, N+1)] # i는 0부터 N까지 반복될것임.
    memo[0][0] = 1 # 꼭대기는 항상 1임


    # memoization은 Top - down 방식
    # 큰 범위에서 작은 범위로 처리됨.
        # 재귀를 이용해서 풀이
    for col in range(N): #파스칼의 높이만큼 반복하면되는것임.
        pascal(N-1, col)
    print(f'#{tc}')
    for i in range(N):
        print(*memo[i])