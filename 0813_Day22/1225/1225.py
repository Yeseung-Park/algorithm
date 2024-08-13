import sys

sys.stdin = open('input.txt')


# Testcase 수
# T = int(input())
# Testcase 만큼 반복
for tc in range(1, 11):

    test_case = int(input())    # 테스트 케이스의 번호
    password = list(map(int, input().split()))    # 비밀번호가 될 수 있는 데이터

    password_complete = False    # 비밀번호가 완성되었는지 판단하는 boolean 값

    while not password_complete:    # 비밀번호가 완성될 때까지

        for i in range(1, 6):    # 1부터 5까지
            password[0] -= i    # 제일 앞 자리 수를 i만큼 빼주고
            if password[0] <= 0:    # 만약 0이랑 같거나 작아지면
                password[0] = 0    # 0이라고 해주기
            password.append(password[0])    # 뒤에 붙여주고
            password.pop(0)    # 앞에거 빼주고
            if password[-1] == 0:    # 맨 마지막 요소가 0이 되면
                password_complete = True    # 비밀번호가 완성된 것이니까
                break    # 반복문 빠져나가기

    print(f'#{test_case}', *password)