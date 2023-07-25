hour, min, sec = map(int, input().split())
min_sec = int(input())

def time_oven(hour, min, sec, min_sec):

    sec += min_sec
    while sec >= 60:
        sec -= 60
        min += 1
        while min >= 60:
            min -= 60
            hour +=1
            if hour >= 24:
                hour = 0
    return hour, min, sec

result = time_oven(hour, min, sec, min_sec)
print(result[0], result[1], result[2])

