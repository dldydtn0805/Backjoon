
real_result = []
x = int(input())
for i in range(x):
    a, b, c = map(int, input().split())
    list_a = [a,b,c]
    if a == b == c:
        result = a * 1000 + 10000
    elif a == b:
        result = a * 100 + 1000
    elif b == c:
        result = b * 100 + 1000
    elif c == a:
        result = a * 100 + 1000
    else:
        result = max(list_a)*100
    real_result.append(result)
print(max(real_result))
    
