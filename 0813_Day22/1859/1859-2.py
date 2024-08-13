import sys

sys.stdin = open('input.txt')

def find_index(list, x):
    idx_list = []
    for i in range(len(list)):
        if list[i] == x:
            idx_list.append(i)
    return idx_list

def find_maximum_profit(list):
    if len(list) == 0:



# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 연속된 N일 동안 물건의 매매가를 알 수 있다.
    prices = list(map(int, input().split()))    # 연속된 N일 동안의 물건의 매매가
    expense = 0    # 사용한 돈
    stuff = 0    # 현재 가지고 있는 물건의 개수
    max_price = 0

    # 이번에는 최대로 팔 수 있는 날까지 존버했다가 팔아야지
    # 그 이후에는 어떻게 할까 원래대로 할까

    while i

    for price in prices:
        if price > max_price:
            max_price = price

    print(max_price)
    when_max_price = find_index(prices, max_price)
    print(when_max_price)    # 이거의 길이가 최고가가 나타나는 횟수

    sell = 0    # 최고가에 판 횟수
    i = 0    # 하루하루

    while sell < len(when_max_price):
        if prices[i] != max_price:
            expense -= prices[i]
            stuff += 1
            i += 1
        else:
            expense += prices[i] * stuff
            stuff = 0
            sell += 1
            i += 1

    for j in range(i, N):
        if j+1 != N:    # 마지막 날이 아닌 경우
            if prices[j+1] < prices[j]:    # 다음 날에 가격이 떨어졌을 경우 오늘 팔아야 한다.
                expense += prices[j] * stuff
                stuff = 0
            else:    # 다음날이 더 비쌀 경우 일단 사야한다.
                expense -= prices[j]
                stuff += 1
        else:    # 마지막 날인 경우
            expense += prices[j] * stuff    # 무조건 팔기

    # # 최대로 팔 수 있는 날까지 기다리고 만약
    # # 근데 최대로 팔 수 있는 날이 많으면?
    # for i in range(N):
    #     if i+1 != N:    # 마지막 날이 아닌 경우
    #         if prices[i] != max_price:    # 오늘의 가격이 최대로 팔 수 있는 가격이 아닌 경우
    #             expense -= prices[i]
    #             stuff += 1    # 일단 산다.
    #         else:    # 오늘의 가격이 최대로 팔 수 있는 가격일 경우
    #             expense += prices[i] * stuff
    #             stuff = 0    # 다 판다.
    #     else:    # 마지막 날인 경우
    #         expense += prices[i] * stuff    # 무조건 팔기


    # print(max_price)
    print(expense)

    # for i in range(len(prices)):
    #     if i+1 != len(prices):    # 마지막 날이 아닌 경우
    #         if prices[i+1] < prices[i]:    # 다음 날에 가격이 떨어졌을 경우 오늘 팔아야 한다.
    #             expense += prices[i] * stuff
    #             stuff = 0
    #         else:    # 다음날이 더 비쌀 경우 일단 사야한다.
    #             expense -= prices[i]
    #             stuff += 1
    #     else:    # 마지막 날인 경우
    #         expense += prices[i] * stuff    # 무조건 팔기
    #
    # print(expense)