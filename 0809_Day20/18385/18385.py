import sys

sys.stdin = open('input.txt')

def devide_team(people, N):    # 2명씩, 혹은 1명씩 짝을 이루는 과정을 나타낸 재귀함수
    global devided_people    # 외부 선언 변수 전역 처리
    if N < 3:    # 만약 만든 그룹이 3명 이하가 되면 (= 2명 혹은 1명이 되었다면)
        devided_people.append(people)    # 대결할 한 그룹이 완성되었다는 것이므로 devided_people에 append
    else:    # 그 외의 경우
        people1 = []    # 반으로 나눌 두 그룹을 담는 리스트 두 가지
        people2 = []    # 이들은 매번 돌 때마다 초기화가 되어야 한다.
        if N % 2 == 0:    # 만약 전체 사람의 수가 짝수라면
            for i in range(0, N//2):    # N//2를 기준으로 나누고
                people1.append(people[i])    # 앞 번호 사람들은 people1에
            for j in range(N//2, N):
                people2.append(people[j])    # 뒷 번호  사람들은 people2에 담아준다
        else:    # 홀수라면
            for i in range(0, N//2+1):    # N//2+1을 기준으로 나누고
                people1.append(people[i])    # 앞 번호 사람들은 people1에
            for j in range(N//2+1, N):
                people2.append(people[j])    # 뒷 번호 사람들은 people2에 담아준다.
        devide_team(people1, len(people1))    # 그렇게 나눠준 그룹에 대해서 한 번 더 함수를 돌려준다.
        devide_team(people2, len(people2))    # 이 함수는 맨 앞의 N < 3을 만족하기 전까지 계속 돌아간다.


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 사람의 수
    people = list(map(int, input().split()))    # 사람들이 가지고 있는 카드

    # 사람들이 가지고 있는 번호와 카드를 동시에 나타내는 리스트 만들기
    people_with_number = list(enumerate(people, start = 1))

    # 팀 나누기
    devided_people = []    # 짝 지은 그룹(2명 or 1명)을 하나의 리스트로 만들고 그렇게 만들어진 여러 그룹들을 하나로 담는 리스트
    devide_team(people_with_number, N)    # 함수 실행

    # 가장 마지막 한 팀을 선정하는 과정
    while len(devided_people) != 1:    # 나눈 그룹이 하나만 남았을 경우 승자를 정해야할 때이므로 while문을 벗어난다.
        winner_list = []    # 각 그룹에서 이긴 사람을 또 담을 리스트로 매번 초기화를 해준다.
        for team in devided_people:    # devided_people에 있는 각 그룹에  대해서
            if len(team) == 1:    # 그룹의 길이가 1이라는 것은 한 명만 있는 그룹이므로
                winner_list.append(team[0])    # 그냥 승자로 올라간다.
            else:    # 그 외의 경우
                if team[0][1] == team[1][1]:    # 비겼을 때는 번호가 더 큰 사람(오름차순으로 번호를 주므로 더 앞에 있는 사람)이 승자이다.
                    winner_list.append(team[0])
                else:    # 그 외의 경우에는
                    if team[0][1] == 1 and team[1][1] == 2:
                        winner_list.append(team[1])
                    elif team[0][1] == 2 and team[1][1] == 3:
                        winner_list.append(team[1])
                    elif team[0][1] == 3 and team[1][1] == 1:
                        winner_list.append(team[1])
                    else:
                        winner_list.append(team[0])    # 가위바위보 결과에 따라서 승자로 올린다.

        devided_people = []    # 새로운 사람들에 대해서 또 그룹을 만들어야 하기 때문에 devided_people을 초기화해준다.
        devide_team(winner_list, len(winner_list))    # 다시 새로운 사람들에 대해서 그룹을 만든다.
        # 이를 한 팀만 남을 때까지 반복

    # 마지막 한 팀에서 최종 승자를 결정하는 과정
    for team in devided_people:    # 이 과정은 위의 과정과 동일하다.
        if len(team) == 1:    # 대신 이겼을 경우 결과로 해당 사람의 번호를 지정한다는 점이 차이점이다.
            result = team[0][0]
        else:
            if team[0][1] == team[1][1]:
                result = team[0][0]
            else:
                if team[0][1] == 1 and team[1][1] == 2:
                    result = team[1][0]
                elif team[0][1] == 2 and team[1][1] == 3:
                    result = team[1][0]
                elif team[0][1] == 3 and team[1][1] == 1:
                    result = team[1][0]
                else:
                    result = team[0][0]

    print(f'#{tc} {result}')    # 결과 출력