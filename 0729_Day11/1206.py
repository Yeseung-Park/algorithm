# [S/W 문제해결 기본] 1일차 - View

for test_case in range(1, 11):

    N=int(input())

    buildings=list(map(int, input().split()))

    neighbor_building=[]

    sight_sum=[]

    result=0

    for i in range(2, N-2):
        neighbor_building=[buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]
        
        sight=[]

        sight_okay=True

        for j in range(4):

            if neighbor_building[j]>=buildings[i]:
                sight_okay=False
                break
        
        if sight_okay==True:
            for k in range(4):
                sight.append(buildings[i]-neighbor_building[k])
        
            for i in range(3, 0, -1):
                for j in range(0, i):
                    if sight[j]>sight[j+1]:
                        sight[j], sight[j+1]=sight[j+1], sight[j]
            
            sight_sum.append(sight[0])
    
    for sight in sight_sum:
        result+=sight
    
    print(f'#{test_case} {result}')