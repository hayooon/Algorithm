# <왕실의 나이트>

import re


cols = ['a','b','c','d','e','f','h']

loc = input()

row = int(loc[1])
col = cols.index(loc[0]) + 1
print(row, col)

dr = [2, 2, -2, -2, 1, -1, 1, -1]
dc = [1, -1, 1, -1, 2, 2, -2, -2]

count = 0

for i in range (8):
    nx = row + dr[i]
    ny = col + dc[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count+=1

print(count)

# 해답

# # 현재 나이트의 위치 입력 받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (11, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운드 증가
#     if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
#         result += 1

# print(result)