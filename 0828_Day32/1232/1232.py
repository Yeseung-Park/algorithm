import sys

sys.stdin = open('input.txt')

def postorder(node):
    global i
    if node == 0:
        return
    postorder(adjL[node][1])
    postorder(adjL[node][2])
    postfix[i] = adjL[node][0]
    i += 1

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    adjL = [[0]*3 for _ in range(N+1)]    # 인접 리스트
    # [키 값, 왼쪽 노드가 가리키는 값, 오른쪽 노드가 가리키는 값]

    for node in arr:
        node_number = int(node[0])
        node_key = node[1]
        if len(node) == 4:
            left_node = int(node[2])
            right_node = int(node[3])

        adjL[node_number][0] = node_key
        if len(node) == 4:
            adjL[node_number][1] = left_node
            adjL[node_number][2] = right_node


    # 트리 만들고 후위 순회 하자.
    postfix = [0]*N    # 후위 순회 한 값들을 담을 리스트
    i = 0
    postorder(1)

    # 후위 표기로 나타낸 수식을 계산
    stack = []    # 계산을 위한 스택
    for num in postfix:
        if num.isdecimal():    # 숫자면
            stack.append(int(num))
        else:
            if num == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                temp = num1+num2
                stack.append(temp)
            elif num == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                temp = num1-num2
                stack.append(temp)
            elif num == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                temp = num1*num2
                stack.append(temp)
            elif num == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                temp = num1/num2
                stack.append(temp)

    result = int(stack.pop())
    print(f'#{tc} {result}')
