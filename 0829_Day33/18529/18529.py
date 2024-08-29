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

    N, hexa = input().split()

    result = hexadecimal_to_binary(hexa)

    print(f'#{tc} {result}')