import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    print(T)    # 테스트 케이스 갯수가 잘 들어오는지 확인
    # 입력을 리스트로 변환
    # print(list(map(int, input().split())))  # input 함수는 파일 한 줄씩 문자열 형태로 받아옴
    # a, b, c, d = map(int, input().split())
    # print(a, c, b, d)

    print(list(input()))    # 문자열은 이렇게 받아오기 (굳이 split()이나 map()이 필요없다.)