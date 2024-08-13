import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 연속된 N일 동안 물건의 매매가를 알 수 있다.
    price = list(map(int, input().split()))    # 연속된 N일 동안의 물건의 매매가
    expense = 0    # 사용한 돈

    for i in range(N-1, 0, -1):
        if price[i] < price[i-1]:
            pass
        else:
            expense += price[i] - price[i-1]
            price [i-1] = price[i]

    print(f'#{tc} {expense}')