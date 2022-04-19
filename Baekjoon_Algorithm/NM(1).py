
s = []

def nm(n,m):
    if (len(s) == m):
        print(s)
    else:
        for i in range (0,n):
            if (i not in s):
               s.append(i)
               nm(n,m)
            else:
                continue

n, m = map(int,input().split())
nm(n,m)