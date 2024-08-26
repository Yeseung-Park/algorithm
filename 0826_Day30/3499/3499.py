import sys

sys.stdin = open('input.txt')

def divide_half(list, N):
    if N % 2 == 0:    # 짝수라면
        return list[0:N//2], list[N//2:]
    else:    # 홀수라면
        return list[0:N//2+1], list[N//2+1:]

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())

    cards = list(input().split())

    cards1, cards2 = divide_half(cards, N)

    for i in range(N//2):
        cards1.insert(i*2+1, cards2[i])

    print(f'#{tc}', *cards1)