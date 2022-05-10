import sys

T = int(input())

for i in range (T):
    number = 1
    score = []
    N = int(input())
    for j in range (N):
        score.append(list(map(int,sys.stdin.readline().split())))
    score.sort(key = lambda x: x[0])

    # (1,4)(2,3)(3,2)(4,1)(5,5)
    minS = score[0][1]
    for k in score:
        if k[1] < minS:
            number+=1
            minS = k[1]
    print(number)
