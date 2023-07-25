def min_def(x, y):
    result_x = []
    i = 2
    while x != 1:
        if x % i == 0:
            x //= i
            result_x.append(i)
        else:
            i+=1
    result_y = []
    i = 2
    while y != 1:
        if y % i == 0:
            y //= i
            result_y.append(i)
        else:
            i+=1
    return tuple(set(result_x)&set(result_y))[-1]

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if x == 1 or y == 1:
        result = x*y
    elif min_def is True:
        result =  x*y // min_def(x, y)
    else:
        result = x*y
    print(result)