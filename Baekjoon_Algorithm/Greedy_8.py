# 주유소

# 17점
n = int(input())
distance = list(map(int,input().split()))
oil = list(map(int,input().split()))

total = 0
minValue = oil[0]

for i in range(n-1):
    if minValue > oil[i]:
        minValue = oil[i]
    total += minValue * distance[i]

print(total)

n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

# 100점 - subtask (price0)
total = 0
minValue = 0

for i in range(n-1):
    if price[i] < price[i+1]:
        price[i+1] = price[i]
    total += price[i] * distance[i]

print(total)