import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    str1 = input()
    str2 = input()

    count_dict = {}    # str1의 문자 하나하나의 개수를 담기 위한 딕셔너리
    # 문자 : 개수

    for string in str1:
        count_dict[string] = 0    # 초기값은 0으로 정해준다.

    keys = list(count_dict.keys())    # count_dict의 키 값을 담은 리스트

    for string2 in str2:    # 만약 str2의 문자 중
        for key in keys:
            if key == string2:    # keys의 요소와 동일한 문자가 있다면
                count_dict[key] += 1    # 해당 key의 값에 1 추가

    values = list(count_dict.values())    # count_dict의 값을 담은 리스트
    max_value = 0    # values의 최댓값을 구하기 위한 기본 값

    for value in values:
        if value > max_value:
            max_value = value    # count_dict의 값 중 최댓값 구하기

    print(f'#{tc} {max_value}')