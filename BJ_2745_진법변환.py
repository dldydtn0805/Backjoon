n, b = input().split()
case = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0
for i in range(len(n)):
    sum += case.index(n[-i-1])*int(b)**i
print(sum)