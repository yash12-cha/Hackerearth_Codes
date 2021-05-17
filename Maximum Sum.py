
n = int(input())
arr = list(map(int, input().split()))
sum_ = count = 0
max_ = max(arr)
for i in range(n):
   if arr[i] >= 0:
       sum_ += arr[i]
       count += 1
if count == 0:
        print(max_, count+1)
else:
        print(sum_, count)
