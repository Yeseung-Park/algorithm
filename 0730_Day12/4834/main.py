# 최빈수 구하기

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 카드 장수
    number = list(map(int, input()))    # 주어진 연속된 숫자를 각각 리스트로 분리
    count_dict = {}    # 각 카드 별 장수를 기록하는 딕셔너리

    for num1 in number:
        count = 0    # 카드 별 장수를 체크하는 변수: 새로운 숫자를 다룰 때마다 초기화가 되어야 한다.
        for num2 in number:
            if num1 == num2:
                count += 1
                count_dict[num1] = count

    count_value = list(count_dict.values())    # 카드 별 장수만 담은 리스트

    for i in range(len(count_value)-1, 0, -1):    # 장수 중 최댓값을 찾기 위한 정렬
        for j in range(0, i):
            if count_value[j] > count_value[j+1]:
                count_value[j], count_value[j+1] = count_value[j+1], count_value[j]

    maximum_value = count_value[-1]
    maximum_key = []    # 최빈값을 담는 리스트 (최빈값이 여러 개 일 경우 대비)

    for key in count_dict:
        if count_dict[key] == maximum_value:
            maximum_key.append(key)

    if len(maximum_key) >= 2:
        for i in range(len(maximum_key)-1, 0, -1):  # 장수 중 최댓값을 찾기 위한 정렬
            for j in range(0, i):
                if maximum_key[j] > maximum_key[j + 1]:
                    maximum_key[j], maximum_key[j + 1] = maximum_key[j + 1], maximum_key[j]
        real_maxi = maximum_key[-1]
        print(f'#{tc} {real_maxi} {count_dict[real_maxi]}')
    else:
        real_maxi = maximum_key[0]
        print(f'#{tc} {real_maxi} {count_dict[real_maxi]}')