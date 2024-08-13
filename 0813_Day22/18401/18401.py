import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())    # N: 화덕의 크기    M: 피자의 개수
    C = list(map(int, input().split()))    # 치즈의 양
    Cheese = [0] * M
    for i in range(1, M+1):
        Cheese[i-1] = [i, C[i-1]]    # 치즈의 양을 피자 번호와 함께 리스트로 저장
    oven = [0] * N    # 화덕
    pizza = []    # 다 구워진 피자를 담을 리스트

    # 우선 빈 화덕에 앞에서부터 피자 다 넣기
    for i in range(N):
        oven[i] = Cheese.pop(0)

    while len(pizza) < M:    # 피자가 다 구워질 때까지
        rear = 0    # rear는 0
        while rear < N:    # 화덕 한 바퀴 돌 때까지
            if oven[rear] == 0:    # 빈 자리는 0으로 표현할 것이므로 0인 경우 피자가 없다는 것이므로
                pass    # pass
            else:    # 그 외의 경우는 피자가 있다는 것이므로
                if oven[rear][1] < 1:    # 피자의 치즈 양이 1보다 작을 경우 다 구워졌다는 것이므로
                    pizza.append(oven[rear])    # pizza 리스트에 추가하고
                    if Cheese:    # 아직 남아있는 피자가 있을 경우
                        oven[rear] = Cheese.pop(0)    # 완성된 피자 자리에 새로운 피자를 넣고
                    else:    # 남아있는 피자가 없을 경우
                        oven[rear] = 0    # 그냥 빈 공간으로 두기
            rear += 1    # 다음 화덕 자리에 대해서 탐색
        for i in range(N):    # 화덕을 한 바퀴 돌았다면 남아있는 피자에 대해
            if oven[i] == 0:    # 피자가 없는 경우
                pass    # 넘어가고
            else:    # 피자가 있는 경우
                oven[i][1] = oven[i][1] // 2    # 피자의 치즈를 절반으로 줄이기

    result = pizza[-1][0]    # 결과는 마지막으로 구워진 피자의 번호, 즉 pizza 리스트의 제일 마지막에 있는 피자

    print(f'#{tc} {result}')