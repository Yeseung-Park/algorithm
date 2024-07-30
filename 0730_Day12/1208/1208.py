# Flatten

import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    dump = int(input())    # 주어진 시행 횟수

    boxes = list(map(int, input().split()))

    case = 0    # 실제 시행 횟수

    difference = 0    # 높이차 초기 설정

    while case < dump:

        for i in range(len(boxes)-1, 0, -1):
            for j in range(0, i):
                if boxes[j] > boxes[j+1]:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]    # boxes 오름차순 정렬

        boxes[len(boxes)-1] -= 1
        boxes[0] += 1    # 덤프 해주기

        for i in range(len(boxes)-1, 0, -1):
            for j in range(0, i):
                if boxes[j] > boxes[j+1]:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]    # boxes 오름차순 재정렬

        difference = boxes[len(boxes)-1]-boxes[0]    # 높이차 계산
        case += 1    # 시행 횟수에 1 추가

        if difference <= 1:
            print(f'#{tc} {difference}')
            break    # 만약 높이차가 1 이하가 된다면 결과를 출력하고 반복문을 빠져나감
        else:
            continue    # 그 외의 경우 반복문 계속 하기

    print(f'#{tc} {difference}')    # 결과 출력