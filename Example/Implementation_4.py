# <문자열 재정렬>
# 틀림 - 숫자가 없을 때를 고려하지 않음

# input_data = input()
# num = list(map(str,[1,2,3,4,5,6,7,8,9,0]))
# nums = 0
# char = []

# for i in range (len(input_data)):
#     if input_data[i] in num:
#         nums += int(input_data[i])
#     else:
#         char.append(input_data[i])
# char.sort()

# print("".join(char)+str(nums))

# 해답

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))
