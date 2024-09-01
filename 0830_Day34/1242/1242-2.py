import sys

sys.stdin = open('input.txt')

def hexadecimal_to_binary(n):
    hex_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    binary = ''
    for num in n:
        binary += hex_bin[num]

    return binary

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    pseudo = [input().strip() for _ in range(N)]
    codes = set()
    password_list = set()

    # print(pseudo)
    # 끝에는 무조건 0이 아니므로 뒤에서부터 0이 아닌 문자를 찾고 14개, 28개... 이런 식으로 찾는 범위를 넓히기
    # 그냥 이진수로 먼저 바꾸는게 낫겠다. 그러면 56개, 112개... 이런 식으로 찾는 범위 넓히기
    # 우선 예쁘게 만들자.

    # 오른쪽에 있는 0을 다 없애고 남은 애들을 이진수로 만들어서 codes에 넣기
    for i in range(N):
        pseudo[i] = pseudo[i].rstrip('0')
        pseudo[i] = hexadecimal_to_binary(pseudo[i])
        if pseudo[i] != '':
            codes.add(pseudo[i])

    # 패스워드 추출하기
    for code in codes:
        i = len(code)-1    # 맨 끝부터 검색
        while i > 0:
            if code[i] != '0':    # 0이 아닌게 등장하면 그때부터 실제 코드
                k = 56    # 길이를 56, 128, ... 로 늘리면서 판단할 예정
                while True:
                    is_code_true = True    # 대응하는 비밀번호를 찾았는지 확인하는 변수
                    temp = code[i-k+1:i+1]    # 길이만큼 떼어내고
                    weight = k // 56    # 두께 정하고
                    password = ''    # 실제 비밀번호
                    # 두께에 따라서 달라지는 대응관계
                    switch = {'000' * weight + '11' * weight + '0' * weight + '1' * weight: '0', '00' * weight + '11' * weight + '00' * weight + '1' * weight: '1',
                              '00' * weight + '1' * weight + '00' * weight + '11' * weight: '2', '0' * weight + '1111' * weight + '0' * weight + '1' * weight: '3',
                              '0' * weight + '1' * weight + '000' * weight + '11' * weight: '4', '0' * weight + '11' * weight + '000' * weight + '1' * weight: '5',
                              '0' * weight + '1' * weight + '0' * weight + '1111' * weight: '6', '0' * weight + '111' * weight + '0' * weight + '11' * weight: '7',
                              '0' * weight + '11' * weight + '0' * weight + '111' * weight: '8', '000' * weight + '1' * weight + '0' * weight + '11' * weight: '9'}
                    for j in range(0, k, 7*weight):    # 하나씩 보자
                        if switch.get(temp[j:j+7*weight]) is None:    # 만약 대응되는 것이 없으면
                            is_code_true = False    # 현재 코드는 k만큼의 길이를 가진 것이 아니라는 것
                            break    # 빠져나오기
                        else:    # 그 외의 경우에는
                            password += switch[temp[j:j+7*weight]]    # 계속 패스워드 만들어주기
                    if not is_code_true:    # 현재 코드가 k 만큼의 길이를 가진 것이 아니기 때문에
                        k += 56    # 다음 길이로 계속 판단
                    else:    # 그 외에는 이게 비밀번호가 맞으니까
                        password_list.add(password)    # 비밀번호 set에 넣기
                        break    # 빠져나오기
                i -= k    # 탐색한 만큼 앞으로 가서 재탐색
            else:    # 0일 경우에는
                i -= 1    # 한 칸씩만 앞으로 가기

    # 맞는 비밀번호인지 확인하는 부분
    real_password_sum = []
    for password in password_list:
        verify = 0
        for i in range(len(password)-1):
            if i % 2 == 0:
                verify += int(password[i])*3
            else:
                verify += int(password[i])
        verify += int(password[-1])
        if verify % 10 == 0:
            real_password = list(map(int, password))
            real_password_sum.append(sum(real_password))

    result = sum(real_password_sum)

    print(f'#{tc} {result}')