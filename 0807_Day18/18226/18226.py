import sys

sys.stdin = open('input.txt')

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())
    arr = []    # 10cm 종이와 20cm 종이 개수의 순서쌍을 담는 리스트
    result = 0    # 결과를 담을 변수

    # i는 10cm 종이의 개수를, j는 20cm 종이의 개수를 의미
    for i in range(N//10+1):
        for j in range(N//20+1):
            pair = [0]*2
            if 10*i+20*j == N:    # 해당 식을 만족하면
                pair[0] = i    # i는 pair의 첫 번째 요소로
                pair[1] = j    # j는 pair의 두 번째 요소로 넣기
                arr.append(pair)

    for pair in arr:
        if pair[1] == 0:    # 20cm 종이가 없는 경우
            result += 1    # 경우의 수는 하나니까 +1
        else:
            result_1 = fact(pair[0]+pair[1])/(fact(pair[0])*fact(pair[1]))    # 10cm와 20cm가 섞여 있을 때 그걸 나열하는 경우의 수
            result_2 = result_1*(2**pair[1])    # 20cm를 10cm 2개로 나눌 수 있으므로 그것까지 고려한 최종 경우의 수
            result += result_2    # 경우의 수에 result_2 더하기

    print(f'#{tc} {int(result)}')