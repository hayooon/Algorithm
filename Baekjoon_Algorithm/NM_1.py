n, m = map(int, input().split())
s = []
check = [False] * n

def nm(n,m):
    if (len(s) == m):
        print(" ".join(map(str,s)))
    else:
        for i in range(n):
            if (check[i]==False):
                check[i]=True
                s.append(i+1)
                nm(n,m)
                check[i]=False
                s.pop()
            else:
                continue

nm(n,m)