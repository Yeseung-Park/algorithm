# 최빈수 구하기

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    num = int(input())    # 테스트 케이스 번호
    numbers = list(map(int, input().split()))    # 주어진 수를 리스트로 변환
    num_dict = {}    # 수와 해당 수의 개수를 담을 딕셔너리

    for num1 in numbers:
        count = 0    # 개수 초기 값: 새로운 숫자를 셀 때마다 초기화가 되어야 한다.
        for num2 in numbers:
            if num1 == num2:
                count += 1
                num_dict[num1] = count

    count_list = list(num_dict.values())    # 개수를 담는 리스트

    for i in range(len(count_list)-1, 0, -1):    # count_list 오름차순 정렬
        for j in range(0, i):
            if count_list[j] > count_list[j+1]:
                count_list[j], count_list[j+1] = count_list[j+1], count_list[j]

    maximum_value = count_list[len(count_list)-1]    # 최빈값의 개수
    maximum_key = []    # 최빈값을 담는 리스트

    for key in num_dict:
        if num_dict[key] == maximum_value:
            maximum_key.append(key)

    if len(maximum_key) >= 2:    # 최빈값이 여러개 일 경우 가장 큰 값을 출력하는 조건문
        for i in range(len(maximum_key)-1, 0, -1):
            for j in range(0, i):
                if maximum_key[j] > maximum_key[j+1]:
                    maximum_key[j], maximum_key[j+1] = maximum_key[j+1], maximum_key[j]
        print(f'#{num} {maximum_key[len(maximum_key)-1]}')
    else:    # 최빈값이 하나일 경우 그냥 출력
        print(f'#{num} {maximum_key[0]}')
