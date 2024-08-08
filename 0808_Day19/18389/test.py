# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):

    string = input()

    operator_stack = []
    prefix_arr = ""
    for s in string:
        if s in ['+', '-', '/', '*']:
            operator_stack.append(s)
        else:
            prefix_arr += s
    while operator_stack:
        prefix_arr += operator_stack.pop()
    print(f'#{tc} {prefix_arr}')