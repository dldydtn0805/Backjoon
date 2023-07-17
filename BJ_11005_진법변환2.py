n, b = map(int, input().split())
case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_case = []
# 진법 변환 = 10**자리수 * 해당 자리 번호
# sum = 0
# for i in range(len(n)):
    # print(int(b)**i)
    # print(case.index(n[-i-1])*int(b)**i)
    # sum += (int(new_case.index(b[-i]))*((new_case.index(b))**int((n[-i]))))
    # print(new_case.index(b)) #35
    # print(case2.index(n[-i-1]))
    # sum += case.index(n[-i-1])*int(b)**i
# print(sum)
        # new_case.append((int(b))**(len(str(n))-i))
        # n -= (int(n) // (int(b))**(len(str(n))-i)) * (int(b)**(len(str(n))-i))
        # int(n) // (int(b))**(len(str(n))-i)
###
#### new2 = []
#### for i in range(len(new_case)):
####     x = int(b)**i
####     new2.append(x)
#### 


# for i in range(len(str(n))):
#     if int(n) // (int(b))**(len(str(n))-i) != 0:  
#         new_case.append(int(n) % (int(b))**(len(str(n))-i))
# print(new_case)
# for i in range(len(new_case)):
#     while new_case[i] > int(b):
#         new_case[i] = new_case[i] // int(b)
# print(new_case)
# result = []
# for i in case:
#     if case.index(i) in new_case:
#         result.append(i)
# print(result)
