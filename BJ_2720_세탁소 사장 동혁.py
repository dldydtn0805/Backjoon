t = int(input())
moneys = [25, 10, 5, 1]
count = {}
for i in range(t):
    total = int(input())
    for money in moneys:
        count[money] = total//money
        total %= money
        print(count[money], end=' ')