
def func(x, y):
    if y == '@':
        return float(x)*3
    elif y == '%':
        return float(x)+5
    elif y == '#':
        return float(x)-7


t = int(input())
for i in range(t):
    case = list(input().split())
    while len(case) != 1:
        case[1] = func(case[0], case[1])
        case.pop(0)
    print(f'{case[0]:.2f}')
