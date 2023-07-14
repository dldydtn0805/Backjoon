T = int(input())
for test_case in range(T):
    num_A, num_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    total = []
    if (len(A)) < (len(B)):           
        for x in range((len(B)-len(A)+1)):  
            temp = 0  
            for i in range(len(A)):
                sum = 0                                                              
                sum += B[(i+x)]*A[i]
                temp += sum      
            total.append(temp)
            total.sort()             
    elif (len(A)) > (len(B)):        
        for x in range((len(A)-len(B)+1)):
            temp = 0    
            for i in range(len(B)):
                sum = 0                                        
                sum += A[(i+x)]*B[i]
                temp += sum                              
            total.append(temp)
            total.sort()
    else:       
        temp = 0
        for i in range(len(B)):
            sum = 0                                  
            sum += A[i]*B[i]
            temp += sum             
            total.append(temp)    
        total.append(temp)
        total.sort()
    print(f"#{test_case+1} {total[-1]}")