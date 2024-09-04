import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, X = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 약간 stack으로 접근하면 좋을 것 같기도?
    # 행 먼저 탐색
    for i in range(N):
        stack = []    # 지형의 높이를 차례대로 저장하는 스택
        is_land_okay = True    # 활주로 건설이 가능한지 확인하는 변수
        for j in range(N):
            if not stack:    # 스택이 비어있으면
                stack.append(land[i][j])
                # 별다른거 보지 않고 넣기
            else:    # 그 외의 경우에는
                if stack[-1] == land[i][j]:    # 이전 지형이랑 높이가 동일하면
                    stack.append(land[i][j])    # 넣기
                elif abs(stack[-1]-land[i][j]) >= 2:    # 높이차가 1보다 크면 안 돼!
                    is_land_okay = False
                    break
                else:
                    if stack[-1] > land[i][j]:    # 더 낮은 높이의 지형을 만났을 경우
                        if land[i][j:j+X] == [land[i][j]]*X:    # X 만큼 지형이 반복될 경우
                            stack.append(land[i][j])    # 활주로 건설 쌉가능이므로 계속 탐색
                        else:
                            is_land_okay = False
                            break
                    else:    # 더 높은 높이의 지형을 만났을 경우
                        if stack[-X::] == [stack[-1]]*X:    # X 만큼 지형이 반복되었을 경우
                            stack.append(land[i][j])    # 활주로 건설 쌉가능이므로 계속 탐색
                        else:
                            is_land_okay = False
                            break
        if is_land_okay:
            result += 1

    # 그냥 전치행렬 만들어줘야 할 것 같다...
    for i in range(N):
        for j in range(N):
            if i < j:
                land[i], land[j] = land[j], land[i]

    # 열 탐색이 조금 이상하다... 문제점은 알겠는데 집 가서 생각해보자

    # 그 후 열 탐색
    for i in range(N):
        stack = []  # 지형의 높이를 차례대로 저장하는 스택
        is_land_okay = True  # 활주로 건설이 가능한지 확인하는 변수
        for j in range(N):
            if not stack:  # 스택이 비어있으면
                stack.append(land[i][j])
                # 별다른거 보지 않고 넣기
            else:  # 그 외의 경우에는
                if stack[-1] == land[i][j]:  # 이전 지형이랑 높이가 동일하면
                    stack.append(land[i][j])  # 넣기
                elif abs(stack[-1] - land[i][j]) >= 2:  # 높이차가 1보다 크면 안 돼!
                    is_land_okay = False
                    break
                else:
                    if stack[-1] > land[i][j]:  # 더 낮은 높이의 지형을 만났을 경우
                        if land[i][j:j + X] == [land[i][j]] * X:  # X 만큼 지형이 반복될 경우
                            stack.append(land[i][j])  # 활주로 건설 쌉가능이므로 계속 탐색
                        else:
                            is_land_okay = False
                            break
                    else:  # 더 높은 높이의 지형을 만났을 경우
                        if stack[-X::] == [stack[-1]] * X:  # X 만큼 지형이 반복되었을 경우
                            stack.append(land[i][j])  # 활주로 건설 쌉가능이므로 계속 탐색
                        else:
                            is_land_okay = False
                            break
        if is_land_okay:
            result += 1

    print(land)
    print(result)