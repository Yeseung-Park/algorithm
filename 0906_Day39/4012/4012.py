import sys

sys.stdin = open('input.txt')

def foodA_foodB(n, start):
    global minimum
    if n == N//2:    # 절반 정한다면
        foodA = path[:]
        foodB = []
        for ingredient in ingredients:
            if ingredient not in foodA:
                foodB.append(ingredient)    # foodA를 만들 재료랑 foodB를 만들 재료가 정해진 것
        result = calculate_taste(foodA, foodB)    # 그 두개로 시너지 계산
        if result < minimum:    # 결과가 기존 최소값보다 작으면
            minimum = result    # 갱신~
        return
    for i in range(start, N):
        path.append(ingredients[i])
        foodA_foodB(n+1, i+1)
        path.pop()

def calculate_taste(foodA, foodB):
    # foodA의 맛부터 계산
    foodA_taste = 0
    for i in foodA:
        for j in foodA:
            if synergy[i][j] == 0:
                pass
            else:
                foodA_taste += synergy[i][j]
    # 그 다음 foodB
    foodB_taste = 0
    for i in foodB:
        for j in foodB:
            if synergy[i][j] == 0:
                pass
            else:
                foodB_taste += synergy[i][j]
    # 둘의 맛이 차이 계산
    result = abs(foodA_taste-foodB_taste)
    return result


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N = int(input())    # 음식의 개수
    synergy = [list(map(int, input().split())) for _ in range(N)]
    ingredients = [x for x in range(N)]
    path = []
    minimum = 1e9

    # 기본적인 접근은 음식 재료를 두 팀으로 나눈 다음 각각에 대해서 시너지 계산하기
    # 조합!

    foodA_foodB(0, 0)

    print(f'#{tc} {minimum}')