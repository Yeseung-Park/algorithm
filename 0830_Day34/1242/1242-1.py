import sys

sys.stdin = open('input.txt')

def hexadecimal_to_binary(n):
    hex = '0123456789ABCDEF'
    bi = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    binary = ''
    for num in n:
        temp = bi[hex.index(num)]
        binary += temp

    return binary

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N, M = map(int, input().split())
    code = [input().strip() for _ in range(N)]
    possible_code = set()    # code에서 16진수로 나타내져있는 가능성이 있는 부분 담기
    real_code_list = []    # 실제 2진수로 변환한 코드 담는 리스트
    password_list = []

    for i in range(N):
        string = code[i].strip('0')
        if string == '':
            pass
        else:
            temp = []
            zero = 0
            for num in string:
                if num != '0':
                    zero = 0
                    temp.append(num)
                else:
                    zero += 1
                    if zero > M//14:
                        temp = temp[:len(temp)-zero]
                        possible_code.add(''.join(temp))
                        temp = []
                    else:
                        temp.append(num)

    print(possible_code)

    # 근데 이렇게 하면 암호코드의 첫번째랑 마지막이 0인 경우는 어떻게 해?
    # 마지막이 0인 경우는 없을 것 같다.
    # possible_code를 이진수로 변환하고 56의 배수가 아니라면 가장 가까운 56의 배수가 될 때까지 0을 앞에 더해주기

    for pos_code in possible_code:
        temp1 = hexadecimal_to_binary(pos_code)
        temp2 = temp1.strip('0')    # 필요 없는 0은 다 지우기

        print(temp2)
        print(len(temp2))
        if len(temp2) >= 56:
            if len(temp2) % 56 != 0:    # 지운게 56의 배수가 아니라면
                x = (len(temp2)//56+1)*56 - len(temp2)
                y = len(temp2) % 56
                if x < y:
                    temp2 = '0'*x + temp2
                    real_code_list.append(temp2)
                else:
                    temp2 = temp2[len(temp2)%56:]
                    real_code_list.append(temp2)
                # real_code_list.append(temp2[len(temp2)%56:])    # 앞의 0을 그만큼 빼버리기
            else:    # 아니면
                real_code_list.append(temp2[:])    # temp2가 코드 전체
        else:
            temp2 = '0'*(56-len(temp2)) + temp2
            real_code_list.append(temp2)

    print(real_code_list)
    for real_code in real_code_list:
        print(real_code)
        print(len(real_code))
        k = len(real_code)//56
        print(k)
        switch = {'000'*k+'11'*k+'0'*k+'1'*k: '0', '00'*k+'11'*k+'00'*k+'1'*k: '1',
                  '00'*k+'1'*k+'00'*k+'11'*k: '2', '0'*k+'1111'*k+'0'*k+'1'*k: '3',
                  '0'*k+'1'*k+'000'*k+'11'*k: '4', '0'*k+'11'*k+'000'*k+'1'*k: '5',
                  '0'*k+'1'*k+'0'*k+'1111'*k: '6', '0'*k+'111'*k+'0'*k+'11'*k: '7',
                  '0'*k+'11'*k+'0'*k+'111'*k: '8', '000'*k+'1'*k+'0'*k+'11'*k: '9'}
        password = ''
        for i in range(0, len(real_code)-7*k+1, 7*k):
            temp = real_code[i:i+7*k]
            if temp == '0'*(7*k):
                pass
            else:
                password += switch[temp]
        password_list.append(password)

    print(password_list)
    result_list = []

    for password in password_list:
        verify = 0
        for i in range(len(password)-1):
            if i%2 == 0:    # 홀수번째 숫자면
                verify += int(password[i])*3
            else:
                verify += int(password[i])
        verify += int(password[-1])
        if verify % 10 == 0:    # 10의 배수라면 맞는 비번이니까
            temp = list(map(int, password))
            result_list.append(sum(temp))

    result = sum(result_list)

    print(f'#{tc} {result}')



    # print(possible_code)
    # print(real_code_list)