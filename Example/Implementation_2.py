# <시각> - 완전 탐색 (brute-force)

n = int(input())

count = 0

for hour in range (0,n+1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(hour) or '3' in str(min) or '3' in str(sec):
                count += 1
            else:
                continue

print(count)

# 해답

# h = int(input())

# count = 0
# for i in range (h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 count+=1

# print(count)


