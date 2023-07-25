a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

def avg(a, b, c, d, e) :
    arg = [a, b, c, d, e]
    sum = 0
    for i in arg:
        if i < 40:
            i = 40
        sum += i
    return f'{sum / 5:.0f}' 

print(avg(a, b, c, d, e))