original = []
modified_original = []
for _ in range(5):
    case = input()
    original.append(case)
temp = 0
for i in original:
    if len(i) >= temp:
        temp = len(i)        
for i in original:
    A = i+str('*')*(temp-len(i))
    modified_original.append(A)
for col in range(temp):
    for row in range(5):
        if modified_original[row][col] == '*':
            pass
        else:
            print(modified_original[row][col], end='')