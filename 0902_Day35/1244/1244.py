import sys

sys.stdin = open('input.txt')

def decide_change(n):
    if n == 2:
        change_card_list.append(change_card[:])
        return
    for i in range(len(numbers)):
        if used1[i] == True:
            continue
        used1[i] = True
        change_card.append(i)
        decide_change(n+1)
        change_card.pop()
        used1[i] = False

def change(n):
    global maximum
    if n == change_num:
        result = 0
        for j in range(len(numbers)):
            result += numbers[j]*(10**(len(numbers)-1-j))
        if result > maximum:
            maximum = result
        return
    for i in range(len(change_card_list)):
        if numbers[change_card_list[i][0]] == numbers[change_card_list[i][1]]:
            continue
        numbers[change_card_list[i][0]], numbers[change_card_list[i][1]] = numbers[change_card_list[i][1]], numbers[change_card_list[i][0]]
        change(n+1)
        numbers[change_card_list[i][0]], numbers[change_card_list[i][1]] = numbers[change_card_list[i][1]], numbers[change_card_list[i][0]]

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    temp1, temp2 = input().split()
    numbers = list(map(int, temp1))
    change_num = int(temp2)
    change_count = 0
    change_card_list = []    # 교환할 카드의 인덱스 담는 변수
    change_card = []
    used1 = [False]*len(numbers)
    used2 = [False]*len(change_card_list)
    maximum = 0

    decide_change(0)
    print(change_card_list)

    change(0)

    print(maximum)