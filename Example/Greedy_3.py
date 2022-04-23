# <모험가 길드>
# 틀림
# N = int(input())

# group = list(map(int, input().split()))

# group.sort(reverse=True)

# start = 0
# count = 0

# while True:
#     if (start >= len(group)):
#         break
#     elif (group[start] > len(group[start:])):
#         break
#     else:
#         count += 1
#         start += group[start]
# print (count)

# 해답
# 오름차순으로 풀기

n = int(input())
data = list(map(int, input().split()))        
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인
    count += 1 # 현재 그룹에 해당하는 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력