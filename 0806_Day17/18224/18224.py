import sys

sys.stdin = open('input.txt')

def bracket_right(arr):    # 괄호가 제대로 짝지어졌는지 확인하는 함수
    stack = []
    for bracket in arr:
        if bracket == '(':    # '('가 등장했다면 stack에 집어넣기
            stack.append(bracket)
        elif bracket == '{':    # '{'가 등장했다면 stack에 집어넣기
            stack.append(bracket)
        elif bracket == ')':    # ')'가 등장했다면 stack의 제일 위에 위치한 요소를 가져와서 비교하기
            temp = stack.pop()
            if temp != '(':    # 만약 그렇게 가져온 요소가 '('이 아닐 경우
                break    # 짝이 맞지 않다는 것이므로 그냥 바로 빠져나가기
        elif bracket == '}':    # '}'가 등장했다면 stack의 제일 위에 위치한 요소를 가져와서 비교하기
            temp = stack.pop()
            if temp != '{':    # 만약 그렇게 가져온 요소가 '{'이 아닐 경우
                break    # 짝이 맞지 않다는 것이므로 그냥 바로 빠져나가기
        else:
            pass    # 그 외의 문자에 대해서는 그냥 무시하기

    if stack != []:    # 위 과정을 다 하고 난 다음 stack에 무언가가 남아있을 경우
        return 0    # 짝이 맞지 않는 것이므로 return 0
    else:
        return 1    # 그 외의 경우 결과가 잘 나온 것이므로 return 1

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    arr = list(input())

    result = bracket_right(arr)

    print(f'#{tc} {result}')