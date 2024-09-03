import sys

sys.stdin = open('input.txt')

def check_babygin(n, start, player):    # 주어진 리스트로 원소가 3개인 조합을 만들고 그 조합이 run이거나 triplet인지 확인하는 함수
    global find_baby_gin
    if n == 3:
        check = sorted(path)
        if max(check) == min(check):    # triplet일 경우
            find_baby_gin = True    # 찾았다고 표시하고 돌아가기
            return
        elif check[1]-check[0] == 1 and check[2]-check[1] == 1:    # run일 경우
            find_baby_gin = True    # 찾았다고 표시하고 돌아가기
            return
        else:    # 그 외의 경우
            return    # 걍 돌아가기
    for i in range(start, len(player)):    # 조합 만들기
        path.append(player[i])
        check_babygin(n+1, i+1, player)
        path.pop()

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    numbers = list(map(int, input().split()))
    player1 = []    # player 1의 카드
    player2 = []    # player 2의 카드
    path = []    # 조합 만들기 위한 path
    winner = None    # 승자를 담는 변수
    find_baby_gin = False    # 찾았는지 확인하는 변수

    for i in range(len(numbers)):
        if i % 2 == 0:    # 홀수 번째 카드
            player1.append(numbers[i])
            if len(player1) >= 3:    # 3장 이상이 모이면
                check_babygin(0, 0, player1)    # 모인 카드로 만들 수 있는 조합을 찾고 run 혹은 triplet 판별
                if find_baby_gin:    # 찾았으면
                    winner = 1    # 승자 정하고
                    break    # 빠져나오기
        else:    # 짝수 번째 카드
            player2.append(numbers[i])
            if len(player2) >= 3:    # 3장 이상이 모이면
                check_babygin(0, 0, player2)    # 모인 카드로 만들 수 있는 조합을 찾고 run 혹은 triplet 판별
                if find_baby_gin:    # 찾았으면
                    winner = 2    # 승자 정하고
                    break    # 빠져나오기

    # 결과 출력
    if winner == 1:
        print(f'#{tc} {winner}')
    elif winner == 2:
        print(f'#{tc} {winner}')
    else:
        print(f'#{tc} 0')