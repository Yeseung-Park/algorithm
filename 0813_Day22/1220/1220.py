import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    N = int(input())    # 정사각형 테이블의 한 변의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_magnetic = [0] * N    # 열 별 자석의 배치 상태를 담는 리스트
    result = 0    # 교착 상태의 개수를 담는 변수

    # 일단 열 별로 모으기
    for j in range(N):
        magnetic = []
        for i in range(N):
            if arr[i][j] != 0:    # 자석인 경우
                magnetic.append(arr[i][j])    # magnetic에 append
        total_magnetic[j] = magnetic    # total_magnetic에 열별로 모은 자석 리스트 append

    for magnetic in total_magnetic:
        i = 0    # 새로운 열에 대해 생각할때마다 인덱스가 초기화되어야 한다.
        while i < len(magnetic):    # n극을 기준으로 생각할 것
            if i == len(magnetic)-1:    # 마지막 요소일 경우
                i += 1    # 아무 것도 체크하지 않고 그냥 인덱스 추가
            else:    # 그 외의 경우
                if magnetic[i] == 1:    # 만약 N극일 경우
                    if magnetic[i+1] == 2:    # 바로 옆이 S극이면
                        result += 1    # 교착상태에 하나 추가하고
                        i += 2    # 다다음 인덱스 확인
                    else:    # 그 외의 경우에는
                        i += 1    # 그냥 다음 인덱스 확인
                else:    # S극일 경우에는
                    i += 1    # 그냥 고려하지 않고 다음 인덱스 확인

    print(f'#{tc} {result}')