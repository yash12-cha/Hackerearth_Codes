i = int(input(""))
lis = list(map(int,input().strip().split()))[:i]
s = sum(lis)
t = []
for p in lis:
    if (s - p) % 7 == 0 :
        t.append(p)
if len(t) == 0:
    print(-1)
else:
    print(lis.index(min(t)))
