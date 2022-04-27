# <동전 0>

N, K = map(int,input().split())
count = 0
remain = 0
A = []
for i in range(N):
    A.append(int(input()))

A.sort(reverse=True)

for i in A:
    count += K // i
    K %= i

print(count)



