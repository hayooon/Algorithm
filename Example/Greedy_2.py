# <곱하기 혹은 더하기>
num = []
text = input()
for i in range (len(text)):
    num.append(int(text[i]))
print(num)

result = num[0]

for i in range (1,len(num)):
    if (result == 0 or num[i] == 0):
        result += num[i]
    else:
        result *= num[i]

print(result)

# #해답

# data = input()
# result = int(data[0])

# for i in range (1, len(data)):
#     # 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)
