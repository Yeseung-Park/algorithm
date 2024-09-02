import sys

sys.stdin = open('input.txt')

def change(n, change_count):    # n은 숫자열의 길이, change_count는 일단 처음은 0
    if change_count == change_num:    # 문제에서 정한 만큼 자리바꿈이 일어났다면
        result = 0
        for k in range(len(numbers)):    # 그때의 숫자열의 값 계산해보기
            result += numbers[k]*(10**(len(numbers)-1-k))
        return result    # 값 반환

    # 현재 숫자열의 상태와 자리바꿈이 일어난 횟수를 함께 tuple로 지정하고
    # 해당 tuple이 memo 안에 있다면 (이미 한 번 등장한 숫자열이라면)
    state = tuple(numbers + [change_count])
    if state in memo:
        return memo[state]    # 한 번 더 계산 안 하고 그냥 그 값 그대로 반환

    maximum = 0    # 기본 최댓값
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] != numbers[j]:    # 같은 원소끼리는 바꿀 필요가 없지
                numbers[i], numbers[j] = numbers[j], numbers[i]    # 자리 바꾸고
                maximum = max(maximum, change(n, change_count+1))    # 최종 횟수에 도달할 때까지 자리를 바꾼다음에
                # 돌아오면 동시에 최댓값 비교해서 갱신
                numbers[i], numbers[j] = numbers[j], numbers[i]    # 이제 다시 다른 경우에 대해서 반복

    memo[state] = maximum    # 특정 숫자열일 때 최댓값을 해당 숫자열을 키로 갖는 딕셔너리의 값으로 저장
    return maximum    # 최댓값 반환

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    temp1, temp2 = input().split()
    numbers = list(map(int, temp1))
    change_num = int(temp2)    # 입력값 받아와서 적당히 정수 변환 해주고 변수 지정하기
    change_count = 0    # 몇 번 자리바꿈 했는지 확인하는 변수
    maximum = 0    # 최대값
    memo = {}    # memoization을 위한 딕셔너리
    # 함수를 한 번 돌릴 때마다 여기에다가 그 결과를 저장해줄 것이다.
    # 이게 시간초과가 안 나는 핵심이다.
    # 사실 GPT가 알려줬다.

    print(f'#{tc} {change(len(numbers), 0)}')