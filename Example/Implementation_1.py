# <상하좌우>
# n = int(input())

# dir = list(map(str,input().split()))
# print(dir)

# # L: 왼쪽으로 한 칸 이동
# # R: 오른쪽으로 한 칸 이동
# # U: 위로 한 칸 이동
# # D: 아래로 한 칸 이동

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0 ,0]

# # 현재 위치
# x, y = 1, 1

# for i in dir:
#     if (i == "L"):
#         if (x+dx[0]<1 or y+dy[0]<1 or x+dx[0]>n or y+dy[0]>n):
#             continue
#         x += dx[0]
#         y += dy[0]
        
#     elif (i == "R"):
#         if (x+dx[1]<1 or y+dy[1]<1 or x+dx[1]>n or y+dy[1]>n):
#             continue
#         x += dx[1]
#         y += dy[1]
#     elif (i == "U"):
#         if (x+dx[2]<1 or y+dy[2]<1 or x+dx[2]>n or y+dy[2]>n):
#             continue
#         x += dx[2]
#         y += dy[2]
#     elif (i == "D"):
#         if (x+dx[3]<1 or y+dy[3]<1 or x+dx[3]>n or y+dy[3]>n):
#             continue
#         x += dx[3]
#         y += dy[3]
#     else:
#         pass

# print(x,y)

# 해답

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range (len(move_type)):
        if plan == move_type[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
