a, b = map(int, input().split())
count = 0
while a != 1:
    if a % 2 == 1:
        a -= 1
        count += 1
    else:
        a //= 2
        count += 1

while b != 1:
    if b % 2 == 1:
        b -= 1
        count += 1
    else:
        b //= 2
        count += 1

print(count)