import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())    # 비트 문자열의 입력 개수
    bit = ''
    for _ in range(N):
        bit += input().strip()    # 하나의 문자열로 받아오기

    result = [0]*(N*10//7)    # 존재하는 숫자만큼 크기의 결과 리스트

    for i in range(0, 10*N-6, 7):    # 전체 문자열 중
        temp = bit[i:i+7]    # 7개씩 끊어서 보기
        for j in range(7):    # temp의 문자 하나하나씩
            num = (2**(6-j))*int(temp[j])    # 2진수로 고려해서
            result[i//7] += num    # 변환하기

    print(f'#{tc}', *result)