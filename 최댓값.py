Total = []
Original = []
for row in range(9):
    row = list(map(int, input().split()))

    row.sort()
    Total.append(max(row))
Total.sort()    
print(Total[-1])

if Total[-1]