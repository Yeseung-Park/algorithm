import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1,T+1):

    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    find_code = False
    code_table = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
                  '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}    # 변환 관계를 딕셔너리로 나타내주기

    # 모든 숫자는 7비트로 나타냈을 때 마지막 자리가 1이므로
    # 뒤에서부터 찾아서 1이 등장하면 그게 코드의 마지막인 부분이고 그것부터 56자리
    for i in range(N):
        for j in range(M-1, -1, -1):
            if code[i][j] == '1':
                true_code = code[i][j-55:j+1]
                find_code = True
                break
        if find_code:    # 코드 라인을 하나 찾으면 더 찾을 필요가 없으므로 빠져나오기
            break

    password = [0]*8    # 변환한 비밀번호를 담을 리스트

    for i in range(0, 50, 7):
        temp = true_code[i:i+7]    # 7자리씩 끊어서 보기
        password[i//7] = code_table[temp]    # 적절한 자리에 변환해서 넣기

    # 올바른 패스워드인지 확인하기

    verify = 0
    for i in range(8):
        if i % 2 == 0:    # 홀수 자리
            verify += password[i]*3
        else:    # 짝수 자리
            verify += password[i]

    if verify % 10 == 0:    # 올바른 암호코드
        print(f'#{tc} {sum(password)}')
    else:    # 잘못된 암호코드
        print(f'#{tc} 0')