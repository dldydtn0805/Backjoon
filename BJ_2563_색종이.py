t = int(input())

total = [[0 for _ in range(100)] for _ in range(100)] # 2차원 배열 선언

for i in range(t): #총 T개의 사각형을 만들어준다
    x, y = map(int, input().split()) #각 사각형의 시작점을 입력, 여기부터 10 만큼 2차원으로 채워진다 
    for row in range(x, x+10):
        for col in range(y, y+10):
            total[row][col] = 1 #total에서 사각형 영역에 해당하는 부분을 1로 채워준다

result = 0
for i in total: #전체 영역을 탐색한다
    result += i.count(1) #전체 영역에서 구성요소인 각 리스트에서 1의 개수를 카운팅 해서 모든 리스트에있는 1의 값을 result에 더해준다
print(result)