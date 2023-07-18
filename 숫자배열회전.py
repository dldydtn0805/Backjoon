T = int(input())
N = int(input())
for i in range(N):
    original = list(map(str, input().split()))

for row in range(N):
    for col in range(N):
        print(original[N-col][row])
        print(original[N-row][N-col])