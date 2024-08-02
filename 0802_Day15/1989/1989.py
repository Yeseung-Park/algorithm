import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    text = input()

    palindrom = True

    for i in range(len(text)//2):
        if text[i] == text[len(text)-1-i]:
            pass
        else:
            palindrom = False
            break

    if palindrom == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')