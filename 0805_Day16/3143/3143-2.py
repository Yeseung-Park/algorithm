import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    text, pattern = input().split()
    typing = 0

    i = 0
    M = len(pattern)
    N = len(text)

    while i < N:    # 주어진 text를 다 순회할 때까지
        if text[i:i+M] == pattern:    # 만약 패턴이 존재한다면
            typing += 1    # 타이핑 횟수를 한 번만 늘리고
            i += M    # 패턴 길이만큼 건너뛰고 거기서부터 다시 탐색
        else:    # 그 외의 경우
            typing += 1
            i += 1    # 한글자씩 탐색하고 타이핑 횟수도 한글자씩 늘리기


    print(f'#{tc} {typing}')