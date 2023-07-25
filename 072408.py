T = int(input())

def function(A, X): 
    if X == '@':
        return float(A)*3
    elif X == '%':
        return float(A)+2
    elif X == '#':
        return float(A)-7
    else:
        return A
for i in range(T):
    cases = list(input().split())
    for i in range(len(cases)):
        cases[i] = function(cases[i-1], cases[i])