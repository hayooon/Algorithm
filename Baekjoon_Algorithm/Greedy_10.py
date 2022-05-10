# 수들의 합

# (시간초과)
# N = int(input())
# number = []
# i = 1

# while(True):    
#     if i not in number:
#         if N-i <= i:
#             number.append(N)
#             break
#         else:
#             N -= i
#             number.append(i)
#     i+=1

# # print(number)
# print(len(number))

# 다른 풀이
N = int(input())
i = 1
while(True):
    if i * (i + 1) / 2 > N:
        break
    else:
        i += 1
print(i - 1)
        
        