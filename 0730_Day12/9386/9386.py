import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    numbers = input()

    # 문자열 상태 그대로 받아온 입력값을 '0'을 기준으로 분리하기
    # 연속된 1만 가진 문자열을 따로 얻기 위해
    new_number = numbers.split('0')

    # 최댓값을 찾기 위해 오름차순으로 정렬하되 문자열의 길이가 중요하므로 각 요소의 길이를 기준으로 정렬
    for i in range(len(new_number)-1, 0, -1):
        for j in range(0, i):
            if len(new_number[j]) > len(new_number[j+1]):
                new_number[j], new_number[j+1] = new_number[j+1], new_number[j]

    maxi = len(new_number[-1])

    print(f'#{tc} {maxi}')


