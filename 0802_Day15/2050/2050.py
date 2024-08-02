import sys

sys.stdin = open('input.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):
arr = list(input())
result = []

for alpha in arr:
    result.append(ord(alpha)-64)

print(*result)