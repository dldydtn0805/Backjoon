a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

x = [a,c,e]
y = [b,d,f]
result = []

for i in x:
    if x.count(i) == 1:
        result.append(i)
for i in y:
    if y.count(i) == 1:
        result.append(i)

print(*result)


