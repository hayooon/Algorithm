# < 보물 >

n = int(input())

list_a = list(map(int,input().split()))
list_b = list(map(int, input().split()))

count = 0
for i in range(n):
    count += min(list_a) * max(list_b)
    list_a.remove(min(list_a))
    list_b.remove(max(list_b))

print(count)