# 30

letter = list(map(int,input()))
if 0 not in letter or sum(letter) % 3 != 0:
    print(-1)
else:
    letter.sort(reverse=True)
    print("".join(map(str,letter)))



