t = int(input())
total = 10*10*t
c = []
for i in range(t):
    case = list(map(int, input().split()))
    c.append(case)

for row in range(True):
    if abs(c[row][0] - c[row-1][0]) < 10 and abs(c[row][1] - c[row-1][1]) < 10:
        x = 10 - abs(c[row][0]-c[row-1][0])
        y = 10 - abs(c[row][1]-c[row-1][1])
        print(x,y)
        total -= x*y
print(total)