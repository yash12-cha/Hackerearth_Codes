N = int(input())
count = 0
for i in range(N):
    w,h = map(int,input().split())
    p = max(w,h)
    q = min(w,h)
    if (p / q) >= 1.6 and (p/q) <= 1.7:
        count = count + 1
print(count)

'''We use max(w,h)/min(w,h) so that always the longer side gets divided by the smaller side. 
