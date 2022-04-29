# < 회의실 배정 >

n = int(input())
meeting = []
for i in range (n):
    meeting.append(list(map(int,input().split())))

meeting.sort(key = lambda x: x[0])
meeting.sort(key = lambda x: x[1])

count = 0
finish = 0
for meet in meeting:
    if meet[0] >= finish:
        count += 1
        finish = meet[1]
    else: 
        continue

print(count)   

    



