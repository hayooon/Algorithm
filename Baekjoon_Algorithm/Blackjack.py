# 시도 #1
n, m = map(int, input().split())
card = []
for i in map(int,input().split()):
    card.append(i)

# print(" ".join(map(str,card)))

sums = []

def blackjack():

    for i in range(n):
        for j in range (i+1,n):
            for k in range(j+1,n):
                sum = card[i] + card[j] + card[k]
                if (sum > m):
                    continue
                else:
                    sums.append(sum)

    max = sorted(sums,reverse=True)
    print(max[0])
    # return 0

blackjack()