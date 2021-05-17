'''Logic:-

FIRST YOU HAVE TO FIGURE OUT WHICH IS THE MINIMUM VALUE.
FOR THAT LETS SEE THE COST AS function f(x)=Ax^2+B(n-x)^2,
WHERE x IS THE NUMBER OF TYPE 1 ITEMS.
YOU WILL GET MINIMUM FOR f'(x)=0 i.e. for x=nB/(A+B).'''

T = int(input())
for i in range(T):
    N,A,B = map(int, input().split())
    L1 = round((N*B)/(A+B))
    X = L1
    Y = N - L1
    k=A*(X**2)+B*(Y**2)
    print(k)
