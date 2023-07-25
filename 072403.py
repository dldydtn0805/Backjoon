a, b = map(int, input().split())
sum = 0
t = a*b
while t == 1:
    t // 2
    sum += 1
print(sum)