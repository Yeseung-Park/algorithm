import sys

sys.stdin = open('input.txt')

def find_max(list):
    maximum = 1
    for num in list:
        if num > maximum:
            maximum = num
    return maximum

def find_min(list):
    minimum = 1000
    for num in list:
        if num < minimum:
            minimum = num
    return minimum

def sorting(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(0, i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())    # 당근의 개수
    carrots = list(map(int, input().split()))    # 당근의 크기
    # 당근의 크기가 항상 정렬되어서 나오지 않으므로 당근을 먼저 오름차순으로 정렬해준다.
    sorting(carrots)


    # 어차피 우리에게 중요한 것은 개수이다. 어떤 크기의 당근이 상자에 들어가는지가 아니라.
    # 그래서 인덱스를 각 상자에 들어가는 마지막 당근의 인덱스라고 생각하고
    # 각 상자에 해당하는 개수를 인덱스 값으로 계산해서 생각한다.
    # 이렇게 쓰긴 했지만 사실 제대로 이해한 것인지 모르겠다.

    minimum = 1000    # 최대로 차이나도 1000개까지만 차이나겠지
    possible = False    # 실제로 조건을 만족하는 상자가 존재하는지 확인하는 변수

    for i in range(1, N-1):    # small에 들어갈 당근 개수 고려
        # N-1까지인 이유는 모든 상자에 당근이 적어도 하나씩은 들어가야 하기 때문에 마지막 두 당근은 middle과 big 상자에 하나씩 들어갈 수 있도록 해야한다.
        # 처음에는 0부터 N-2까지라고 했는데 생각해보니 i 자체가 당근의 개수가 되어버리기 때문에 1부터 하는게 맞다.
        if carrots[i] == carrots[i-1]:    # 만약 현재 당근과 바로 전의 당근의 무게가 동일할 경우
            continue    # 바로 전의 당근도 넣어주기 위해 continue
        # 다를 경우에는 middle에 들어갈 당근 개수 고려
        for j in range(i+1, N):    # N까지인 이유는 모든 상자에 당근이 적어도 하나씩은 들어가야 하기 때문에 마지막 한 당근은 big 상자에 들어갈 수 있도록 해야한다.
            if carrots[j] == carrots[j-1]:    # 만약 현재 당근과 바로 앞의 당근의 무게가 동일할 경우
                continue    # 바로 앞의 당근도 넣어주기 위해 continue

            # 여기까지 넘어왔다면 각 상자에 들어가야 할 당근의 개수는 다 정한 것이다.
            # 상자 = 상자에 들어갈 당근의 개수
            small = i    # small 박스에는 앞에서 i번째까지 당근을 봤기 때문에 i개의 당근이 들어가야 한다.
            middle = j - small    # middle 박스에는 j번째까지의 당근을 봤고 그 중 small 박스에 들어간 당근은 제외하고 들어간다.
            big = N - (small + middle)    # big 박스에는 small과 middle에 들어가지 않은 당근이 들어간다.

            if small == 0 or middle == 0 or big == 0:    # 만약 아무것도 안 들어간 상자가 하나라도 있을 경우
                continue    # 현재 경우는 조건을 만족하지 않으므로 개수차를 고려할 필요도 없기에 continue

            if small > N//2 or middle > N//2 or big > N//2:    # 만약 N//2개를 초과한 상자가 하나라도 있을 경우
                continue    # 이 경우도 조건을 만족하지 않으므로 개수차를 고려할 필요도 없기에 continue

            # 여기까지 넘어왔다면 각 상자에 들어있는 당근의 개수가 모든 조건을 만족했다는 의미이다.
            # 그러면 박스 간의 당근 개수차를 구하자.

            possible = True    # 모든 조건을 만족하는 배치가 존재하므로 True로 바꾸기
            boxes = [small, middle, big]    # 상자 당 당근 개수를 한 번에 담은 boxes 리스트
            # 개수차라는 것은 가장 당근이 많은 상자와 적은 상자의 당근 개수 차이를 의미하는 것이고 우리는 다양한 경우의 수 중 그 개수차가 가장 작은 것을 찾는 것이다.
            diff = find_max(boxes) - find_min(boxes)
            if diff < minimum:    # 개수차가 minimum 보다 작을 경우
                minimum = diff    # 현재 개수차가 새로운 minimum

    if possible:    # 조건을 만족하는 개수 배치가 존재할 경우
        result = minimum    # 최소 개수차가 결과로
    else:    # 존재하지 않을 경우
        result = -1    # -1 반환

    print(f'#{tc} {result}')
