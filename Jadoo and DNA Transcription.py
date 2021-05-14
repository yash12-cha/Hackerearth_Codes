    string=input()
    flag='a'
    st=[]
    for i in string:
        if i=='A' :
            st.append('U')
        elif i=='G':
            st.append('C')
        elif i=='C':
            st.append('G')
        elif i=='T':
            st.append('A')
        else:
            print("Invalid Input")
            flag='b'
            break
    if flag=='a':
        for j in st:
            print(j,end="")
