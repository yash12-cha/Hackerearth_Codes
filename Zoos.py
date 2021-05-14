    s = input("")
    X = 0
    Y = 0
    if len(s) > 20 :
        print("Limited Exceed.")
    else:
        for i in range(0,len(s)):
            if s[i] == 'z' or s[i] =='Z':
                X = X + 1
            else :
                Y = Y + 1
        c = 2 * X
        if ( c == Y):
            print("Yes")
        else:
            print("No")
