    t = int(input(""))
    n = int(input(""))
    for i in range(0,t):
        x1,y1 = (i-1,0)
        x2,y2 = (i + 1 ,0)
        x3,y3 = (i,0)
    result = abs(x1) + abs(y1) + abs(x2) + abs(y2)+ abs(x3)+ abs(y3)
    print(result) 
