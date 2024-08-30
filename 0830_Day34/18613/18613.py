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

    hex = input().strip()
    binary = hexadecimal_to_binary(hex)
    num_of_zero = 0
    code = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
            '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}
    result = []

    for i in range(len(binary)-1, 0, -1):    # 앞 뒤의 쓸모없는 0이 몇개인지 찾기
        if binary[i] == '0':
            num_of_zero += 1
        else:
            break

    real_binary = binary[num_of_zero:len(binary)-num_of_zero]    # 쓸모없는 0을 제외한 애들만 빼기

    for i in range(0, len(real_binary)-5, 6):    # 코드 변환
        result.append(code[real_binary[i:i+6]])

    print(f'#{tc}', *result)