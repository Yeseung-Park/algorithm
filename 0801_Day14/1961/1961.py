import sys
import copy

sys.stdin = open('input.txt')

def turn_90(arr):
    # 기본적인 원리는 전치 행렬 + 좌우 뒤집기

    # 전치 행렬
    for i in range(N):
        for j in range(N):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 좌우 뒤집기
    for i in range(N):
        for j in range(N // 2):
            arr[i][j], arr[i][N - 1 - j] = arr[i][N - 1 - j], arr[i][j]

    return arr

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = turn_90(arr)    # 90도만큼 회전
    arr_180 = turn_90(copy.deepcopy(arr_90))    # 180도만큼 회전
    arr_270 = turn_90(copy.deepcopy(arr_180))    # 270도만큼 회전
    # 꼭 깊은 복사를 해주어야 한다.

    # 이 이후로는 요구하는 대로 출력하는 과정
    total_result = []    # 최종 결과를 담을 리스트

    for i in range(N):
        result_90 = ''.join(map(str, arr_90[i]))    # 한 행에 담긴 요소를 하나의 string으로 변환하는 과정
        result_180 = ''.join(map(str, arr_180[i]))
        result_270 = ''.join(map(str, arr_270[i]))

        result = [result_90, result_180, result_270]    # 다양한 각도로 회전한 결과의 동일한 행을 하나의 리스트로 지정

        total_result.append(result)    # 그렇게 만들어진 새로운 리스트를 최종 결과에 하나로 담기

    print(f'#{tc}')
    for i in range(N):
        print(*total_result[i])    # 최종 결과 리스트 하나씩 출력하기