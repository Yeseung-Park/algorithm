import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 연속된 N일 동안 물건의 매매가를 알 수 있다.
    price = list(map(int, input().split()))    # 연속된 N일 동안의 물건의 매매가
    expense = 0    # 사용한 돈
    stuff = 0    # 현재 가지고 있는 물건의 개수

    # 최대로 팔 수 있는 날까지 존버하다가 팔아야하나?
    # 우선 이건 처음 접근 방법

    for i in range(len(price)):
        if i+1 != len(price):    # 마지막 날이 아닌 경우
            if price[i+1] < price[i]:    # 다음 날에 가격이 떨어졌을 경우 오늘 팔아야 한다.
                expense += price[i] * stuff
                stuff = 0
            else:    # 다음날이 더 비쌀 경우 일단 사야한다.
                expense -= price[i]
                stuff += 1
        else:    # 마지막 날인 경우
            expense += price[i] * stuff    # 무조건 팔기

    print(expense)