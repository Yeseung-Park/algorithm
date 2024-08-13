import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 연속된 N일 동안 물건의 매매가를 알 수 있다.
    prices = list(map(int, input().split()))    # 연속된 N일 동안의 물건의 매매가
    selling_price = 0    # 팔아야 하는 가격

    for i in range(N-1, -1, -1):    # 거꾸로 보면서
        if prices[i+1] > prices[i]:    # 가격이 증가하면 반대로 가격이 떨어졌다는 것이므로
            pass    # 아무것도 하지마
        else:
            if prices[i] > selling_price:
                selling_price = prices[i]

