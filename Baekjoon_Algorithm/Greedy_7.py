# 로프
# 40 30 20 10
N = int(input())
ropes = []
for i in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

maxWeight = 0
weight = 0

for i in range (N):
    weight = ropes[i]*(i+1)

    if weight > maxWeight:
        maxWeight = weight

print(maxWeight)




