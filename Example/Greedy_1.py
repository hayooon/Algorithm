# <1이 될 때까지>
N, K = map(int, input().split())

count = 0

while(N != 1):

    if (N % K == 0):
        N = N // K
        count = count + 1
    else:
        N = N - 1
        count = count + 1

print(count)  

# # 해답
# N, K = map(int, input().split())

# result = 0

# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     target = ( N // K) * K
#     result += (n - target) # result에 1을 빼는 연산 횟수 더하기
#     n = target
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때 반복문 탈출)
#     if n < K :
#         break
#     # K로 나누기
#     result += 1
#     n //= K

#     #마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1)
# print(result) 
