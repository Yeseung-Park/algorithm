import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0    # 꽃가루의 최댓값을 담는 변수

    for i in range(N):
        for j in range(M):
            flower_sum = arr[i][j]    # 하나의 요소를 터뜨렸을 때 나오는 꽃가루의 수를 담는 변수로 다음 요소로 이동할 때마다 초기화 된다.
            num = arr[i][j]    # 처음 터뜨린 풍선의 꽃가루 수만큼 좌우상하의 풍선을 탐색해야 하므로 해당 값을 저장해주고
            for k in range(1, num+1):    # 그만큼 반복문을 돌린다.
                di = [0, k, 0, -k]
                dj = [k, 0, -k, 0]    # 상하좌우로 k칸 옆에 있는 요소 탐색
                for l in range(4):
                    ni = i + di[l]
                    nj = j + dj[l]
                    if 0 <= ni < N and 0 <= nj < M:
                        flower_sum += arr[ni][nj]
            if maximum < flower_sum:
                maximum = flower_sum    # 터뜨린 풍선의 모든 꽃가루 수가 maximum보다 크면 그게 새로운 maximum

    print(f'#{tc} {maximum}')