import sys    # korean keyboard didn't work so I wrote annotation in english just for this time

sys.stdin = open('input.txt')

def bracket(arr):    # function for examining bracket
    stack = []    # declaring stack

    for string in arr:
        if string == '(':   # if string is (
            stack.append(string)     # insert string into stack
        elif string == ')':    # if string is )
            if stack == []:    # but stack is empty
                return -1
                break    # it means it doesn't match, so get out of loop
            else:    # else
                stack.pop()    # take out the last element of stack and delete it

    if stack != []:    # after the for loop if stack isn't empty
        return -1    # it means it doesn't match, so return -1
    else:    # else
        return 1    # bracket matches well and return 1

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    arr = input().strip()
    result = bracket(arr)

    print(f'#{tc} {result}')