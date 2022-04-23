# <왕실의 나이트>

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