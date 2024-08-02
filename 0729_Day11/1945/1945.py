# 간단한 소인수분해

T=int(input())

for test_case in range(1, T+1):

    N=int(input())

    devide_2=True
    exp_2=0
    devide_3=True
    exp_3=0
    devide_5=True
    exp_5=0
    devide_7=True
    exp_7=0
    devide_11=True
    exp_11=0

    while devide_2==True:
        
        if N%2==0:
            N=N/2
            exp_2+=1
        elif N%2!=0:
            devide_2=False
    
    while devide_3==True:

        if N%3==0:
            N=N/3
            exp_3+=1
        elif N%3!=0:
            devide_3=False
    
    while devide_5==True:

        if N%5==0:
            N=N/5
            exp_5+=1
        elif N%5!=0:
            devide_5=False
    
    while devide_7==True:

        if N%7==0:
            N=N/7
            exp_7+=1
        elif N%7!=0:
            devide_7=False
        
    while devide_11==True:

        if N%11==0:
            N=N/11
            exp_11+=1
        elif N%11!=0:
            devide_11=False
        
    print(f'#{test_case} {exp_2} {exp_3} {exp_5} {exp_7} {exp_11}')
