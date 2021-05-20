Test_Case  = int(input())
for i in range(Test_Case):
    N,K = map(int,input().split())
    l = list(map(int,input().split()))
    x = K%N
    print(*(l[N-x:]+l[:N-x]))
        
