import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0    # 죽인 파리의 최댓값으로 초기값은 0으로 지정

    # M*M 파리채의 가장 왼쪽 위의 원소를 기준으로 배열 크기만큼 순회하면서 더해주고 최댓값을 찾는 방식

    for i in range(0, N-M+1):    # 기준 원소의 행(i)과 열(j)값을 지정하는 부분
        for j in range(0, N-M+1):    # N-M+1 까지인 이유는 그 이상을 기준 요소의 행과 열로 지정할 경우 M*M이 기존 행렬을 벗어나기 때문에
            s = 0    # M*M 크기의 배열의 원소의 합을 담는 변수로 기준이 되는 원소가 바뀔 때마다 초기화
            for k in range(M):    # 기준 원소를 시작으로 가로 M, 세로 M 이내의 원소들을 순회
                for l in range(M):    # 기준 원소를 시작으로 가로 M, 세로 M 이내의 원소들을 순회
                    if 0 <= i+k < N and 0 <= j+l < N:    # 위에서 기준 원소의 행과 열 값을 N-M+1로 제한해줬지만 한 번 더 인덱스를 벗어난 경우 제외
                        s += arr[i+k][j+l]    # 순회하면서 하나씩 더해주기
            if maximum < s:    # 만약 순회하면서 더한 값이 maximum보다 크다면
                maximum = s    # maximum은 s

    print(f'#{tc} {maximum}')