import sys

sys.stdin = open('input.txt')

def count(x, list):    # list 안에서 x의 개수를 찾는 함수
    result = 0
    for num in list:
        if num == x:
            result += 1
    return result

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    # 기본적인 접근 방식은 루프 한바퀴를 1초라고 생각하고 정해진 시간이 될 때마다 붕어빵을 정해진 개수만큼 stack에 append한다.
    # 만약 손님이 왔는데 stack에 붕어빵이 없다면 impossible 하고 break!
    # 한 가지 의문은 손님이 동시에 도착하기도 하나? 맞다.
    # 0초에 손님이 오면 무조건 불가능하다!!

    N, M, K = map(int, input().split())
    guest = list(map(int, input().split()))
    bread_stack = []    # 만든 붕어빵을 담는 리스트
    second = 0    # 시간 (1초, 2초, 3초...)

    #가장 늦게 오는 손님은 언제 오는지 찾는 과정
    latest_guest = 0
    for num in guest:
        if num > latest_guest:
            latest_guest = num

    result = 'Possible'    # 기본 결과는 'Possible'로 설정

    while second <= latest_guest:    # 손님이 가장 늦게 오는 시간을 넘어설 때까지
        if second == 0:    # 만약 0초인데
            if second in guest:    # 손님이 온다면
                result = 'Impossible'    # 불가능하므로 result = 'Impossible'
                break
        else:    # 그 외의 경우
            if second % M == 0:    # 현재 시간이 M의 배수일 경우
                for _ in range(K):    # 한 번에 만들 수 있는 붕어빵의 수 K만큼
                    bread_stack.append(0)    # 붕어빵 스택에 append
            if second in guest:    # 현재 시간이 손님이 오는 시간이면
                for _ in range(count(second, guest)):    # 한 번에 오는 손님 수 만큼 붕어빵을 하나씩 빼는데
                    if not bread_stack:    # 만약 붕어빵이 없다면
                        result = 'Impossible'    # 불가능하므로 result = 'Impossible'
                        break
                    else:    # 그 외의 경우에는
                        bread_stack.pop()    # 붕어빵 빼기
        second += 1    # 시간 흐르기

    print(f'#{tc} {result}')