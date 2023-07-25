def fun(x,y,z):
    if y == '+':
        return x+z
    elif y == '*':
        return x*z
    
A = int(input())
B = input()
C = int(input())

result = fun(A,B,C)
print(result)