import sys
s = int(sys.stdin.readline())
def max_func(s):
    cases = []
    i = 1
    while 1:
        cases.append(i)
        if sum(cases) > s:
            break
        i += 1
    return len(cases)-1

result = max_func(s)
print(result)