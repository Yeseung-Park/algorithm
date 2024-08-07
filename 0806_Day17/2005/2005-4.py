# Tabulation 방식으로 파스칼의 삼각형을 구현하는 방법

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())

    # Bottom-up으로 진행
    # 작은 것을 해결한 결과를 이용해서 큰 것을 해결

    print(f'#{tc}')
    before_list = [1]
    print(*before_list)

    for _ in range(N-1):    # 첫 번째 줄은 이미 해결을 했기 때문에 N-1
        temp_list = []    # 층 별로 새롭게 계산된 값이 저장되어야 하기에 초기화 위치는 N이 반복될 때 위치해야 함
        temp_list.append(1)    # 가장 왼쪽의 1
        for i in range(len(before_list)-1):    # 계산되어야 하는 횟수는 이전 리스트의 길이-1
            # 두 수를 합해서 temp_list에 저장
            result = before_list[i] + before_list[i+1]
            temp_list.append(result)
        temp_list.append(1)    # 가장 오른쪽의 1

        print(*temp_list)
        before_list = temp_list