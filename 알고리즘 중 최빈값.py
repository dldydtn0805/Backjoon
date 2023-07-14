T = int(input())
for i in range(T):
    count = {}
    temp = []
    case = int(input())
    temp = list(map(int, input().split()))
    for i in temp:
        try: count[i] += 1
        except: count[i] = 1
    A = []
    for key, value in count.items():
        A.append(value)
        A.sort()
    for key, value in count.items():
        if value == (A[-1]):
            print(f"#{case} {key}")