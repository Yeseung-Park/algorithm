import sys

sys.stdin = open('input.txt')

def find(i, N, total, complete):    # 시작 사람 번호(항상 0), 전체 사람 수, 확률 담는 변수, 한 일인지 확인하는 리스트
    # 사실 complete은 인자로 안 받아도 되는데 디버깅 확인해주려고 넣음
    global maximum
    if i == N:    # 모든 일을 봤으면
        if total > maximum:    # 최댓값 갱신
            maximum = total
        return

    if total <= maximum:    # 확률은 곱하면 곱할 수록 작아지기 때문에 이미 작아졌다는건 더 작아질 수밖에 없다.
        return    # 이건 안 되는 경로야 돌아가기
    # 이게 진짜 핵심이다. 백트래킹!

    for j in range(N):    # 일 하나하나 보기
        if j in complete:    # 이미 한 일이면 넘어가기
            continue
        complete.append(j)    # 일 했다고 표시해주고
        find(i+1, N, total*(probability[i][j]*0.01), complete)    # 다음 일에 대해서 재귀 ㄱㄱ total도 갱신
        complete.pop()    # 여기로 돌아왔다는건 다시 보겠다는 것이므로 했던 일에서 빼주기

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())    # 직원들의 번호 및 해야할 일의 번호
    probability = [list(map(int, input().split())) for _ in range(N)]
    complete = []    # 이미 완료한 일을 담는 리스트
    maximum = 0    # 최댓값 담는 변수
    total = 1    # 초기 값

    find(0, N, total, complete)

    print(f'#{tc} {maximum*100:.6f}')

