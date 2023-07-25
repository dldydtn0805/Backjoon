T = int(input())
a = int(input())
case_list = list(map(str, input().split()))

for i in case_list[1:]:
    if i == '@':
        i =case_list[case_list.index(i)-1]*3
    elif i == '%':
        i =case_list[case_list.index(i)-1]+5
    elif i == '#':
        i = case_list[case_list.index(i)-1]-7
    
print(case_list[-1])