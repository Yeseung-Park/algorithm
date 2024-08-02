import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    str1 = input()
    str2 = input()

    same = False

    if str1 in str2:
        same = True

    if same == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')