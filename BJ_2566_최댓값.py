# original = []
# max_original = []
# for i in range(9):
#     A = list(map(int, input().split()))
#     original.append(A)
#     max_original.append(max(A))
# print(max(max_original))
# for row in range(9):
#     for col in range(9):
#         if (original[row][col]) == (max(max_original)):
#             print(original.index(original[row+1]), original[row].index(original[row][col+1]))

original = []
for i in range(9):
    case = list(map(int, input().split()))
    original.append(case)
max_num = 0
original_i = 0
original_j = 0
for i in range(9):
    for j in range(9):
        if original[i][j] >= max_num:
            max_num = original[i][j]
            original_i = original.index(original[i])
            original_j = original[i].index(original[i][j])
print(max_num)
print(original_i+1, original_j+1)