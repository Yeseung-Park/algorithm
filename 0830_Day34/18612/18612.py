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
for tc in range(1,T+1):

    hexadecimal = input()
    binary = hexadecimal_to_binary(hexadecimal)
    result = []

    for i in range(7, (len(binary)//7)*7+1, 7):    # 우선 7개씩 묶을 수 있을 만큼 묶기
        temp = binary[i-7:i]
        dec = 0
        for j in range(len(temp)):
            dec += 2**(6-j)*int(temp[j])
        result.append(dec)

    temp = binary[len(binary)//7*7:]    # 마지막 나머지들은 따로 계산해주기
    dec = 0
    for j in range(len(temp)):
        dec += 2**(len(temp)-1-j)*int(temp[j])
    result.append(dec)


    print(f'#{tc}', *result)