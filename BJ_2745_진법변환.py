n, b = input().split()
case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# new = []
# 진법 변환 = 10**자리수 * 해당 자리 번호
sum = 0
for i in range(len(n)):
    # print(int(b)**i)
    # print(case.index(n[-i-1])*int(b)**i)
    # sum += (int(new.index(b[-i]))*((new.index(b))**int((n[-i]))))
    # print(new.index(b)) #35
    # print(case2.index(n[-i-1]))
    sum += case.index(n[-i-1])*int(b)**i
print(sum)