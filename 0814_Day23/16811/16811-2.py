import sys
sys.stdin = open('input.txt')

# 문제 분석
# 1. 소, 중, 대 박스에 나누어 포장
# 2. 같은 크기의 당근은 같은 상자에
# 3. 빈 상자가 있어서는 안 된다.
# 4. 한 상자에 N // 2개를 초과하는 당근이 있어서는 안 된다.
# 5. 1 ~ 4번 조건을 만족하면서, 각 상자에 든 당근 개수 차이 최소화
# 이 개수 차이를 return
# 조건 만족할 수 없을 때 -1

# 접근
# 모든 조합을 구한다.
# 조건을 통과하는 것 중에서 최소 차이를 return 한다.
# 정렬하고, 인덱스 만으로 조합을 구한다.

# TestCase 개수
T = int(input())

# TestCase만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()  # 정렬

    min_diff = 1e9
    isDone = False

    for i in range(1, n - 1): # 작은 상자 크기
        if carrots[i] == carrots[i - 1]: # 조건 2. 같은 값이면 continue
            continue

        for j in range(i + 1, n): # 중간 상자 크기
            if carrots[j] == carrots[j - 1]: # 조건 2. 같은 값이면 continue
                continue

            small = i
            medium = j - i
            large = n - j

            # 조건 3
            if small == 0 or medium == 0 or large == 0:
                continue

            # 조건 4
            if small > n // 2 or medium > n // 2 or large > n // 2:
                continue

            isDone = True
            diff = max(small, medium, large) - min(small, medium, large)
            min_diff = min(min_diff, diff)

    if isDone:
        print(f'#{tc} {min_diff}')
    else:
        print(f'#{tc} -1')
