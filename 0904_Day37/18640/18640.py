import sys

sys.stdin = open('input.txt')

def binary_search(start, end, key, list):
    if start > end:    # 여기까지 왔으면
        return -1    # 해당 키가 리스트에 없다는 것으로 -1 반환
    else:
        mid = (start+end)//2
        if list[mid] == key:
            return mid
        elif list[mid] > key:
            path.append('l')
            return binary_search(start, mid-1, key, list)
        else:
            path.append('r')
            return binary_search(mid+1, end, key, list)

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0

    # A 정렬
    A.sort()

    for number in B:
        path = []
        idx = binary_search(0, len(A)-1, number, A)
        if idx != -1:    # A 안에 존재하는 경우만 생각
            if path == [] or len(path) == 1:    # 그냥 처음부터 가운데 값이거나 찾기 위해 한 번만 탐색했을 경우
                result += 1    # 조건을 만족
            else:
                if path[0] == 'l':    # 왼쪽 탐색부터 시작했다면
                    if ('r' not in path[0::2]) and ('l' not in path[1::2]):    # 짝수 번째 인덱스에는 'l'만, 홀수 번째 인덱스에는 'r'만 있을 때
                        result += 1    # 번갈아가면서 탐색했다는 것
                else:    # 오른쪽 탐색부터 시작했다면
                    if ('l' not in path[0::2]) and ('r' not in path[1::2]):    # 짝수 번째 인덱스에는 'r'만, 홀수 번째 인덱스에는 'l'만 있을 때
                        result += 1    # 번갈아가면서 탐색했다는 것

    print(f'#{tc} {result}')