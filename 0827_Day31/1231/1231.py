import sys

sys.stdin = open('input.txt')

def inorder(node):    # 왼쪽->루트->오른쪽
    if node == 0:
        return
    inorder(left_adjL[node])
    inorder_list.append(num_dict[node])
    inorder(right_adjL[node])

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())
    arrange = [list(input().split()) for _ in range(N)]

    left_adjL = [0]*(N+1)
    right_adjL = [0]*(N+1)
    num_dict = {}    # 노드에 따른 글자를 저장하는 딕셔너리

    for arr in arrange:    # 인접 리스트 만들기
        num_dict[int(arr[0])] = arr[1]    # 딕셔너리에 번호랑 글자 저장
        if len(arr) == 3:    # 왼쪽만 채워져 있으면
            left_adjL[int(arr[0])] = int(arr[2])    # 하나만 채우고
        elif len(arr) == 4:    # 둘 다 채워져 있으면
            left_adjL[int(arr[0])] = int(arr[2])
            right_adjL[int(arr[0])] = int(arr[3])    # 둘 다 채우기

    inorder_list = []
    inorder(1)    # 중위순회
    result = ''.join(inorder_list)    # 원하는대로 결과 출력


    print(f'#{tc} {result}')

