T = int(input())
for i in range(T):
    B = []
    N = int(input())
    A=list(map(int,input().split()))
    A.sort()
    for j in range(N-1):
        P = A[j]
        Q = A[j+1]
        result = (P & Q) ^ (P | Q)
        B.append(result)
    M= min(B)
    print(M)
